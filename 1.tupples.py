Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1=(1,2,3,4,5,6,7)
>>> tup2=(7,8,9,0,5,6)
>>> #tuples are created
>>> print(len(tup1))
7
>>> print(len(tup2))
6
>>> print(tup1+tup2)
(1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 0, 5, 6)
>>> len(tup1+tup2)
13
>>> max(tup1+tup2)
9
>>> min(tup1+tup2)
0
>>> def product( tup1+tup2 )
SyntaxError: invalid syntax
>>> tup3=tup1+tup2
>>> print(tup3)
(1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 0, 5, 6)

>>> tuple1=(1,2,3)
>>> def product(tuple1):
    prod = 1
    for x in tuple1:
        prod = prod * x
    return prod

>>> print(product(tuple1))
6



