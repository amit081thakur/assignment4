Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>#Q.1- Create a dictionary to store name and marks of 10 students by user input. 
>>> student ={'aakash': 57, 'aanchal': 67,'aashna': 47, 'abhinav': 45, 'ajeta': 63, 'aliya': 34, 'akshat': 23,'akshit': 88, 'amit': 31, 'ankit':99}
>>>	  
>>> print(student['aakash'])
57
>>>
>>>
>>>
>>>
>>> #Q.2-Sort the dictionary created in previous question according to marks.
>>>
>>> #sorting in ascending order.
>>> sort=sorted(student)
>>> print(student)
{'aakash': 57, 'aanchal': 67, 'aashna': 47, 'abhinav': 45, 'ajeta': 63, 'aliya': 34, 'akshat': 23, 'akshit': 88, 'amit': 31, 'ankit': 99}
>>> sort= sorted(student.items(),key=operator.itemgetter(1))
>>> print(sort)
[('akshat', 23), ('amit', 31), ('aliya', 34), ('abhinav', 45), ('aashna', 47), ('aakash', 57), ('ajeta', 63), ('aanchal', 67), ('akshit', 88), ('ankit', 99)]
>>>
>>> #sorting in descending order

>>> sort1= sorted(student.items(),key=operator.itemgetter(1),reverse=True)
>>> print(sort)
[('akshat', 23), ('amit', 31), ('aliya', 34), ('abhinav', 45), ('aashna', 47), ('aakash', 57), ('ajeta', 63), ('aanchal', 67), ('akshit', 88), ('ankit', 99)]
>>> print(sort1)
[('ankit', 99), ('akshit', 88), ('aanchal', 67), ('ajeta', 63), ('aakash', 57), ('aashna', 47), ('abhinav', 45), ('aliya', 34), ('amit', 31), ('akshat', 23)]
>>>
>>>
>>>
>>> #Q.3- Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary. 
>>>
>>>
>>> word = "MISSISSIPPI"
>>> word.count('M')
1
>>> word.count('I')
4
>>> word.count('S')
4
>>> word.count('P')
2
>>> alphabet= {'M':1,'I':4,'S':4,'P':2}
>>> print(alphabet['I'])
4
>>> 
