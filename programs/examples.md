# 例题、习题记录

## 1、走近Python

#### exp-1: matplotlib绘图

```python
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0.,4.,0.1)
plt.plot(t,t,t,t+2,t,t**2)
```

用plot函数一次画三条线：
- 第一条 x1=t,y1=t
- 第二条 x2=t,y2=t+2
- 第三条 x3=t,y3=t**2

结果：

<img height="300" align="center" src="https://github.com/yanmengk/Python_NJU/blob/master/resource/Figure_1.png" alt="">

#### exp-2: 利用scipy.cluster聚类
```python
from pylab import * 
from scipy.cluster.vq import * 
list1 = [88.0,74.0,96.0,85.0]
list2 = [92.0,99.0,95.0,94.0]
list3 = [91.0,87.0,99.0,95.0]
list4 = [78.0,99.0,97.0,81.0]
list5 = [88.0,78.0,98.0,84.0]
list6 = [100.0,95.0,100.0,92.0]
data = vstack((list1,list2,list3,list4,list5,list6))
centroids,_ = kmeans(data,2)
result,_= vq(data,centroids)
print(result)
```
输出结果：
> [0 1 1 1 0 1]

### 2、Python面面观