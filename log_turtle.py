Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Turtle()
>>> tao.shape('turtle')
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.lefe(90)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tao.lefe(90)
AttributeError: 'Turtle' object has no attribute 'lefe'
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)

	
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> for i in rang(5):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    for i in rang(5):
NameError: name 'rang' is not defined
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in (10,50,90):
	print(i)

	
10
50
90
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)
	print('No. ' , i)

	
No.  0
No.  1
No.  2
No.  3
>>> for i in range(8):
	tao.forward(50)
	tao.left(45)
	print('No. ' , i)

	
No.  0
No.  1
No.  2
No.  3
No.  4
No.  5
No.  6
No.  7
>>> tao.reset()
>>> for i in range(8):
	tao.forward(50)
	tao.left(45)
	print('No. ' , i)

	
No.  0
No.  1
No.  2
No.  3
No.  4
No.  5
No.  6
No.  7
>>> for i in range(8):
	tao.forward(100)
	tao.left(45)
	print('No. ' , i)

	
No.  0
No.  1
No.  2
No.  3
No.  4
No.  5
No.  6
No.  7
>>> for i in range(8):
	tao.forward(50)
	tao.right(45)
	print('No. ' , i)

	
No.  0
No.  1
No.  2
No.  3
No.  4
No.  5
No.  6
No.  7
>>> for i in range(8):
	tao.forward(100)
	tao.right(45)
	print('No. ' , i)

	
No.  0
No.  1
No.  2
No.  3
No.  4
No.  5
No.  6
No.  7
>>> tao.reset()
>>> for i in range(8):
	tao.forward(100)
	tao.left(45)
	print('No. ' , i)

	
No.  0
No.  1
No.  2
No.  3
No.  4
No.  5
No.  6
No.  7
>>> for i in range(4):
	 for j in range(8):
		 tao.forward(100)
		 tao.left(45)
	print('8 เหลี่ยมรูปที่' ,i)
	
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(4):
	 for j in range(8):
		 tao.forward(100)
		 tao.left(45)
	print('8 เหลี่ยมรูปที่' ,i)
	
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(10):
	 for j in range(8):
		 tao.forward(100)
		 tao.left(45)
	print('8 เหลี่ยมรูปที่' ,i)
	
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(10):
	 for j in range(8):
		 tao.forward(100)
		 tao.left(45)
	print('8 เหลี่ยมรูปที่' ,i)tao.reset()
	
SyntaxError: unindent does not match any outer indentation level
>>> tao.reset
<bound method RawTurtle.reset of <turtle.Turtle object at 0x0000003DC820DCA0>>
>>> tao.reset()
>>> def retangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

		
>>> retangle()
>>> for i in range(10):
	retangle()
	tao.left(36)

	
>>> 