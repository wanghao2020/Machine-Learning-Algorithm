# SVM 详解

标签（空格分隔）： 机器学习 支持向量机

---
　　支持向量机基本上是最好的有**监督学习算法**，因其英文名为Support Vector Machine，简称SVM。通俗来讲，它是一种二类分类模型，其基本模型定义为特征空间上的**间隔最大**的**线性分类器**，其学习策略便是间隔最大化，最终可转化为一个凸二次规划问题的求解。

## 目录
[TOC]

-----

### **一. 线性可分支持向量机与硬间隔最大化**

#### **1. 线性可分支持向量机**

　　给定一些数据点，它们分别属于两个不同的类，现在要找到一个线性分类器把这些数据分成两类。如果用**X**表示数据点，用**Y**表示类别（y可以取1或者-1，分别代表两个不同的类），一个线性分类器的学习目标便是要在n维的数据空间中利用**间隔最大化**找到一个超平面（hyper plane），这个超平面的方程可以表示为（ wT中的T代表转置）：
$$ W^T + B = 0 $$
对应的决策函数:
$$ f(x)=sign(w^T+B)$$   
如下图所示：
感知机：

![对比](http://img.blog.csdn.net/20141201123622095)

支持向量机

![线性分类](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131131479073.png)

>和感知机的分类方法很像，但是两者的区别和解决的个数区别？
－－多了约束条件和解的唯一性

#### **2. 间隔是什么？**
1> 函数间隔
$$ \gamma_{i}=y_{i}(w*x_{i}+b)$$
>表达了分类的正确性和确信度

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131131573905.png)
>取最小的间隔为衡量标准

函数间隔带来的问题？
>成倍地增加**W**和**b**的值，分类的平面没有改变，但是函数的间隔却变大了。

2> 几何间隔
对法向量的**W**加以约束即为:  **||W||=1**
$$ \gamma_{i}=y_{i}\lgroup{\frac{w}{\lVert {w} \rVert}*x_{i}+\frac{b}{\lVert {w} \rVert}}\rgroup$$

得到几何间隔的含义如下图所示：
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131131571364.png)
>A为某一个样本点，B为在分类面上的垂直投影点，W为垂直分类面的向量

通过几何间隔的最小化

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131132042274.png)

>---函数间隔和几何间隔的关系
相差**||w||**倍

#### **3. 向量机目标？**

　　对一个数据点进行分类，当超平面离数据点的“间隔”越大，分类的确信度（Confidence）也越大。所以，为了使得分类的确信度尽量高，需要让所选择的超平面能够最大化这个“间隔”值。这个间隔如下图所示
　　
![](http://img.blog.csdn.net/20140829135959290)

用数学的表达方法为：



$$max_{\gamma,w,b}\quad\gamma$$
$$s.t.\quad y^{(i)}\lgroup{\frac{w}{\lVert {w} \rVert}*x_{i}+\frac{b}{\lVert {w} \rVert}}\rgroup\ge\gamma\quad\quad i=1,...,m$$
$$||w||=1$$

不易求解，所以对上面的表达式进行简单的转化


![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131132079992.png)

再次转化
>将函数间隔定义为1，来求w的的值


![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131132112071.png)

>证明解的唯一性：见书P101,从存在性和唯一性进行证明

#### **4. 如何求解？**

**拉格朗日对偶性**(*附录C*)

不等式约束的极值问题求法：

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131234511451.png)

定义一般化的拉格朗日公式

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131234515322.png)

>ai,bi分别为拉格朗日算子

如何将上面的两个方程进行等价

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131234552417.png)

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235002969.png)

因此原始的问题可以换成：

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235029805.png)

如果直接求解，首先面对的是两个参数,然后再在w上求最小值。这个过程不容易做。

**从对偶的角度出发**

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235042016.png)

将问题转化为先求拉格朗日关于w的最小值，然后再求两个值的最大值

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235084651.png)

> 相对于原问题只是更换了min和max的顺序，而一般更换顺序的结果是
Max Min(X) <= MinMax(X)

**KKT条件**：假设f(x)和g(x)都是凸函数，h(x)是仿射的，并且存在w使得对于所有的i，![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235119338.png),在这种假设下，一定存在![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235128748.png)使得![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235129795.png)是原问题的解,![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235134679.png)是对偶问题的解.

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235189201.png)

**SVM的求解**
原始问题

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235229818.png)

将约束条件改写为：

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235232260.png)

从KKT条件得知只有函数间隔是1（离超平面最近的点）的线性约束式前面的系数![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235237560.png),也就是说这些约束式![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235236621.png),对应的点称为**支持向量**。对于其他的不在线上的点![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/20110313123524492.png),极值不会在他们所在的范围内取得，因此前面的系数![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235259870.png).

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235267786.png)

对运来的目标函数**构造拉格朗日函数**如下:

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235281633.png)

对偶问题为：

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235316385.png)

首先求解最小值：
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235339186.png)
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235346088.png)

得到结果：
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235346579.png)

代入后，化简过程如下：
![](http://pic002.cnblogs.com/images/2011/279228/2011051016205860.png)

最后得到:
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235354876.png)

由于最后一项是0，因此简化为
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235352302.png)

为了后面方便这里将**向量的内积**![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235368365.png)为![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235365268.png)

最后一步极大化
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235392986.png)
> 根据这个优化问题求出对应的a的值

由a的值求解出原始问题的解（书上有详细的证明）
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235468704.jpg)

根据平面的方程可以根据 w 的值推出 b 的值

从而得到决策函数:
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131235502419.png)
$$f(x) =sign(w^{T}*x+b)$$

> 从分类的决策函数可以看出，分类的结果只依赖于输入x和训练样本输入的内积。而取决定性作用的为支持向量。

----
### **二. 线性支持向量机与软间隔最大化**

当数据不是完全线性可分的时候，我们就需要对数据具有一定的容错性，即允许一定的数据不满足函数间隔大与1的约束条件。所以引入松弛变量

#### **1. 线性支持向量机**

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103182037075228.png)

　　可以看到一个离群点（可能是噪声）可以造成超平面的移动，间隔缩小，可见以前的模型对噪声非常敏感。再有甚者，如果离群点在另外一个类中，那么这时候就是线性不可分了。

#### **2. 修改线性支持**

>原因：更好的分类效果，支持线性不可分的情况。

上一节中的为硬间隔，这次修改的为软间隔

![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103182037085162.png)

> C>0,为惩罚参数，在调参中具体使用
C越大，对误分类的惩罚增加,减少误分类的个数
C越小，对误分类的惩罚减少，加大了间隔距离

**修改后的拉格朗日公式**也要修改如下：
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/20110318203710504.jpg)

先写出拉格朗日公式（如上），然后将其看作是变量 w 和 b 的函数，分别对其求偏导，得到 w 和 b 的表达式。然后代入公式中，求带入后公式的极大值。整个推导过程类似以前的模型:
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/20110318203713207.png)

>发现没有了参数e,多了a<=C的限制约束。

对比下前后KKT条件的变化
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103182037208924.png)

>根据此处可以看书b的求解方法变化，根据(16)式进行求解。

第一个式子表明在两条间隔线外的样本点前面的系数为0，离群样本点前面的系数为C，而支持向量（也就是在超平面两边的最大间隔线上）的样本点前面系数在(0,C)上。通过KKT条件可知，某些在最大间隔线上的样本点也不是支持向量，相反也可能是离群点。

#### **4. 求解方法**

根据上面求解可知道 w 仍然是原来的求解方法。
$$w^{*}=\sum_{i=1}^{N}a_{i}^{*}y_{i}x_{i}$$
求解b值，只有在
$$ 0<a_{j}^{*}<C$$
根据某个第J的实例，通过超平面的方程得到b值
$$b^{*} = y_{j}-\sum_{i=1}^{N}y_{i}(x_{i}.x_{j}) $$

----
### **三. 非线性支持向量机与核函数**

了解到了SVM处理线性可分的情况，而对于非线性的情况，SVM的处理方法是选择一个核函数 κ(⋅,⋅)，通过将数据映射到高维空间，来解决在原始空间中线性不可分的问题。

先看两个图片

![](http://img.blog.csdn.net/20140830002108254)

分类前，线性不可分：
![](http://img.blog.csdn.net/20141201135856804)

使用核函数,线性可分:
![](http://img.blog.csdn.net/20141201135911562)

#### **1. 核函数是什么？有什么用？**

假设x为输入空间，H为特征空间，则定义映射函数

$$ \phi(x):\chi\to H$$
使得对所有的$$x,z\in\chi$$函数都会满足的
$$K(x,z)=\phi(x).\phi(z)$$
>好处：
1. 在学习和预测中只需要定义核函数，而不用显示的定义映射函数。
2. 因为只涉及到实例与实例之间的内积，计算方便。
#### **2. 核函数如何在支持向量机中使用**
　　使用核函数后，线性的时候我们使用SVM学习出w和b，新来样本x的话，我们使用![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103182034414967.png)来判断,使用核函数以后![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103182034419045.png),然后我们并不需要找出![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103182034436721.png)

只需要将原来的判断函数
![](http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103182034435783.png)
避开了直接在高维空间中进行计算

$$\sum_{i=1}^{N}a_{i}y^{i}K(x,x^{i})+b $$即可


**常用的核函数**有：
- 多项式核，空间维度为![](http://img.blog.csdn.net/20141201140034491),m是原始空间的维度，d是多项式的维度
$$ K(x,z) = (x*z+1)^{p}$$
-  高斯核，将原始空间映射为无穷维空间
$$ K(x,z) = exp(-\frac{||x-z||^{2}}{2\sigma^{2}})$$

----
### **四. 序列最小最优化算法(SMO算法)**

　　分而治之，将原始的问题变成了求解析解，加速了求解过程。(详细见书)

#### **1. 只对两个变量优化，求二次规划的解析解**
　
　　首先选择两个变量，固定其他变量，可以由一个变量推出另一个变量，因此就转化成了一个实际的一元二次求解的情况，根据限定的范围，从而得到最优解，依次进行更新。
　　
#### **2. 优化变量的选择**

1. 第一个变量的选择，主要是在外层中选取违反KKT条件最严重的样本点。顺序是首先遍历边界上的支持向量点，然后再遍历整个训练集，判断时候满足KKT条件。
2. 再第二个变量的选择标准是希望能变量有足够大的变化。

----
### **五. 扩展及致谢**

- [x] 常见的手写数字分类，文本分类等分类问题
- [x] 由二分类问题扩展为多分类的问题
- [x] 常用的核技巧
- [x] 常用的SVM包，LIBSVM，SVM Light等


----


![致谢](http://pic.wenwo.com/fimg/55706112187_516.jpg)
　　
　　
　　
　　
　　


  
