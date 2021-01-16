## 课程体系

### 1 What\`s the Merchine learning ?
### 2 What\`s the KNN algorithm?
### 3 What\`s the regression?
### 4 What\`s the loss function  and why it\`s the key for our marchine learning  task?
### 5 What is  Gradient Descent?
### 6 More complication function
### 7 Activation function
### 8 Neural network
### 9 Deep learning
### 10 Back propagation
### 11 Auto-back propogation
### 12 Topological sorted
### 13 Auto_Compute Gradient
### 14 All the elements  of a neural network framework

## 数学知识

### lesson 01

### corr() 相关性分析

KNN 通过相近数据的一个评价指标进行评价，【常见的是欧式距离$L = (\hat{y}-y_i)^2$】
### 模拟函数$f(x) = k * x + b$ 线性函数
#### 参数：{k, b}求解
#### 评价指标：好坏｜ Loss函数 (MSE)
$$loss(\hat{y},y) = \frac{1}{N}\sum_{i \in N} (y_i - \hat{y_i})^2 $$

#### 如何获取最优的K和b 
- 1. 使用微积分计算
$$
\begin{align}loss & = \frac{1}{n} \sum(y_i - \hat{y_i})^2 \\
& = \frac{1}{n} \sum(y_i - (k \cdot x_i + b))^2 \\
&\Rightarrow A\cdot k^2 + B \cdot k + C
\end{align}
$$

- 微积分弊端 ：求解导数异常复杂

- 2. 随机模拟 蒙特卡洛方法

 随机梯度的处理，更新速度随loss 的变小越来越小
 
- 3. 梯度下降方法
$$
\begin{align} \frac{\partial loss}{\partial x} &> 0 \\
k^\prime &= k + (-1)\frac{\partial loss(k,b)}{\partial k_n}\cdot \theta \\
b^\prime &= b + (-1)\frac{\partial loss(k,b)}{\partial b_n}\cdot \theta \\
\alpha \\
\nabla {\frac{\partial loss}{\partial k}}
\end{align}
$$
$\star$ 核心：梯度下降


####   From simple linear Regression to complicated neural networks 
#### From manul coding gradients to auto-gradients
#### Previus :let the computer fit functions 
$$sigmoid(x) = \sigma(x) = \frac{1}{1+e^{-x}}$$

$$\frac{\partial{loss}}{\partial{l_1}}\cdot \frac{\partial{l_1}}{\partial{\sigma}}\cdot \frac{\partial \sigma}{\partial l_2} \cdot \frac{\partial l_2}{\partial k_2}$$

$$链式求导$$

$$\diamondsuit$$
$$\heartsuit$$
$$\clubsuit$$
$$\spadesuit$$

