# 对比学习（Contrastive Learning）

## 图对比学习

### MoCL:Contrastive Learning on Molecular Graphs with Multi-level Domain Knowledge

> 【KDD2021】多层次领域知识在分子图上的对比学习

- GNN是数据需求性，但在现实世界中获取有标签的数据是非常昂贵的，但以一种无监督的方式对GNN进行预处理是现有的探索
- 图对比学习通过最大化成对图增强之间的互信息，已被证明对各种下游任务是有效的。
- 现有的图对比学习框架局限性：
  - 增强是为一般图设计的，因此对于某些领域可能不能适合或不够强大
  - 对比方案只学习对局部扰动不变的表示，一i那次不考虑数据集的全局结构
- 本文主要针对生物医学领域存在分子图的图对比学习，提出了新的框架MoCL：
  - 利用领域知识在局部或全局水平上帮助表示学习
  - 局部层次的领域知识扩展过程，这样在不改变图语义的情况下