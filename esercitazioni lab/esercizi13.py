# Ignorare le righe fino alla 31
from typing import Any, Callable, List, Tuple


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Esegue un test e controlla il risultato
def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "succeeded" if (result == expected) else "failed"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(
            f'{color}Test on {func_str} on input {args_str} {test_outcome}.\n'
            f'\tOutput: {result_str} Expected: {expected_str}\n')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')


# Definire una funzione che data una lista di interi, trovi
# la sotto-lista la cui somma degli elementi è massima.
# La funzione deve restituire la somma degli elementi in tale
# sotto-lista.
# La lista in input può avere sia elementi positivi che negativi,
# ma contiene almeno un elemento positivo.
# IMPORTANTE: Risolvere l'esercizio utilizzando un solo ciclo
# (vale a dire, ciascun elemento può essere analizzato soltanto una volta)
def max_sum_subsequence(arr: List[int]) -> int:
    max_sum = 0
    curr_sum = 0
    for n in arr:
        curr_sum += n
        max_sum += n if curr_sum > max_sum else 0
        curr_sum = max(curr_sum, 0)
    return max_sum


# Scrivere una funzione che prende due liste di interi. Ciascuna
# lista è ordinata in ordine crescente. Restituire una lista ordinata
# contenente tutti gli elementi nelle due liste. Se un elemento appare più
# volte e/o in entrambe le liste, tutte le copie di tale elemento dovranno
# apparire nella lista restituita.
# IMPORTANTE: Non usare sort/sorted e "passare" su ciascun elemento al massimo una volta.
def merge_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
    result = []
    i_1 = 0
    i_2 = 0
    while i_1 < len(list1) and i_2 < len(list2):
        if list1[i_1] < list2[i_2]:
            result.append(list1[i_1])
            i_1 += 1
        else:
            result.append(list2[i_2])
            i_2 += 1
    result.extend(list1[i_1:])
    result.extend(list2[i_2:])
    return result


# Scrivere una funzione che data una lista contenente rows x cols elementi
# costruisca una matrice di dimensioni rows x cols contenente gli elementi 
# della lista in ordine "a spirale", a partire dall'angolo a sinistra. 
# Si può assumere che la lista non contiene 0.
# Ad esempio:
#  Input: rows = 5
#         cols = 5
#         lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
#  Output: 
#         [[ 1 ,  2,  3,  4, 5 ],
#          [ 16, 17, 18, 19, 6 ],
#          [ 15, 24, 25, 20, 7 ],
#          [ 14, 23, 22, 21, 8 ],
#          [ 13, 12, 11, 10, 9 ]]
def list_to_matrix_spiral(lst: List[int], rows: int, cols: int) -> List[List[int]]:
    result = [[0 for _ in range(cols)] for __ in range(rows)]
    direction = 0
    row, col = 0, 0
    for el in lst:
        result[row][col] = el

        if direction == 0:
            col += 1
            if col == cols or result[row][col] != 0:
                col -= 1
                row += 1
                direction = 1
        elif direction == 1:
            row += 1
            if row == rows or result[row][col] != 0:
                row -= 1
                col -= 1
                direction = 2
        elif direction == 2:
            col -= 1
            if col < 0 or result[row][col] != 0:
                row -= 1
                col += 1
                direction = 3
        elif direction == 3:
            row -= 1
            if row < 0 or result[row][col] != 0:
                row += 1
                col += 1
                direction = 0
    return result


# Data una lista di interi e un intero target_sum, trovare (e restituire come coppia) due elementi
# la cui somma è uguale a target_sum. Il primo elemento della coppia deve essere minore o uguale al secondo.
# La funzione deve restituire None se non ci sono due elementi che hanno come somma quella specificata
# in target_sum.
# ATTENZIONE: Analizzare ciascun elemento solo una volta. Se necessario, potete ordinare la lista 
# prima di analizzare gli elementi.
def find_sum(lst: List[int], target_sum: int) -> Tuple[int, int]:
    for el in lst:
        lst_copy = lst.copy()
        lst_copy.remove(el)
        other = target_sum - el
        if other in lst_copy:
            return min(el, other), max(el, other)

    # Second solution provided by teacher
    # lst.sort()
    # first, second = 0, len(lst) - 1
    # while first < second:
    #     if lst[first] + lst[second] == target_sum:
    #         return lst[first], lst[second]
    #     elif lst[first] + lst[second] > target_sum:
    #         second -= 1
    #     else:
    #         first += 1


# Test funzioni
check_test(max_sum_subsequence, 6, [-2, 1, -3, 4, -1, 2, 1, -5, 4])
check_test(max_sum_subsequence, 10, [1, 2, 3, 4])
check_test(max_sum_subsequence, 2, [-1, 2, -3, -4])
check_test(merge_sorted_lists, [1, 2, 3, 4, 5, 6, 7, 8], [2, 4, 6, 8], [1, 3, 5, 7])
check_test(merge_sorted_lists, [1, 2, 3, 3, 4, 5, 6, 6, 7, 8], [2, 4, 6], [1, 3, 3, 5, 6, 7, 8])
check_test(list_to_matrix_spiral,
           [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]],
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 5, 5)
check_test(find_sum, (3, 7), [3, -2, 5, 1, 7], 10)
check_test(find_sum, None, [1, 3, 4, 1], 8)
check_test(find_sum, (-4, -2), [-2, 1, -4, 3, -2, 99], -6)
