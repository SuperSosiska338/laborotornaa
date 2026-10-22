import sys
import math
import cli
import time
from calc import equation, stats, integration, series
from calc.arrays import MIN_VALUE, MAX_VALUE, MAX_COUNT, MAX_SEARCH, fill_full, binary_search
from calc.sorting import METHODS


def print_solve(args):

    count = sum(x is not None for x in [args.a, args.b, args.c])
    if count == 0:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
          raise ValueError("Введённый коэффициент не является целым числом")
    else:
        a, b, c = args.a, args.b, args.c

    equation.ogr(a, b, c)
    kind, d, roots = equation.solve(a, b, c)



    if kind == "Линейное":
        print("Уравнение линейное")
        print(f"x = {roots[0]:.3f}")
    else:
        print("Уравнение квадратное")
        print(f"Дискриминант: {d}")
        if len(roots) == 2:
            print(f"x1 = {roots[0]:.3f}")
            print(f"x2 = {roots[1]:.3f}")
        elif len(roots) == 1:
            print(f"x = {roots[0]:.3f}")
        else:
            print("Действительных корней нет")


def print_stats(args):

    if args.input:
        with open(args.input, "r", encoding="utf-8-sig") as n:
           num = n.read()
    else:
        #num = sys.stdin.read()
        num = []

    while True:
        a = input()
        num.append(a)
        if a == "":           
         break

    nums = ""
    for n in num:
         nums += n
     
    numders = nums.split()
    if not numders:
        raise ValueError("Список пуст")

    values = []
    for number in numders:
        try:
            val = float(number)
        except ValueError:
            raise ValueError(f"{number} не является числом")

        if not math.isfinite(val):
                       raise ValueError("Значение не является конечным")
           
        if abs(val) > stats.MAX_ABSNUM:
                       raise ValueError("Значение по модулю больше 10000")

        values.append(val)

    if len(values) > stats.MAX_NUM:
                raise ValueError("Чисел больше 20")

    

    number_table = [
        ("Количество", len, "d"),
        ("Сумма", stats.summa, ".3f"),
        ("Срднее арифметическое", stats.srednee, ".3f"),
        ("Сумма квадратов", stats.summa_kvadratov, ".3f"),
        ("Среднее квадратическое", stats.srednee_kvadrat, ".3f"),
        ("Дисперсия", stats.dispersia, ".3f"),
        ("СКО", stats.SKO, ".3f"),
        ("Стандартное отклонение", stats.standart_otlonenie, ".3f"),
        ("Наименьшее", stats.minimum, ".3f"),
        ("Наибольшее", stats.maximum, ".3f"),
        ("Положительных", stats.kol_polojitelnih, "d"),
        ("Отрицательных", stats.kol_otricatelnih, "d"), 
    ]

    for podpis, func, form in number_table:
         result = func(values)
         if result is None:
              print(f"{podpis}: НЕ СУЩЕСТВУЕТ")
         else:
              print(f"{podpis}: {result:{form}}")  

def print_series(args):
   # try:
    term, formula_str = series.FORMULAS[args.func]
   # except:
      #   raise ValueError("Неверная функция")

   

    if args.terms is not None:
        if not (1 <= args.terms <= series.MAX_TERMS):
            raise ValueError("Количество слагаемых вне диапазона")
        
        print(formula_str)
        res = series.summa_by_count(term, args.terms)
        count = args.terms
    else:
        if (not math.isfinite(args.eps) or not (0 < args.eps <= series.MAX_EPS)):
            raise ValueError("Точность вне диапазона")
        print(formula_str)
        res, count = series.summa_by_eps(term, args.eps)

    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {res:.4f}")

def print_integration(args):
     
 func, formula_str, low, high, limit = integration.FUNCTIONS[args.func]

 if not math.isfinite(args.a) or not math.isfinite(args.b):
        raise ValueError("Предел не является конечным числом")
 if args.a >= args.b:
        raise ValueError("начальный предел не меньше конечного")
 if not (1 <= args.steps <= 100000):
        raise ValueError("Количество шагов вне диапазона")
 if limit == False:
        if (args.a <= low or args.a >= high or args.b <= low or args.b >= high):
            raise ValueError("Предел вне промежутка")
 else:
      if (args.a < low or args.a > high or args.b < low or args.b > high):
            raise ValueError("Предел вне промежутка")
 print(formula_str)

 result = integration.integrate(func, args.a, args.b, args.steps)
 print(f"Значение интеграла: {result:.4f}")

def read_mas(path):
    try:
        if path:
            with open(path, "r", encoding="utf-8-sig") as f:
                text = f.read()
        else:
            lines = []
            while True:
                try:
                    line = input()
                    if not line.strip():
                        break
                    lines.append(line)
                except EOFError:
                    break
            text = " ".join(lines)

        text_with_spaces = text.replace(',', ' ')
        words = text_with_spaces.split()

        replace_words = [int(w) for w in words]

        if not (1 <= len(replace_words) <= MAX_COUNT):
            raise ValueError("количество элементов вне диапазона")

        for x in replace_words:
            if not (MIN_VALUE <= x <= MAX_VALUE):
                raise ValueError(f"значение элемента {x} вне диапазона")
    
        return replace_words
                     
    except Exception as e:
        raise ValueError(f"ОШИБКА чтения: {e}")
    


def write_mas(data, file):
    output = " ".join(str(x) for x in data) + "\n"
    if file:
        try:
            with open(file, "w", encoding="utf-8") as f:
                f.write(output)
                print(f"Записано элементов: {len(data)} в файл {file}")
        except Exception as e:
            raise ValueError(f"ОШИБКА записи в файл: {e}")
    else:
        sys.stdout.write(output)


def print_fill(args):
    if not (1 <= args.count <= MAX_COUNT):
        raise ValueError(f"количество элементов вне диапазона 1..{MAX_COUNT}")
    
    if args.min > args.max:
        raise ValueError("параметр min не может быть больше max")
    
    if not (MIN_VALUE <= args.min <= MAX_VALUE) or not (MIN_VALUE <= args.max <= MAX_VALUE):
        raise ValueError(f"границы должны быть внутри {MIN_VALUE}..{MAX_VALUE}")

    data = fill_full(args.count, args.min, args.max, args.seed)
    write_mas(data, args.output)


def time_sum(operation_name, operation, parameters):
    start_time = time.perf_counter()
    result = operation(*parameters)
    elapsed_time = time.perf_counter() - start_time
    print(f"Время операции sort ({operation_name}): {elapsed_time:.6f} с", file=sys.stderr)
    return result


def print_sort(args):
    data = read_mas(args.input)
    method = METHODS[args.method]
    descending = (args.order == "desc")

    time_sum(args.method, method, [data, descending])
    
    write_mas(data, args.output)
    print("Массив отсортирован")

    
def print_search(args):
    if not (-MAX_SEARCH <= args.value <= MAX_SEARCH):
        raise ValueError(f"модуль искомого не больше {MAX_SEARCH}")

    data = read_mas(args.input) 
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            raise ValueError("массив не упорядочен по возрастанию")
    
        
    index = binary_search(data, args.value)
    
    if index is None:
        raise ValueError(f"Значение {args.value} не найдено.")
    else:
        print(f"Значение {args.value} имеет элемент с индексом {index + 1}")
    

def main(argv):
   
    parser = cli.commandos()
    args = parser.parse_args(argv)
  

    if args.command is None:
        parser.print_help()


    handlers = {
        "fill": print_fill,
        "sort": print_sort,
        "integrate": print_integration,
        "series": print_series,
        "stats": print_stats,
        "solve": print_solve,
        "search": print_search
    }


    try:
     
        func = handlers.get(args.command)
        if func:
            return func(args)
     
    except (ValueError, OSError, KeyError) as error:
        err = str(error)
        if isinstance(error, OSError):
            err = "Файл не открывается"
        print(f"Ошибка:{err}", file=sys.stderr)
        return 1

    return 0

      
          

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))