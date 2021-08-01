# EM算法(Expectation-Maximum)

## 原理篇

* **本质**：**概率模型**，去估计一个密度函数，**最大化对数似然函数**去估计参数。**无法直接用极大化对数似然函数**得到模型分布的参数，用**启发式跌代法**，**用于求解含有隐变量**的最大似然估计、最大后延概率估计问题。

  > 1. 隐变量：对概率模型有一定的影响，但无法观测；
  >
  > ​       观测数据X+隐变量 = 完全数据
  >
  > 2. 无法用[极大似然](https://blog.csdn.net/zengxiantao1994/article/details/72787849)的两种情况：数据缺失、含有未知隐变量

* **作用**：经常存在数据缺失或者不可用的的问题，这时候直接处理数据比较困难，而**数据添加**办法有很多种，常用的有神经网络拟合、添补法、卡尔曼滤波法等等，但是EM算法之所以能迅速普及主要源于它**算法简单，稳定上升**的步骤能非常可靠地找到“最优的收敛值”。

* **思想**：我们可以发现我们的算法里已知的是**观察数据**，未知的是隐含数据和模型参数，**在E步**，我们所做的事情是固定模型参数的值，优化隐含数据的分布，而**在M步**，我们所做的事情是固定隐含数据分布，优化模型参数的值。

**主要步骤：**

已知：概率分布、随机抽取的样本；

未知：分类、模型参数

* E-step：**猜想隐含数据**，更新隐含数据和模型参数

* M-step：**基于观察数据和猜测的隐含数据求极大对数似然**，求解模型K

* E-step：基于前面得到的模型K，继续猜测隐含数据，继续极大化对数似然

* M-step：求模型参数

* 直至模型分布无明显变化，算法收敛

  > EM算法步骤如下：
  >
  > 输入：观测变量数据X，隐变量Z，联合分布p(X,Z|Θ)
  >
  > 输出：模型参数Θ
  >
  > (1) 选择初始参数Θ0
  >
  > (2)E步：记Θi为第i次迭代参数Θ的估计值，在第i+1次迭代的E步，计算*Q*(Θ,Θ*g*);
  >
  > (3)M步：确定第i+1次迭代的参数的估计值Θ(*i*+1),即为：
  > $$
  > Θ 
  > (i+1)
  >  =argmax 
  > Θ
  > ​	
  >   Q(Θ,Θ 
  > (g)
  >  )
  > $$
  > (4)重复(2)和(3)步，直至收敛

## 预备知识--Jensen不等式

[未学](https://blog.csdn.net/baidu_38172402/article/details/89090383)

https://www.cnblogs.com/datasnail/p/9545385.html

## 应用篇1--GMM

EM在GMM中的应用

![高斯分布分析](E:\360MoveData\Users\lenovo\Desktop\截图未命名.jpg)

> 图中可知：
>
> 1. 单个高斯拟合效果差，均值应该分布在数据密集处
>
> 2. 混合高斯模型中的**隐变量**，同时，隐变量在概率模型中不能改变边缘分布，即：
>    $$
>    p(x_i)=\int_{z_i}p(x_i|z_i)*p(z_i)dz_i = \alpha_z =  \sum_{z_i=1}^k\alpha_{z_i}N(x_i|\mu_z,\Sigma_z)
>    $$
>    每个数据都有一个隐变量，告诉你在哪个高斯模型中(由两个高斯扩展到n个高斯)
>    $$
>    P(z_i = z_1|x_i,\Theta^{g}) = \frac{a}{a+b}
>    $$
>
> 3. 
>
> $$
> P(x) = \sum_{l=1}^{k}\alpha_l*N(X|\mu_l,\Sigma_l)
> \quad\quad\quad \sum^k_{l=1}\alpha_l = 1
> $$
>
> $$
> Θ=\{α_1	,…,α_k,μ_1,…,μ_k,Σ_1,…,Σ_{k-1}\}
> $$
>
> 4. 目标函数为：
>    $$
>    Θ_{MLE}=argmax_{Θ}*L(Θ∣X)
>    =argmax_Θ(\sum_{l=1}^nlog*\sum_{l=1}^kα_lN(X∣μ_l,Σ_l))
>    $$
>    该式子包含和（或积分）的对数，不能像单个高斯模型那样直接求导，再令导数为0来求解。这时我们需要**利用 EM 算法通过迭代逐步近似极大化L(Θ∣*X*)来求解**。

### EM算法在GMM中的应用：

$$
Θ^{(g+1)}=argmax_Θ∫_Zln(P(X,Z∣Θ))P(Z∣X,Θ^{(g)})dz
$$

1. #### E-step（期望步）

   $$
   p(X|\Theta) = \sum^k_{l=1}\alpha_lN(X|\mu_l,\Sigma_l) = \prod_{i=1}^n\sum_{l=1}^k\alpha_lN(x_i|\mu_l,\Sigma_l).............①
   $$

   由①得②：
   $$
   P(X,Z∣Θ)= ∏_{i=1}^np(x_i,z_i|Θ)= ∏^n_{i=1}p(x_i|z_i,Θ)p(z_i∣Θ)=\\ ∏^n_{i=1} α_{z_i}N(μ_{z_i},Σ_{z_i})......②
   $$
   由贝叶斯得③：
   $$
   P(z|X,\Theta) = \prod_{i=1}^np(z_i|x_i,\Theta) = \prod^x_{i=1}\frac{\alpha_{z_i}N(\mu_{z_i},\Sigma{z_i})}{\sum^k_{l=1}\alpha_lN(\mu_l,\Sigma_l)}..............③
   $$
   结合②③得④：
   $$
   Q(\Theta,\Theta^{(g)}) = \int_Zln(p(X,Z|\Theta))P(Z|X,\Theta^{(g)}dz = \\\int_{z1}...\int{zk}(\sum_{i=1}^n[ln\alpha_{z_i}+lnN(\mu_z{z_i},\Sigma_{z_i}])*\prod_{i=1}^np(z_{z_i}|x_i,\Theta^{(g)})dz_1...dz_k
   $$
   令：
   $$
   f(z_i)= ln\alpha_{z_i} + lnN(\mu_{z_i},\Sigma_{z_i})
   $$

   $$
   p(z_1...z_k) = \prod^n_{i=1}p(z_i|x_i,\Theta^{(g)})
   $$

   ④式可得⑤：
   $$
   Q(\Theta,\Theta^{(g)} = \int_{z_1}...\int(\sum^n_{i=1}f(z_i))*p(z_1,...,z_k)dz_1...dz_k   ........⑤
   $$
   ⑤的**第一项化简**：（不懂）
   $$
   \int_{z_1}...(f(z_1))*p(z_i,...,z_k)dz_1,...,dz_k = \\ \int_{z_1}\int_{z2}...\int_{z_k}*p(z_1,...,z_k)dz_1...dz_k= \\
   \int_{z_1}f(z_1)*p(z_1)dz_1
   $$
   综合得到⑥：
   $$
   Q(\Theta,\Theta^{(g)} = \sum_{i=1}^n\int_{z_i}f(z_i)*p(z_i)dz_i = \\\sum_{i=1}^n\int_{z_i}(ln\alpha_{z_i} + lnN(x_i|\mu_{z_i},\Sigma_{z_i}))*p(z_i|x_i,\Theta^{(g)}dz_i
   =\\
   \sum_{l=1}^k\sum_{i=1}^n(ln\alpha_l + lnN(x_i|\mu_l,\Sigma_l)*p(l|x_i,\Theta^{(g)}))
   $$

2. #### M-step（极大步）

   $$
   Q(\Theta,\Theta^{(g)} = \sum_{i=1}^n\int_{z_i}f(z_i)*p(z_i)dz_i = \\\sum_{i=1}^n\int_{z_i}(ln\alpha_{z_i} + lnN(x_i|\mu_{z_i},\Sigma_{z_i}))*p(z_i|x_i,\Theta^{(g)}dz_i
   =\\
   \sum_{l=1}^k\sum_{i=1}^n(ln\alpha_l + lnN(x_i|\mu_l,\Sigma_l)*p(l|x_i,\Theta^{(g)})) = \\
   \sum_{l=1}^k\sum_{i=1}^nln\alpha_l*p(l|x_i,\Theta^{(g)}) + \sum_{l=1}^k\sum_{i=1}^nln[N(x_i|\mu_l,\Sigma_l)]*p(l|x_i,\Theta^{(g)})
   $$

   第一项只含参数 α，第二项只含参数 μ,Σ，因此我们可以独立地进行最大化两项。
   (1) 最大化μ,Σ
   $$
   \frac{∂\sum^k_{l=1}\sum_{i=1}^nln[N(x_i|\mu_l,\Sigma_l)]*p(l|x_i,\Sigma^{(g)}}{∂\mu_1,...,∂\mu_k,∂\Sigma_1,...,∂\Sigma_k} = [0,0,...,0]
   $$
   化简得：
   $$
   \mu_l = \frac{\sum_{i=1}^nx_i*p(l|x_i,\Theta)}{\sum_{i=1}^n*p(l|x_i,\Theta)}
   $$

   $$
   \Sigma_l = \frac{\sum_{i=1}^n(x_i - \mu_l)(x_i -\mu_l)^Tp(l|x_i,\Theta)}{\sum_{i=1}^np(l|x_i,\Theta)}
   $$

   (2) **最大化*****α\***
   $$
   \frac{∂\sum_{l=1}^k\sim_{i=1}^nln\alpha_l*p(l|x_i,\Theta^{(g)}}{∂\alpha_1,...,∂\alpha_k} = [0,...,0]  \quad\quad\quad\quad st.\sum_{l=1}^k\alpha_l = 1
   $$
   用朗格朗日乘子法求解：
   $$
   L(\alpha_1,...,\alpha_k,\lambda) = \sum_{l=1}^kln(\alpha_l)(\sum_{i=1}^np(l|x_i,\Theta^{(g)}) - \lambda(\sum_{l=1}^k\alpha_l -1)
   $$
   求导得：
   $$
   \alpha_l = \frac{1}{N}\sum_{i=1}^nP(l|x_i,\Theta^{(g)})
   $$

   > *α*1 就是把所有样本点的加起来再除以样本总数N，即求所有样本点的 :
   > $$
   > P(z_i = z_1|x_i,\Theta^{g}) = \frac{a}{a+b}
   > $$
   > 如应用篇的图



## EM的收敛性





[参考1：知乎关于EM](https://zhuanlan.zhihu.com/p/40991784)

[参考2：GMM应用](https://blog.csdn.net/kevinoop/article/details/80522477)

[参考3：EM九个境界](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652010007&idx=4&sn=8abd041d3b1c5918ed7c4f9a981284e3&chksm=f12102e6c6568bf03fed785ee9369b6b53ad8463e5791ac24afb0940e54c663e3b1cc94d1f0a&mpshare=1&scene=1&srcid=0711kdWoQgkgvJFZ9HixG9vJ&sharer_sharetime=1594424401448&sharer_shareid=1673af32070db02a9dff0bdc6977c1da&key=f9077bed3f45e74f77ec6fa6db46cd0277b6cde58263cfb16728848940fb6abb64162c19b4909dec8e1a23d866333ea02e5abbf1125f298f3b3221710d81c8ab33c8ee785830d222b196ca877fb40217&ascene=1&uin=ODQwMDQ0MjE3&devicetype=Windows+7+x64&version=62090529&lang=zh_CN&exportkey=AQ3v55YcLLDQA92wNyj1%2BNQ%3D&pass_ticket=7KZ%2FnBWle8ETVyJ7%2BkFTfuy8EAVqwM%2FeShXuX33hUvd84ob%2F0KYitWRxBKe36rDL)