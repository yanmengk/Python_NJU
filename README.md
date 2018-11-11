# 用Python玩转大数据
## 1、走近Python
Python是**胶水语言**（很容易和其他程序语言连接，集成封装），是**高级脚本语言**（比其他脚本语言只能处理简单任务强大），是**面向对象语言**（完全支持继承、重载、派生、多继承）。
Python是**动态强类型语言**。所谓的动态是指Python中的变量可以指向不同类型的对象，无需事先声明。强类型可以这样理解，在 Python 中 1 + 'A'是不允许的，两者类型必须一致，而在 C 语言中这个表达式 是将 1 和字符 A 的 ASCII 值 65 相加，结果是 66，因此 Python 是强类型。
Python中的**eval()函数**：将字符串str当成有效的表达式来求值并返回计算结果。
### Python中的续行
续行符：“\”
无需续行符可直接换行的两种情况：
- 小括号、中括号、花括号的内部可以多行书写
- 三引号包括下的字符串也可以跨行书写

Python可以一行多语句书写，此时用**;**隔开，如下
```python
x = 'Today' ; y = 'is' ; z = 'Thursday' ; print(x, y, z)
```
Python中通过以下语句可以得到关键字：
```python
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

```
Python支持链式赋值：
> PI = pi = 3.14159

Python支持多重赋值：
> PI, r=3.14159, 3 等同于(PI, r) = (3.14159, 3)
### Python的复数型
Python的复数型的虚数部分必须有j
求虚部、实部、共轭如下：
```python
x = 2.4+5.6j
x.imag
x.real
x.conjugate()
```
### Python中比较运算
* 数值的比较：按值的大小
* 字符串的比较：**按ASCII码值的大小**
### Python中的变量管理
每个对象被创建时都会获得一个身份 id，可用 id()函数查看，同时会伴随一个引用计数器。
id() 函数用于获取对象的内存地址。如果两个变量a,b通过id()函数获取的内存地址相同，那么a is b返回True,否则返回False。
在 Python 中存在特殊的地方，**小整数（并无确切范围）和字符串**是*不可变*的，Python 会采用高效的方式去存储

### Python中的函数
Python中的内建函数：
```python
dir(__builtins__)
['ArithmeticError', ...... , '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

```
数值型内建函数：
```python
abs(): 求绝对值

bool(): 求布尔值

bin(x): 求x对应的二进制
>>> bin(9)

'0b1001'


oct(x):求x对应的八进制
>>> oct(9)

'0o11'


hex(x): 求x对应的十六进制
>>> hex(17)

'0x11'


round(x): 对x四舍五入

int(x): 对x截断取整

float(x): 将x变为float类型

complex(num):将num变为complex复数型

divmod(a,b): 求a//b和a%b的值

pow(a,b): 求a**b(a的b次方)

ord(): 求对应的ASCII的值
>>> ord('A')

65


chr():求该数值在ASCII表中对应的符号
>>> chr(89)

'Y'

```
可能用到的非内建函数：
```python
import math
math.floor(x) #向下取整
math.ceil(x) #向上取整

math.degrees() #将弧度转为角度
math.radians() #将角度转为弧度
>>> math.degrees(3.14)

179.9087476710785

>>> math.radians(180)

3.141592653589793


```



## 2、Python面面观
### 列表解析式与生成器表达式
```python
>>> [i+1 for i in range(10) if i%2==0]

[1, 3, 5, 7, 9]

>>> (i+1 for i in range(10) if i%2==0)

<generator object <genexpr> at 0x10bbd1938>

```
生成器表达式与列表解析式类似，不过采用圆括号标识，一般用在数据量比较大时使用。
### 循环中的else语句
循环中的else：
- 如果循环代码从break处终止，跳出循环，则不执行循环后边的else语句
- 正常结束循环，则执行else中代码
### Python中的OS模块函数
```python
>>> import os

>>> os.getcwd()

'/Users/yanmk/学习/技术学习/Python/Python_NJU'

>>> os.chdir('/Users/yanmk/学习')

>>> os.getcwd()

'/Users/yanmk/学习'

>>> os.rename(current_file_name, new_file_name)



>>> os.remove(file_name)



>>> os.mkdir(newdir)



>>> os.rmdir(dirname) #此目录为空时，否则抛出OSError

```
### Python中random模块中的常用函数
```python
>>> import random
>>> random.choice(['C++', 'Java', 'Python']) #随机从列表中选一个
>>> random.randint(1, 100) #[1,100]范围内随机选一个
>>> random.randrange(0, 10, 2) #[start,step=2,end)范围内选一个
>>> random.random()  #[0,1)范围随机数
>>> random.uniform(5, 10)
>>> random.sample(range(100), 10) #在0-99范围内随机采样10个数字组成列表
>>> random.shuffle(list) #随机打乱列表
```
### Python中datetime模块中的常用函数
```python3
>>> import datetime

>>> from datetime import date

>>> date.today()

datetime.date(2018, 11, 7)

>>> from datetime import time

>>> tm=time(23, 20, 35)

>>> print(tm)

23:20:35

>>> type(tm)

<class 'datetime.time'>

>>> from datetime import datetime

>>> dt=datetime.now()

>>> print(dt)

2018-11-07 20:33:10.454317

>>> print(dt.strftime('%a, %b %d %Y %H:%M'))

Wed, Nov 07 2018 20:33

>>> dt = datetime(2018, 2, 3, 23, 29)

>>> print(dt)

2018-02-03 23:29:00

>>> ts=dt.timestamp()

>>> print(ts)

1517671740.0

>>> print(datetime.fromtimestamp(ts))

2018-02-03 23:29:00

```
更多datetime模块相关的信息，参见(http://www.runoob.com/python3/python3-date-time.html)
## 3、数据的获取与表示
### Python中的format函数格式化字符串
```python
>>> print('There are %d punctuation marks. ' % (2))

There are 2 punctuation marks. 

>>> print('There are {0:d} punctuation marks. '.format(2))

There are 2 punctuation marks. 

```
以上两种方式都可以格式化字符串，但是更推荐使用第二种format形式，更多format信息参见(http://www.runoob.com/python/att-string-format.html)

### Python中文件的打开、关闭、读写操作
> file_obj = open(filename, mode='r', buffering=-1, …)

- mode为可选参数，默认值为r
- buffering也为可选参数，默认值为-1，使用系统默认的缓冲区大小（0代表不缓冲，1 或大于1的值表示缓冲一行或指定缓冲区大小）
- mode为w时，会清空原内容再写
- 推荐使用with open(file_name, 'w') as f，可以进行上下文管理（结束后自动关闭文件）、异常处理。

> file_obj.seek(offset , whence=0)

- 在文件中移动文件指针，从 whence（0表示文件头部，1表示当前位置，2表示文件尾部）偏移offset个字节
- whence参数可选，默认值为0
## 3、强大的Python数据结构和扩展库
### Python中的集合set相关的运算
![](https://github.com/yanmengk/Python_NJU/blob/master/resource/Figure_2.png)
Python的pandas库中的DataFrame数据结构：
- loc: 通过**行标签**索引行数据
- iloc:通过**行号**索引行数据
- ix:混合以上两种方式，官方已经不推荐使用

## 4、强大的数据结构和Python扩展库
## 5、Python基本数据统计
## 6、Python高级数据处理与可视化
上述章节主要讲述了Python中的数据结构：list、tuple、set、dict
Numpy库、Pandas库（Series和DataFrame）、Matplotlib库、Scipy库。
## 7、面向对象和图形用户界面
Python的GUI库：
- wxPython：具有优秀的跨平台能力
- PyQt：**优点**：提供了GPL与商业协议两种授权方式，可以免费地用于自由软件的开发；跨平台；文档比其他GUI库丰富；与Qt、C++开发经验互通；可使用大多数为Qt开发的组件；**更适合专业人士**；**缺点**：要注意避免内存泄露；运行时庞大。
- Tkinter：**优点**：Python事实上的标准GUI，创建的GUI简单，学起来和用起来也简单；**缺点**：性能不太好，执行速度慢。
- PyGTK：**优点**：底层的GTK+提供了各式 的可视元素和功能；能开发在GNOME桌面系 统运行的功能完整的软件；**缺点**：在Windows平台表现不太好
