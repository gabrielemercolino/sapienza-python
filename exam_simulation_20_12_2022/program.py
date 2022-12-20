#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import images
import os

################################################################################
################################################################################
################################################################################

""" Operations to do FIRST OF ALL:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and MATRICULATION NUMBER
 3) Change the directory name examPY in your matriculation number

To pass the exam you have to:
    - solve at least 3 func problems and
    - solve at least 1 rec problem
    - get a score greater or equal tu 18

The final score is the sum of the solved problems.
"""
name = "Gabriele"
surname = "Mercolino"
student_id = "2046313"

#########################################

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To debug recursive functions you can turn off the recursive test setting
# DEBUG=True in the file grade.py
#
# DEBUG=True turns on also the STACK TRACE that allows you to know which
# line number in program.py generated the error.
################################################################################

# %%  ---- FUNC1 ----
''' func1: 2 points
Define a function func1(string_list) that takes as input a list of strings and
returns another list with only the strings that start with a capital letter.
The returned list has to be ordered by the number of letters in
increasing order.
'''


def func1(string_list: list[str]) -> list[str]:
    result = [word for word in string_list if word[0].isupper()]
    return sorted(result, key=len)


# %%  ---- FUNC2 ----
''' func2: 2 points
Define a function func2(pathname) that takes as input a string representing
the path of a text file. The file has only rows with two words separated by
whitespace. The function must return a dictionary where the keys are the first
elements of a row and the values are sets with the second elements of a row.
Every second element of a row appears in the set corresponding to the key
of the first element of the same row.

Example:
Content of animals.txt:
    cat     meaow
    dog     woof
    cat     purr
The call func2('animals.txt') returns {'cat':{'meaow', 'purr'}, 'dog':{'woof'}
'''


def func2(pathname):
    diz = {}
    with open(pathname) as f:
        for line in f:
            key, val = line.split()
            diz[key] = diz.get(key, set()) | {val}
    return diz


# %%  ---- FUNC3 ----
'''  func3: 2 points
Define a function func3(listA, listB, listC, pathname) that takes three lists
of numbers (integers or floats) and returns a new list where each element is
obtained considering the sum between the corresponding elements of the lists
listA and listB, sum multiplied for the corresponding element of listC.
The list built as above has to be written, one value for each row, in a text
file, with name pathname,
The function has to return the maximum value of the built list.
'''


def func3(listA, listB, listC, pathname):
    result = [(val1 + val2) * val3 for val1, val2, val3 in zip(listA, listB, listC)]
    text = "".join(str(val) + "\n" for val in result)
    with open(pathname, "wt") as f:
        f.write(text)
    return max(result)


# %%  ---- FUNC4 ----
""" func4: 6 points

Define the function func4(triangles) that takes as input a list of
triples of positive numbers and eliminates from the list all triples
that cannot be the sides of a right triangle. Each number in the
triple can be either cathetus or hypotenuse, and there is no
predetermined order.  The function must return the number of triples
deleted from the triangles list. The triangles list must be modified
in-place.  To evaluate whether a triangle is right-angled one can use
the Pythagorean theorem: the sum of the squares constructed on the
catheti must equal the square constructed on the hypotenuse.  For
comparisons, use the round(x,3) rounding function.

Example: if triangles = [(3, 4, 5), (12, 36.05551, 34),
                         (1,1,3), (8,8,8), (2, 3, 4)],
         the function func4(triangles) return the value 3 and modifies the list
         so that
         triangles = [(3, 4, 5), (12, 36.05551, 34)].

In fact, considering the expected result triangles = [(3, 4, 5), (12, 36.05551, 34)]
it holds the following:

| triplet            | check is True                                  |
| (3, 4, 5)          | round( 3² + 4² ), 3) == round( 5² ,3)          |
| (12, 36.05551, 34) | round( 12² + 34² ), 3) == round( 36.05551² ,3) |

NOTE: Break down the problem in small sub problems. Write small functions
for each sub problem. Compose everything together.

"""


def is_right(c1: int, c2: int, ip: int):
    return round((c1 ** 2 + c2 ** 2), 3) == round(ip ** 2, 3)


def func4(triangles: list[tuple[int, int, int]]):
    count = 0
    for tr in triangles.copy():
        triangle = sorted(tr)
        if not is_right(*triangle):
            triangles.remove(tr)
            count += 1
    return count


# %%  ---- FUNC5 ----
""" func5: 6 points
Define a function func5(img, filename) that returns a copy of the image img
flipped with respect to the vertical axis and saves the image in the file
with path as the filename string taken in input. The function returns the
color of the pixel in position (0,0) of the new image.
"""


def func5(img, filename):
    new_img = [[] for _ in img]
    for i, row in enumerate(img):
        for pixel in row:
            new_img[i].insert(0, pixel)
    images.save(new_img, filename)
    return new_img[0][0]


# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex1: 6 points

Define the recursive function ex1 that takes as input a string
'directory' and a string 'namefile'. The function must search recursively
within the directory given by directory and in all subdirectories for
all files with name equal to namefile.  Such files are to be
interpreted as text files. Each text file contains only positive
numeric strings. Files with the same namefile always have the same
number of numeric strings.  The function must return a list of
integers obtained by summing the numeric strings of the files found,
position by position.

Example: if two files with the SAME namefile are found and those
files contain the sequences "11 23 90" and "11 77 0," the function ex3
returns the list [22, 100, 90].

We suggest using the functions os.listdir, os.path.isfile and
os.path.isdir and NOT to use the os.join function in Windows (use
concatenation between strings with the '/' character).

It is forbidden to use the os.walk function.

NOTE: Break down the problem in small sub problems. Write small
functions for each sub problem. Compose everything together.
"""


def rec_1(directory, namefile, lst):
    dir_content = os.listdir(directory)
    if not dir_content:
        return
    filenames, sub_dirs = [f for f in dir_content if os.path.isfile(f"{directory}/{f}")], \
        [f for f in dir_content if os.path.isdir(f"{directory}/{f}")]
    for filename in filenames:
        if filename == namefile:
            with open(f'{directory}/{filename}') as f:
                lst.append([int(num) for n in f.readlines() for num in n.split()])
    for sub_dir in sub_dirs:
        rec_1(f'{directory}/{sub_dir}', namefile, lst)


def ex1(directory, namefile):
    lst = []
    rec_1(directory, namefile, lst)
    print(*lst, sep="\n")
    return [sum(vals) for vals in zip(*lst)]


# %% Ex2
"""
Ex2: 3+3 points
Define a recursive function (or one that uses recursive functions)
ex2(strings, n) that takes a set 'strings' and an integer 'n' and
recursively generates all possible strings that can be constructed by
concatenating n strings of the set strings. The function must return
all strings constructed. The function can return either a set with all
strings constructed (3 points), or a sorted list (6 points).  The list
is ordered considering the descending order of the length of the
strings and, in case of parity, considering the alphabetical order.

Example: if strings={'a','b','c','de'}, the function ex2(strings, 2)
returns the set {'ab','ac','ade','ba','ca','dea','bc','bde','cb','deb','cde','dec'} (6 points)
or the list ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'] (9 points)
"""


def rec_2(strings: set[str], n, result: list, partial):
    if n == 0:
        result.append(partial)
    for string in strings:
        rec_2(strings - {string}, n - 1, result, partial + string)


def ex2(strings, n):
    result = []
    rec_2(strings, n, result, partial='')
    return sorted(result, key=lambda word: (-len(word), word))


###################################################################################
if __name__ == '__main__':
    # Place your tests here
    strings = {'a', 'b', 'c', 'de'}
    n = 2
    res = ex2(strings, n)
    print(res)
