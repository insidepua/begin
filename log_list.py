Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> garage = ( 'toyota' , ' honda' , 'izusu' )
>>> garage.append( ' suzuki ' )
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    garage.append( ' suzuki ' )
AttributeError: 'tuple' object has no attribute 'append'
>>> garage.append( 'suzuki' )
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    garage.append( 'suzuki' )
AttributeError: 'tuple' object has no attribute 'append'
>>> garage = [ 'toyota' , ' honda' , 'izusu' ]
>>> garage.append('suzuki')
>>> print(garage)
['toyota', ' honda', 'izusu', 'suzuki']
>>> print(garage[2])
izusu
>>> garage.remove('honda')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    garage.remove('honda')
ValueError: list.remove(x): x not in list
>>> garage.remove('honda')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    garage.remove('honda')
ValueError: list.remove(x): x not in list
>>> garage.remove( 'honda' )
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    garage.remove( 'honda' )
ValueError: list.remove(x): x not in list
>>> print(garage)
['toyota', ' honda', 'izusu', 'suzuki']
>>> garage.remove('honda')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    garage.remove('honda')
ValueError: list.remove(x): x not in list
>>> garage.remove(' honda ')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    garage.remove(' honda ')
ValueError: list.remove(x): x not in list
>>> garage.remove ('honda')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    garage.remove ('honda')
ValueError: list.remove(x): x not in list
>>> garage.remove ('honda')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    garage.remove ('honda')
ValueError: list.remove(x): x not in list
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> garage.remove ('honda')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    garage.remove ('honda')
ValueError: list.remove(x): x not in list
>>> 
>>> garage.remove (' honda')
>>> print (garage.remove)
<built-in method remove of list object at 0x000000A698E77E00>
>>> 