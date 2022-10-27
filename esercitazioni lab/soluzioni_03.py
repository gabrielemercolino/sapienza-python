from typing import Any, Callable, List


# Stampa un test
def print_test(func: Callable, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        print(f'{func_str}({args_str}) => {result_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'ERROR: {func_str}({args_str}) => {error_str}')


################################################################################
# Stringhe
################################################################################


# Scrivere una funzione che ritorna una stringa di saluto formata da
# `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
def make_hello(name: str) -> str:
    return 'Ciao ' + name + '. ' + 'Buona giornata!'


# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`,
# che rimuove spazi all'inizio e alla fine della stringa.
# Usare solo costrutti del linguaggio e non librerie.
def strip_whitespace(string: str) -> str:
    # Soluzione elegante
    """ while string and string[0] == ' ':
        string = string[1:]
    while string and string[-1] == ' ':
        string = string[:-1]
    return string """
    # Soluzioni meno elegante
    start, end = 0, len(string) - 1
    while start < len(string) and string[start] == ' ':
        start += 1
    while end >= 0 and string[end] == ' ':
        end -= 1
    return string[start:end+1]


# Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# Usare solo costrutti del linguaggio e non librerie.
def split_string(string: str, characters: str = '') -> List[str]:
    substrings = ['']
    for character in string:
        if character in characters:
            substrings += ['']
        else:
            substrings[-1] += character
    result = []
    for substring in substrings:
        if substring:
            result += [substring]
    return result


# Scrivere una funziona che si comporta come `str.replace()`.
# Usare solo costrutti del linguaggio e non librerie.
def replace_substring(string: str, find: str, replace: str) -> str:
    # Trova una sottostringa in una stringa.
    def find_substring(string: str, substring: str) -> int:
        for index in range(0, len(string) - len(substring)):
            if string[index:index+len(substring)] == substring:
                return index
        return -1
    result = string
    length = len(find)
    position = find_substring(result, find)
    while position >= 0:
        result = result[:position] + replace + result[position+length:]
        position = find_substring(result, find)
    return result


# Scrivere una funzione che codifica un messaggio con il cifrario di
# Cesare, che sostituisce ad ogni carattere il carattere che si
# trova ad un certo offset nell'alfabeto. Quando si applica l'offset,
# si riparte dall'inizio se necessario (pensate a cosa fa il modulo).
# La funzione permette anche di decrittare un messaggio applicando
# l'offset in negativo. Si può assumere che il testo è minuscolo e
# fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.
# Suggerimento: Sono utili le funzioni `ord()` e `chr()`.
def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
    result = ''
    for character in string:
        if character == ' ':
            result += ' '
        else:
            index = ord(character) - ord('a')
            if not decrypt:
                offsetted = (index + offset) % 26
            else:
                offsetted = (index - offset + 26) % 26
            result += chr(ord('a') + offsetted)
    return result


# Test funzioni
print_test(make_hello, 'Pippo')
print_test(strip_whitespace, '  Pippo  ')
print_test(strip_whitespace, '   ')
print_test(split_string, 'Pippo Pluto  ', ' \t\r\n')
print_test(split_string, 'Pippo   Pluto  ', ' \t\r\n')
print_test(replace_substring, 'Ciao Pippo. Ciao Pluto.', 'Ciao', 'Hello')
print_test(caesar_cypher, 'ciao pippo', 17, False)
print_test(caesar_cypher, 'tzrf gzggf', 17, True)

################################################################################
# Liste
################################################################################


# Scrivere una funzione che somma i quadrati degli elementi di una lista.
def sum_squares(elements: List[int]) -> int:
    # Soluzione non elegante
    sum = 0
    for element in elements:
        sum += element * element
    return sum
    # Solizione elegante
    # return sum(element * element for element in elements)


# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
def max_element(elements: List[int]) -> int:
    max_ = 0
    for element in elements:
        if max_ <= element:
            max_ = element
    return max_


# Scrivere una funzione che rimuove i duplicati da una lista.
# Commentare sul tempo di esecuzione.
def remove_duplicates(elements: list) -> list:
    result = []
    for element in elements:
        if element not in result:
            result += [element]
    return result


# Scrivere una funzione che si comporta come `reverse()`.
# Usare solo costrutti del linguaggio e non librerie.
def reverse_list(elements: list) -> list:
    # slow implementation
    reversed = []
    for element in elements:
        reversed = [element] + reversed
    return reversed


# Scrivere una funzione `flatten_list()` che prende una lista che contiene
# elementi o altre liste, e ritorna una lista contenente tutti gli elementi.
# Si può assumere che le liste contenute non contengono altre liste.
# Usare la funzione `isinstance()` per determinare se un elemento è una lista.
# Usare solo costrutti del linguaggio e non librerie.
def flatten_list(elements: list) -> list:
    flattened = []
    for element in elements:
        if isinstance(element, list):
            flattened += element
        else:
            flattened += [element]
    return flattened


# Test funzioni
print_test(sum_squares, [1, 2, 3])
print_test(max_element, [1, 2, 3, -1, -2])
print_test(remove_duplicates, [1, 2, 3, 2, 3])
print_test(reverse_list, [1, 2, 3])
print_test(flatten_list, [1, [2, 3]])
