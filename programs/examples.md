# 记录本课程中的例题、习题

## 1、走近Python

#### exp-1:matplotlib绘图

```
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0.,4.,0.1)
plt.plot(t,t,t,t+2,t,t**2)
```
用plot函数一次画三条线：
第一条 x1=t,y1=t
第二条 x2=t,y2=t+2
第三条 x3=t,y3=t**2

结果：

<img height="300" align="center" src="https://github.com/yanmengk/Python_NJU/blob/master/resource/Figure_1.png" alt="">
