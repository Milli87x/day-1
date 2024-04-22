'''day 1 exercise {read all the way to day eight tho :-) } 
Check the python version you are using
Open the python interactive shell and do the following operations. The operands are 3 and 4.
 addition(+)
 subtraction(-)
 multiplication(*)
 modulus(%)
 division(/)
 exponential(**)
 floor division operator(//)
 Write strings on the python interactive shell. The strings are the following:
 Your name
 Your family name
 Your country
 I am enjoying 30 days of python
 Check the data types of the following data:
 10
 9.8
 3.14
 4 - 4j
 
 Your name
 Your family name
 Your country'''

# 1 to check python version we need to open bash and type python --version
# 2 to open pyt interactve shell we need to open a terminal amd type python or python3
#   this allows us to run any mathematical operation
#we dont really need to do this bc pthon does this too, Example
print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)
# to check data types we can use print(type())
name="milliyon"
family_name="gebrehiowt"
country="Ethiopia"
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(name))
print(type(family_name))
print(type(country))

# number 2 isnt something i can show here
# number 3 
""" 1 Write an example for different Python data types such as 
Number(Integer, Float, Complex),  
String, 
Boolean, 
List, 
Tuple,
Set and Dictionary.

2  Find an Euclidian distance between (2, 3) and (10, 8) """


integer=10
float=3.900000
complex= 8 + 0j
string='wassup wassuuuuuuuuuuup'
list=['food', 10, 20,'hello']
tuple=('monday',90, 'tueday')
set={1,2,3,4,5,6,7}
dictonaries={'name':'gareth_bale',
             'age':30,
             'country':'wales',
             'hobbies':'golf'}

print(type(integer))
print(type(float))
print(type(complex))
print(type(string))
print(type(list))
print(type(tuple))
print(type(set))
print(type(dictonaries))

#2
#Import the math library .
import math
#use the numbers as coordinates
x1=2 
y1=3
x2=10 
y2=8
'''eculidean distance is calculated as 
  squared root
  **2=squared or the power of 2 
  '''
distance=math.sqrt((x2-x1)** 2 + (y2-y1)** 2)
print("The Euclidean is:", distance)
