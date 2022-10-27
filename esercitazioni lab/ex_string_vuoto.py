#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implementa una funzione leetv(line) che prende come input una stringa
line e la modifica in modo da avere una versione della stringa in
formato leetspeak. Esempio: `Programming Unit 1` diventa `pR09R4mm1N9_uN1t_1`
Per creare la stringa usare le seguenti regole:

    1) 'a', 'i', 'e', 'o', 'z', 's', e 'g'
        devono essere sostituite con
        '4', '1', '3', '0', '7', '5', e '9' rispettivamente
        a prescindere che siano lower- or UPPER-case
        (quindi la solita regola si applica a
        'A', 'I', 'E', 'O', 'Z', 'S', e 'G', rispettivamente);
    2) 'f', 'n', 'r', 'w', 'l', 'y' e 'x'  (lower-case) devono essere
        sostituite con la loro versione UPPER-case
        ('F', 'N', 'R', 'W', 'L', 'Y' e 'X', rispettivamente);
    3) tutte gli altri caratteri UPPER-case non menzionati in
        in (1) e (2) devono diventare lower-case (e.g., 'B' diventa 'b',
        mentre 'N' rimane 'N');
    4) ' ' (spazio) deve diventare '_' (underscore);
    5) tutti gli altri caratteri non devono cambiare

    La funzione deve ritornare una tupla definita come:
    - primo elemento della tupla contiene la stringa in leet-version
    - il secondo elemento e' un numero che conta il numero di caratteri
        sostituiti

    Ad esempio input e' `"My name is Neo"`, la funzione
    deve ritornare `('mY_N4m3_15_N30', 12)`.
"""
# ---------------------------------------------------------------------- #
#            INPUT                      EXPECTED OUTPUT
# tests = [('My name is Neo',             ('mY_N4m3_15_N30', 12),),
#          ('Follow the White Rabbit!',   ('F0LL0W_th3_Wh1t3_R4bb1t!', 13)),
#          ('What is the Matrix?',        ('Wh4t_15_th3_m4tR1X?', 12))]
# ----------------------------------------------------------------------- #


def leetv(line: str) -> tuple:
    changes = 0

    case_1 = ['a', 'i', 'e', 'o', 'z', 's', 'g']
    case_1_up = ['A', 'I', 'E', 'O', 'Z', 'S', 'G']
    change_1 = ['4', '1', '3', '0', '7', '5', '9']

    case_2 = ['f', 'n', 'r', 'w', 'l', 'y', 'x']
    change_2 = ['F', 'N', 'R', 'W', 'L', 'Y', 'X']

    final_string = line

    for i, letter in enumerate(line):
        if letter.isspace():
            final_string = final_string.replace(" ", "_")
            changes += 1
        if letter in case_1 or letter in case_1_up:
            index = case_1.index(letter)
            final_string = final_string.replace(
                final_string[i], change_1[index])
            changes += 1
        elif letter in case_2:
            final_string = final_string.replace(
                final_string[i], letter.upper())
            changes += 1
        elif letter.isupper() and letter not in change_1 and letter not in change_2:
            final_string = final_string.replace(
                final_string[i], letter.lower())
            changes += 1
    #print(f'\tline : {line}\n\tresult: {(final_string, changes)}')
    return (final_string, changes)


if __name__ == '__main__':
    # Valutazione
    tests = [('My name is Neo', ('mY_N4m3_15_N30', 12),),
             ('Follow the White Rabbit!', ('F0LL0W_th3_Wh1t3_R4bb1t!', 13)),
             ('What is the Matrix?', ('Wh4t_15_th3_m4tR1X?', 12))]
    # se assert vi da errore controllate il vostro output rispetto a
    # quello atteso. Se passate un test vi stampa > Test xx PASSED !
    for i, (inp, expt) in enumerate(tests, 1):
        out = leetv(inp)
        assert out == expt, f'\n{"="*50}\noutput {out}\nexpected {expt}\n{"="*50}'
        print(f'> Test {i} PASSED!')
