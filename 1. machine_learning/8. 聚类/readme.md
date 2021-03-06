## 1. k-means(k均值)算法

### 1.1 算法过程

K-均值是最普及的聚类算法，算法接受一个未标记的数据集，然后将数据聚类成不同的组。

K-均值是一个迭代算法，假设我们想要将数据聚类成 n 个组，其方法为:

- 首先选择𝐾个随机的点，称为聚类中心（cluster centroids）；
- 对于数据集中的每一个数据，按照距离𝐾个中心点的距离，将其与距离最近的中心点关联起来，与同一个中心点关联的所有点聚成一类。
- 计算每一个组的平均值，将该组所关联的中心点移动到平均值的位置。
- 重复步骤，直至中心点不再变化。

### 1.2 损失函数

- K-均值最小化问题，是要最小化所有的数据点与其所关联的聚类中心点之间的距离之和，因此 K-均值的代价函数（又称畸变函数 Distortion function）为：

$J(c^{(1)},c^{(2)},...,c^{(m)},u_1,...,u_k) = \frac 1 m \sum_{i=1}^m||X^{(1)}-u_{c^{(i)}}||^2$，其中$u_{c^{(i)}}$代表与$x^{(i)}$最近的聚类中心点，优化的目标是找出代价最小的$c^{(1)},c^{(2)},...,c^{(m)},u_1,...,u_k$

- K值的选择可以根据“肘部法则”，选择K值和损失函数联合函数的拐点；人工选择

### 1.3 KNN与K-means区别？

K最近邻(k-Nearest Neighbor，KNN)分类算法，是一个理论上比较成熟的方法，也是最简单的机器学习算法之一。

| KNN                                                          | K-Means                                                      |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1.KNN是分类算法<br/>2.属于监督学习<br/>3.训练数据集是带label的数据 | 1.K-Means是聚类算法<br/>2.属于非监督学习<br/>3.训练数据集是无label的数据，是杂乱无章的，经过聚类后变得有序，先无序，后有序。 |
| 没有明显的前期训练过程，属于memory based learning            | 有明显的前期训练过程                                         |
| K的含义：一个样本x，对它进行分类，就从训练数据集中，在x附近找离它最近的K个数据点，这K个数据点，类别c占的个数最多，就把x的label设为c。 | K的含义：K是人工固定好的数字，假设数据集合可以分为K个蔟，那么就利用训练数据来训练出这K个分类。 |

**相似点**

都包含这样的过程，给定一个点，在数据集中找离它最近的点。即二者都用到了NN(Nears Neighbor)算法思想。

### 1.4 K-Means优缺点及改进

k-means：在大数据的条件下，会耗费大量的时间和内存。 优化k-means的建议： 

1. 减少聚类的数目K。因为，每个样本都要跟类中心计算距离。 

2. 减少样本的特征维度。比如说，通过PCA等进行降维。 

3. 考察其他的聚类算法，通过选取toy数据，去测试不同聚类算法的性能。 

4. hadoop集群，K-means算法是很容易进行并行计算的。 

5. 算法可能找到局部最优的聚类，而不是全局最优的聚类。使用改进的二分k-means算法。

   二分k-means算法：首先将整个数据集看成一个簇，然后进行一次k-means（k=2）算法将该簇一分为二，并计算每个簇的误差平方和，选择平方和最大的簇迭代上述过程再次一分为二，直至簇数达到用户指定的k为止，此时可以达到的全局最优。

## 2. 高斯混合模型(GMM)

### 2.1 GMM的思想

高斯混合模型（Gaussian Mixed Model，GMM）也是一种常见的聚类算法，与K均值算法类似，同样使用了EM算法进行迭代计算。高斯混合模型假设每个簇的数据都是符合高斯分布（又叫正态分布）的，当前**数据呈现的分布就是各个簇的高斯分布叠加在一起的结果。**

第一张图是一个数据分布的样例，如果只用一个高斯分布来拟合图中的数据，图 中所示的椭圆即为高斯分布的二倍标准差所对应的椭圆。直观来说，图中的数据 明显分为两簇，因此只用一个高斯分布来拟和是不太合理的，需要推广到用多个 高斯分布的叠加来对数据进行拟合。第二张图是用两个高斯分布的叠加来拟合得到的结果。**这就引出了高斯混合模型，即用多个高斯分布函数的线形组合来对数据分布进行拟合。**理论上，高斯混合模型可以拟合出任意类型的分布。

![00630Defly1g5b8mu9mjmj30iu0apjuh](readme.assets/00630Defly1g5b8mu9mjmj30iu0apjuh.jpg)

![00630Defly1g5b8ms101aj30id0aswhh](readme.assets/00630Defly1g5b8ms101aj30id0aswhh.jpg)

- 高斯混合模型的核心思想是**，假设数据可以看作从多个高斯分布中生成出来的**。在该假设下，每个单独的分模型都是标准高斯模型，其均值 $u_i$ 和方差 $\sum_i$ 是待估计的参数。此外，每个分模型都还有一个参数 $\pi_i$，可以理解为权重或生成数据的概 率。高斯混合模型的公式为：$p(x)=\sum_{i=1}^{k}\pi_iN(x|u_i,\sum_i)$

- 通常我们并不能直接得到高斯混合模型的参数，而是观察到了一系列 数据点，给出一个类别的数量K后，希望求得最佳的K个高斯分模型。因此，高斯 混合模型的计算，便成了最佳的均值μ，方差Σ、权重π的寻找，这类问题通常通过 最大似然估计来求解。遗憾的是，**此问题中直接使用最大似然估计，得到的是一 个复杂的非凸函数**，目标函数是和的对数，难以展开和对其求偏导。
  - **在这种情况下，可以用EM算法。 **EM算法是在最大化目标函数时，先固定一个变量使整体函数变为凸优化函数，求导得到最值，然后利用最优参数更新被固定的变量，进入下一个循环。具体到高 斯混合模型的求解，EM算法的迭代过程如下。
    - 首先，初始随机选择各参数的值。然后，重复下述两步，直到收敛。 
      - E步骤。根据当前的参数，计算每个点由某个分模型生成的概率。 
      - M步骤。使用E步骤估计出的概率，来改进每个分模型的均值，方差和权重。

> 高斯混合模型是一个生成式模型。可以这样理解数据的生成过程，假设一个最简单的情况，即只有两个一维标准高斯分布的分模型*N*(0,1)和*N*(5,1)，其权重分别为0.7和0.3。那么，在生成第一个数据点时，先按照权重的比例，随机选择一个分布，比如选择第一个高斯分布，接着从*N*(0,1)中生成一个点，如−0.5，便是第一个数据点。在生成第二个数据点时，随机选择到第二个高斯分布*N*(5,1)，生成了第二个点4.7。如此循环执行，便生成出了所有的数据点。 

也就是说，我们并不知道最佳的K个高斯分布的各自3个参数，也不知道每个数据点究竟是哪个高斯分布生成的。所以每次循环时，先固定当前的高斯分布不变，获得每个数据点由各个高斯分布生成的概率。然后固定该生成概率不变，根据数据点和生成概率，获得一个组更佳的高斯分布。循环往复，直到参数的不再变化，或者变化非常小时，便得到了比较合理的一组高斯分布。

### 2.2 GMM和K-Means的比较

- 相同点
  - 都是聚类算法
  - 都需要指定K值
  - 都使用EM算法来求解
  - 都只能收敛到局部最优
- 而GMM相对于K-Means来说，优点是可以给出一个样本属于某个类的概率是多少；不仅仅可以用于聚类，还可以用于概率密度估计，而且可以用于生成新的数据样本点。



## 3. 聚类算法如何评估

由于数据以及需求的多样性，没有一种算法能够适用于所有的数据类型、数据簇或应用场景，似乎每种情况都可能需要一种不同的评估方法或度量标准。例如，**K均值聚类可以用误差平方和来评估，但是基于密度的数据簇可能不是球形， 误差平方和则会失效**。在许多情况下，判断聚类算法结果的好坏**强烈依赖于主观解释。**尽管如此，聚类算法的评估还是必需的，它是聚类分析中十分重要的部分之一。

聚类评估的任务是估计在数据集上进行聚类的可行性，以及聚类方法产生结 果的质量。这一过程又分为三个子任务。

1. **估计聚类趋势。**

   这一步骤是检测数据分布中是否存在非随机的簇结构。如果数据是基本随机 的，那么聚类的结果也是毫无意义的。我们可以观察聚类误差是否随聚类类别数 量的增加而单调变化，如果数据是基本随机的，即不存在非随机簇结构，那么聚 类误差随聚类类别数量增加而变化的幅度应该较不显著，并且也找不到一个合适 的K对应数据的真实簇数。

2. **判定数据簇数。**

   确定聚类趋势之后，我们需要找到与真实数据分布最为吻合的簇数，据此判定聚类结果的质量。数据簇数的判定方法有很多，例如手肘法和Gap Statistic方 法。需要说明的是，用于评估的最佳数据簇数可能与程序输出的簇数是不同的。 例如，有些聚类算法可以自动地确定数据的簇数，但可能与我们通过其他方法确 定的最优数据簇数有所差别。

3. **测定聚类质量。**

   在无监督的情况下，我们可以通过考察簇的分离情况和簇的紧 凑情况来评估聚类的效果。定义评估指标可以展现面试者实际解决和分析问题的 能力。事实上测量指标可以有很多种，以下列出了几种常用的度量指标，更多的 指标可以阅读相关文献。

   轮廓系数、均方根标准偏差、R方（R-Square）、改进的HubertΓ统计。

