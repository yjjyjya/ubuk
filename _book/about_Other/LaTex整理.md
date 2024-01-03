# *几个概念*

Tex：一种具有编译和排版功能的基础语言，类似于 C 语言  
LaTeX：是 Tex 的扩展，有许多宏包，功能更加丰富  
TexLive：Tex 语言的编辑器，操作没那么便利  
Texstudio：相当于 TexLive 套上一个外壳，不过编辑起来更加方便  

# *主要公式*

``` latex
主要内容

\begin{document}

\end{document}
```

``` latex
摘要

\begin{abstract}

\end{abstract}
```

``` latex
\section{这里写标题}
\subsection{这里写小标题}

注意这个会自动对标题进行标号
```

``` latex
绘制三线表，即只有三条线的表格

\begin{table}[!htbp]
    \setlength{\tabcolsep}{3mm}
    \begin{tabular}{ccccc}
        \toprule[1.5pt]
        符号 & 含义 \\
        \midrule[1pt]
        $S_{i}$ & i=1，2，3分别为当日可分配的医用品，消耗品，日用品的总量 \\
        $[x_{i1},x_{i2},x_{i3}]$ & 三者分别代表第i个灾区，每人每日实际收到的医用品，消耗品，日用品的数量 \\
        $c_{i}$ & 从所有灾区中划分的第i个灾区 \\
        $R$ & 模糊相似矩阵 \\
        $c_{ij}$ & 第i个灾区中第j个受灾指标 \\
        $a$ & 灾区每人每日医用品平均使用量 \\
        $b$ & 灾区每人每日消耗品品平均使用量 \\
        $c$ & 灾区每人每日日用品平均使用量 \\
        \bottomrule[1.5pt]
    \end{tabular}
\end{table}
```

``` latex
公式

\begin{equation}
    \alpha_{i}=\frac{P_{ih}+P_{iw}\times2}{P_{i}},i=(B_{1},B_{2},B_{3}\cdots,B_{10})
    \label{1}
\end{equation}

\cref{1}，表示对 label 为 1 的公式进行引用
```

``` latex
图片

\begin{figure}[!h]
	\centering
	\includegraphics[width=1.1\textwidth]{图1}
	\caption{模糊相似矩阵}
\end{figure}
```

``` latex
matlab 代码块

\begin{lstlisting}[language=matlab]

\end{lstlisting}
```

关键字 `\keywords{}`  
空格 `\quad`  
换行 `\par`  


# *向量求导法则*

参考资料：https://zhuanlan.zhihu.com/p/273729929  
假设向量 x 为：  
$$\vec{x} = [x_{1}, x_{2}...x_{n}]^{T}$$  
矩阵 $A_{n \times n}$ 为常数矩阵  

1、常数求导  
$$\frac{\partial c}{\partial x} = 0$$

2、公式  
$$\frac{\partial x^{T}a}{\partial x} = \frac{\partial a^{T}x}{\partial x} = a$$  
$$\frac{\partial x^{T}x}{\partial x} = 2x$$  
$$\frac{\partial x^{T}Ax}{\partial x} = Ax+A^{T}x$$  
$$\frac{\partial a^{T}xx^{T}b}{\partial x} = \frac{\partial x^{T}ab^{T}x}{\partial x} = ab^{T}x + ba^{T}x$$  

矩阵求导法则  
$$\frac{\partial a^{T}Xb}{\partial x} = ab^{T}$$  
$$\frac{\partial a^{T}X^{T}b}{\partial x} = \frac{\partial b^{T}Xa}{\partial x} = ba^{T}$$  
$$\frac{\partial a^{T}XX^{T}b}{\partial X} = \frac{\partial X^{T}ab^{T}X}{\partial X} = ab^{T}X + ba^{T}X$$  

$$\begin{aligned}
\frac{\partial a^{T}X^{T}Xb}{\partial X} = \, & \frac{\partial a^{T}(X^{T})(X^{T})^{T}b}{\partial (X^{T})^{T}} \\
= \, & (\frac{\partial a^{T}(X^{T})(X^{T})^{T}b}{\partial X^{T}})^{T} \\
= \, & (ab^{T}X^{T}+ba^{T}X^{T})^{T} \\
= \, & Xba^{T}+Xab^{T} \\
\end{aligned}$$

可以注意一下上面等式的写法


# *推荐网站*

[环境搭建](https://www.jianshu.com/p/9f44e57ac4d0)  
[在线编辑](https://www.codecogs.com/latex/eqneditor.php)  
[在线编辑](https://latex.vimsky.com/)  
[配合Markdown](https://blog.csdn.net/lanxuezaipiao/article/details/44341645)  