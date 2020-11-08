Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
CAT : แมว

========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
CAT : แมว
CAT : แมว

========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
dog : แมว
cat : แมว
>>> 
========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python39\lib\tkinter\__init__.py", line 1885, in __call__
    return self.func(*args)
  File "C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py", line 22, in Translate
    print( vocab +  ' : '+ meaning)
TypeError: can only concatenate str (not "Translated") to str

========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python39\lib\tkinter\__init__.py", line 1885, in __call__
    return self.func(*args)
  File "C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py", line 21, in Translate
    meaning = translator.translate(vocab, dest='th')
  File "C:\Python39\lib\site-packages\googletrans\client.py", line 182, in translate
    data = self._translate(text, dest, src, kwargs)
  File "C:\Python39\lib\site-packages\googletrans\client.py", line 78, in _translate
    token = self.token_acquirer.do(text)
  File "C:\Python39\lib\site-packages\googletrans\gtoken.py", line 194, in do
    self._update()
  File "C:\Python39\lib\site-packages\googletrans\gtoken.py", line 62, in _update
    code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
AttributeError: 'NoneType' object has no attribute 'group'

========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
dog : หมา
cat : แมว
thailand  : ประเทศไทย
python : หลาม
insine : ต่อ se
inside : ภายใน
inside Pua : ภายในปัว

========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
ข้างในปัว : ข้างในปัว
K̄ĥāng nı pạw
inside : ภายใน
P̣hāynı

========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
dog : หมา
H̄mā

========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
dog : หมา
H̄mā
dog : หมา
H̄mā
cat : แมว
Mæw

========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
cat : แมว
Mæw
>>> 
========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python39\lib\tkinter\__init__.py", line 1885, in __call__
    return self.func(*args)
  File "C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py", line 26, in Translate
    meaning = translator.translate(vocab, dest='th')
  File "C:\Python39\lib\site-packages\googletrans\client.py", line 182, in translate
    data = self._translate(text, dest, src, kwargs)
  File "C:\Python39\lib\site-packages\googletrans\client.py", line 78, in _translate
    token = self.token_acquirer.do(text)
  File "C:\Python39\lib\site-packages\googletrans\gtoken.py", line 194, in do
    self._update()
  File "C:\Python39\lib\site-packages\googletrans\gtoken.py", line 62, in _update
    code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
AttributeError: 'NoneType' object has no attribute 'group'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python39\lib\tkinter\__init__.py", line 1885, in __call__
    return self.func(*args)
  File "C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py", line 26, in Translate
    meaning = translator.translate(vocab, dest='th')
  File "C:\Python39\lib\site-packages\googletrans\client.py", line 182, in translate
    data = self._translate(text, dest, src, kwargs)
  File "C:\Python39\lib\site-packages\googletrans\client.py", line 78, in _translate
    token = self.token_acquirer.do(text)
  File "C:\Python39\lib\site-packages\googletrans\gtoken.py", line 194, in do
    self._update()
  File "C:\Python39\lib\site-packages\googletrans\gtoken.py", line 62, in _update
    code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python39\lib\tkinter\__init__.py", line 1885, in __call__
    return self.func(*args)
  File "C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py", line 26, in Translate
    meaning = translator.translate(vocab, dest='th')
  File "C:\Python39\lib\site-packages\googletrans\client.py", line 182, in translate
    data = self._translate(text, dest, src, kwargs)
  File "C:\Python39\lib\site-packages\googletrans\client.py", line 78, in _translate
    token = self.token_acquirer.do(text)
  File "C:\Python39\lib\site-packages\googletrans\gtoken.py", line 194, in do
    self._update()
  File "C:\Python39\lib\site-packages\googletrans\gtoken.py", line 62, in _update
    code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python39\lib\tkinter\__init__.py", line 1885, in __call__
    return self.func(*args)
  File "C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py", line 26, in Translate
    meaning = translator.translate(vocab, dest='th')
  File "C:\Python39\lib\site-packages\googletrans\client.py", line 182, in translate
    data = self._translate(text, dest, src, kwargs)
  File "C:\Python39\lib\site-packages\googletrans\client.py", line 78, in _translate
    token = self.token_acquirer.do(text)
  File "C:\Python39\lib\site-packages\googletrans\gtoken.py", line 194, in do
    self._update()
  File "C:\Python39\lib\site-packages\googletrans\gtoken.py", line 62, in _update
    code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
AttributeError: 'NoneType' object has no attribute 'group'

========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python39\lib\tkinter\__init__.py", line 1885, in __call__
    return self.func(*args)
  File "C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py", line 26, in Translate
    meaning = translator.translate(vocab, dest='th')
  File "C:\Python39\lib\site-packages\googletrans\client.py", line 182, in translate
    data = self._translate(text, dest, src, kwargs)
  File "C:\Python39\lib\site-packages\googletrans\client.py", line 78, in _translate
    token = self.token_acquirer.do(text)
  File "C:\Python39\lib\site-packages\googletrans\gtoken.py", line 194, in do
    self._update()
  File "C:\Python39\lib\site-packages\googletrans\gtoken.py", line 62, in _update
    code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
========== RESTART: C:/Users/Jibb/Desktop/Python/EP1/GUITranslator.py ==========
dog : หมา
H̄mā
inside : ภายใน
P̣hāynı
>>> 