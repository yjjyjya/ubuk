# 电子书 Hadoop 数据分析

标签：云计算

---

## **基础概念**

数据是编程界的“货币”
**数据产品** 是数据与用于推断或预测的统计算法的结合，是一个从数据中学习、自适应并且广泛适用的系统
数据产品例如：推荐系统、恒温器、无人驾驶汽车、智能电网

典型的分析工作流：采集 → 整理 → 建模/计算 → 报告和可视化
大数据流水线：包括采集、分段、计算和工作流管理这 4 个主要阶段的迭代模型，工作流管理出的有用信息还可能通过反馈流机制作为下一次迭代的输入

- 数据团队
    数据工程师
    数据分析师
    领域专家

- Hadoop 是大数据操作系统
    分布式文件系统 HDFS
    负载和资源管理器 YARN
    批处理 MapReduce
    内存计算 Spark
    流式计算 Storm
    SQL Hive

- 概念：
    数据添加到集群后会被分发到各个节点上
    数据块大小一般为128MB，跨系统多次复制以提供冗余，提高容错率，保证数据安全
    一个大作业被分解为小任务
    开发人员专注于数据和计算，不用担心底层的分布式编程细节

> 什么是守护进程（Daemon）
保护程序/服务的正常运行，当程序被关闭、异常退出等时能够再次启动程序/恢复服务
例如 http 服务的守护进程叫 httpd，mysql 服务的守护进程叫 mysqld 
有时候我们需要让我们的程序/服务能不中断地运行，在关闭终端后也能在后台默默运行
除了可以这样：`nohup./xxx &`，也可以写成 Daemon 程序，例如一个服务器

- 集群
    HDFS 和 YARN 提供 API，使得开发人员不用关注底层的集群管理细节
    集群就是运行 HDFS 和 YARN 的一组计算机，每台就是一个节点，[1,+∞)
    Hadoop 进程是服务，这意味着它们一直在集群节点上运行，接受输入并通过网络传
    递输出
    一般来说，拥有 20~30 个 worker 节点和单个 master 节点的集群足以在几十太字节的数据集上同时运行多个作业

- 节点
    - master 节点
    为 Hadoop 的 worker 节点提供协调服务。没有 master 节点，协调就不复存在，也就不可能进行分布式存储或计算
    - worker 节点
    集群中的大多数计算机都属于这类节点。worker 节点运行的服务从 master 节点接受
    任务——存储或检索数据、运行特定应用程序。worker 节点通过并行分析运行分布
    式计算

- HDFS 的 master 服务和 worker 服务
    - NameNode（master 服务）
    用于存储文件系统的目录树、文件元数据和集群中每个文件的 **位置**，像交警指挥交通一般，将客户端指向正确的 DataNode
    - Secondary NameNode（master 服务）
    代表 NameNode **执行内务任务并记录检查点**。虽然它叫这个名字，但它并不是 NameNode 的备份
    - DataNode（worker 服务）
    用于 **存储和管理** 本地磁盘上的 HDFS 块，将各个数据存储的健康状况和状态报告给 NameNode

- YARN 的 master 服务和 worker 服务
    - ResourceManager（master 服务）
    为应用程序 **分配和监视可用的集群资源**（如内存和处理器核心这样的物理资源），处理集群上作业的调度
    - ApplicationMaster（master 服务）
    根据 ResourceManager 的调度，**协调** 在集群上运行的特定应用程序
    - NodeManager（worker 服务）
    在 **单个节点** 上运行和管理处理任务，报告任务运行时的健康状况和状态

> 单节点集群
在“伪分布式模式”中，单个机器将运行所有 Hadoop 守护进程，就好像它是集群的一部分，但网络流量是通过本地环回网络接口流动的。这种模式虽然没有发挥出分布式架构的优势，但却是一种完美的开发模式，因为不必为管理几台机器而费心。Hadoop 开发人员通常使用伪分布式环境，该环境通常位于虚拟机内部，通过 SSH 连接虚拟机

- HDFS
    集中式存储架构
    一般用于存储原始输入数据或者计算阶段的中间结果
    **“数据湖泊”**，里面的数据通过一次写入可以多次读取，并创建大量的异构数据用于不同的计算分析
    - 文件块
        大文件拆分并分发给其他计算机
        每个块都将复制三份（故实际可用磁盘空间比硬件磁盘空间少）
    - 数据管理
        NameNode 记录块所在的位置，定位块的位置
        Secondary NameNode 执行内务任务，合并日志

- YARN
    Hadoop2 时引入，突破了 MapReduce 作业 / 工作负载管理功能与集群 / 资源管理功能高度耦合的限制
    将工作负载管理与资源管理分离

***

## **配置伪分布式节点**

- 更新系统软件
    `$ sudo apt-get update && sudo apt-get upgrade`
    `$ sudo apt install vim`
    `$ sudo apt install net-tools`
    `$ sudo apt install openssh-server`
- 创建 Hadoop 用户
    `$ sudo addgroup hadoop`
    `$ sudo adduser --ingroup hadoop hadoop`
    `$ sudo usermod -a -G hadoop student`
    https://blog.csdn.net/liu_dong_kang/article/details/62881788
- 设置固定 IP
    请查看 linux 常见问题中的：设置子网和主机名
- 配置 SSH
    `ssh-keygen`
    `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`
    `chmod 600 ~/.ssh/authorized_keys`
- 安装 Java
    ```
    sudo apt install openjdk-8-jdk-headless
    whereis jvm
    cd /usr/lib/jvm
    cd java-8-openjdk-amd64/
    ls
    ```
    
    环境变量设置：
    ```
    vi ~/.bashrc
    添加：
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    export JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
    ```
    `$ java -version`
- 禁用 IPv6
    编辑 /etc/sysctl.conf 文件 `$ gksu gedit /etc/sysctl.conf`
    后将以下内容添加到文件的末尾：
    ```
    # 禁用ipv6
    net.ipv6.conf.all.disable_ipv6 = 1
    net.ipv6.conf.default.disable_ipv6 = 1
    net.ipv6.conf.lo.disable_ipv6 = 1
    ```
    
    重新启动，使用以下命令检查状态 `$ cat /proc/sys/net/ipv6/conf/all/disable_ipv6` 若输出 1 则成功禁用
- 安装 Hadoop
    `curl -O http://apache.mirror.com/hadoop-2.5.0/hadoop-2.5.0.tar.gz`
    前往 ISCAS 镜像网站寻找 hadoop 安装包
    解压、修改四个配置文件、生成log文件地址并赋予权限、启动服务的两条命令
        
***

## **常用操作**

- 查看 fs 命令下可用的命令 `$ hadoop fs -help` 
- 从 **本地文件系统** 复制莎士比亚全集到 **远程的（分布式）文件系统**
    `$ hadoop fs -copyFromLocal shakespeare.txt shakespeare.txt`
    全写文件路径 `$ hadoop fs –put /home/analyst/shakespeare.txt hdfs://localhost/user/analyst/shakespeare.txt`
    /user/analyst/是远程文件系统的主目录
- 在远程主目录创建文件夹
    `$ hadoop fs -mkdir ...`
- 列出远程主目录的内容
    `$ hadoop fs -ls -l`
    会列出权限、副本数、用户、组、以字节为单位的文件大小（目录为零）、最后一
次修改的日期和时间，以及文件名
- 将输出通过管道传递给 less 以查看远程文件的内容
    `$ hadoop fs –cat shakespeare.txt | less`
    可以通过方向键导航文件，键入 q 退出并退回到终端
- 仅检查文件的最后 1000 字节
    `$ hadoop fs –tail shakespeare.txt | less`
- 将整个文件从分布式文件系统传输到本地文件系统
    在管道传输的时候使用压缩工具
    `$ hadoop fs –get shakespeare.txt ./shakespeare.from-remote.txt`
- 管理文件和目录的权限，chmod、chgrp 和 chown 命令
    将 shakespeare.txt 的权限更改为 -rw-rw-r--。664 是为权限三元组设置的标志的八进制表示
    `$ hadoop fs –chmod 664 shakespeare.txt`
    chgrp 和 chown 命令分别更改分布式文件系统上文件的 **组和所有者**

> **POSIX**
表示可移植操作系统接口（Portable Operating System Interface of UNIX），POSIX 标准定义了操作系统应该为应用程序提供的接口标准
意在期望获得软件可移植性。换句话说，为一个 POSIX 兼容的操作系统编写的程序，应该可以在任何其它的 POSIX 操作系统（即使是来自另一个厂商）上编译执行
>> Unix设计哲学中有这样子的一条：“舍高效率而取可移植性”

> 这很容易让人想到那些依靠 **虚拟机** 支持的跨平台开发语言的 **跨平台特性**，例如 JAVA，可以说它的跨平台能力是 **靠牺牲性能** 而换取来的。但遵守 POSIX 标准开发的程序在支持 POSIX 标准的操作系统间运行是不需要依靠类似虚拟机这种中间层的支持的，这就能够在不损失性能的前提下，带来强大的跨平台可移植能力
当然这种理解很美好，但实际上很多兼容 POSIX 标准的操作系统所做的实现是在自身原有的 API 接口的基础之上再封装创建一层 POSIX 兼容层来提供对 POSIX 支持，因此这意味着会占用更多一些的系统资源，但这种操作系统的原生支持（即便是二次封装出来的）相比较依托虚拟机的程序来说性能还是要给力的多的多

***

## **MapReduce**

Python 中 map 和 reduce 函数的伪代码
``` Python
def map(key, value):
    # 执行处理
    return (intermed_key, intermed_value)

def reduce(intermed_key, values):
    # 执行处理
    return (key, output)
```

mapper 操作的副本分发到集群上的每一个节点
map和reduce之间需要shuffle和sort进行协调

- 具体操作：
    HDFS 的本地数据以键值对的形式被加载到一个映射过程
    mapper 输出零个或多个键值对，将计算所得的值映射到一个特定的键上
    基于键对这些键值对进行 sort 和 shuffle 操作，然后将它们传递给 reducer，使 reducer 获得键的所有值
    reducer 输出零个或多个最终的键值对，即输出（归约 map 的结果）

- 单词计数
    单词计数应用程序以一个或多个文本文件作为输入，生成一份单词及其频率的列表
    ``` Python
    # emit是一个执行Hadoop I/O的函数
    def map(dockey, line):
        for word in Line.split():
        emit(word, 1)
    
    def reduce(word, values):
        count = sum(value for value in values)
        emit(word, count)
    # emit 是一个执行 Hadoop I/O 的函数；也就是说，它将其参数发送到 MapReduce 流水线的下一个阶段，类似于 Python 中的 yield 函数
    ```

- 分析社交网络
    查看用户间有哪些共同好友
    ``` Python
    def map(person, friends):
        # 键是用户的名称，值是用逗号分隔的朋友列表
        for friend in friends.split(","):
        pair = sort([person, friend])
        emit(pair, friends)
    
    def reduce(pair, friends):
        shared = set(friends[0])
        shared = shared.intersection(friends[1])
        emit(pair, shared)
    ```

MapReduce 不支持通过单个 map 或 reduce 进行迭代
更复杂的应用程序是通过被称为“作业链”的过程，使用多个 MapReduce 作业
执行单个计算来构建的
MapReduce 的 API 是用 Java 编写的，因此提交给集群的 MapReduce 作业是编译好的 Java 归档（Java Archive，JAR）文件

- 将 Hadoop 作业编译成一个 JAR 文件
    `$ hadoop com.sun.tools.javac.Main WordCount.java`
    `$ jar cf wc.jar WordCount*.class`
    这会在当前工作目录中创建一个 wc.jar 文件
- 作业提交
    `$ hadoop jar wc.jar WordCount shakespeare.txt wordcounts`
    作业将执行并输出 mapper 和 reducer 的状态，并且在完成时报告作业完成情况的统计信息。一旦完成，作业的结果将写入 wordcounts 目录
    `$ hadoop fs –ls wordcounts`
    `$ hadoop fs –cat wordcounts/part-00000 | less`
- 列出所有正在运行的作业
    `$ hadoop job -list`
    - 通过 -kill 命令终止某作业
        `$ hadoop job -kill $JOBID`

***

## **Hadoop Streaming**

是 JAR 文件，实用程序
可以指定输入输出的 HDFS 路径参数，还可以指定 mapper、reducer 的可执行程序
注意这里的 Streaming 是指标准的 Unix 流：stdin、stdout、stderr

- mapper.py
    ``` Python
    #!/usr/bin/env python
    import sys
    if __name__ == "__main__":
        for line in sys.stdin:
            for word in line.split():
                sys.stdout.write("{}\t1\n".format(word))
    # 从 sys.stdin 读取每一行，使用空格拆分该行文本，然后逐行将得到的每个单词和数字 1 写入 sys.stdout，并用制表符将两者分隔
    ```

- reducer.py
    ``` Python
    #!/usr/bin/env python
    import sys
    if __name__ == '__main__':
        curkey = None
        total = 0
        for line in sys.stdin:
            key, val = line.split("\t")
            val = int(val)
            if key == curkey:    #若等于上一次的 key，就直接在上一次的基础上累加
                total += val
            else:
                if curkey is not None:
                    sys.stdout.write("{}\t{}\n".format(curkey, total))
            curkey = key
            total = val
    # 注意！！！这里 stdin 是接收从 mapper 输出的、经过排序的逐行输入，故可以如上编程实现 wordcount
    # 若没有事先排序则是不行的
    ```

> 注意
1、代码在 “ifmain” 块中
在 Python 中，只有脚本作为程序的主入口点运行时，此条件才会被触发，被导入的脚本不会运行该方法。Python 开发人员使用它来判断代码是否在一个库中，或者确保任何执行的代码都在 Python 脚本的底层运行，以方便调试。通过这个语句，可以确保这个块不是导入代码以继承 mapper，如果是则这个块就不会被执行
2、每个 mapper 和 reducer 都视为可执行程序，所以每个 Python 文件都应以 #!/usr/bin/env python 开头

- 在 CSV 上的计算
    数据展示
    `2014-04-01,19805,1,JFK,LAX,0854,-6.00,1217,2.00,355.00,2475.00`
    `2014-04-01,19805,2,LAX,JFK,0944,14.00,1736,-29.00,269.00,2475.00`
    - mapper.py
        
        ``` Python
        #!/usr/bin/env python
        import sys
        import csv
        SEP = "\t"
        class Mapper(object):
            def __init__(self, stream, sep=SEP):
                self.stream = stream
                self.sep = sep
            def emit(self, key, value):
                sys.stdout.write("{}{}{}\n".format(key, self.sep, value))
            def map(self):
                self.status("mapping started")
                def map(self):
                    for row in self:
                        if row[6] < 0:
                            self.counter("early departure")
                        else:
                            self.counter("late departure")
                        self.emit(row[3], row[6])    #始发机场（位置 3）并将此作为键，将起飞延误时间（位置 6）作为值
                self.status("mapping complete")
            def __iter__(self):
                reader = csv.reader(self.stream)
                for row in reader:
                    yield row
            def status(self, message):
                sys.stderr.write("reporter:status:{}\n".format(message))
            def counter(self, counter, amount=1, group="ApplicationCounter"):
                sys.stderr.write(
                    "reporter:counter:{},{},{}\n".format(group, counter, amount)
                )
        if __name__ == '__main__':
            mapper = Mapper(sys.stdin)
            mapper.map()
        
        ```
        `__iter__` 函数的实现使该类成为可迭代的，该函数返回一个生成器（一般通过 yield 语句构造）；该函数如果简单地返回 self，就必须同时实现 next 或 `__next__` 方法，这两个方法在迭代完成时抛出 StopIteration。这个类现在可以用于 for 语句，如：
        ```
        for item in Mapper():
            print(item)
        ```
    - reducer.py
    ``` Python
    #!/usr/bin/env python
    import sys
    from itertools import groupby
    from operator import itemgetter
    SEP = "\t"
    class Reducer(object):
        def __init__(self, stream, sep=SEP):
            self.stream = stream
            self.sep = sep
        def emit(self, key, value):
            sys.stdout.write("{}{}{}\n".format(key, self.sep, value))
        def reduce(self):
            for current, group in groupby(self, itemgetter(0)):
                self.status("reducing airport {}".format(current))
                total = 0
                count = 0
                for item in group:
                    total += item[1]
                    count += 1
                    self.counter("airports")
                    self.emit(current, float(total) / float(count))
        def __iter__(self):
            for line in self.stream:
                #异常处理在处理大数据集时至关重要
                #一种常用的策略是跳过引发异常的行，因为还有大量的数据需要计算
                try:
                    parts = line.split(self.sep)
                    yield parts[0], float(parts[1])
                except:
                    continue
    if __name__ == '__main__':
        reducer = Reducer(sys.stdin)
        reducer.reduce()
    ```

- 执行 Streaming 作业
    - 使用 Linux 管道和 sort 命令模拟 Hadoop MapReduce 流水线
        `$ chmod +x mapper.py`
        `$ chmod +x reducer.py`
        使用 cat 命令输出文件的内容，通过管道将输出从 stdout 传输到 mapper.py 的 stdin，再传输到 sort，然后到 reducer.py，最后将结果打印到屏幕上
        `$ cat flights.csv | ./mapper.py | sort | ./reducer.py`

    - 在集群上执行 Streaming 作业
        ```
        # 需要将 Hadoop Streaming JAR 提交给作业客户端，并传入自定义的操作符参数
        $ hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
            -input flights.csv \
            -output average_delay \
            -mapper mapper.py \
            -reducer reducer.py \
            -file mapper.py \
            -file reducer.py
        # -file 选项，它让 Streaming 作业往集群上发送脚本（否则程序无法在节点上找到这些脚本）
        
        # 在 Windows 系统上，注意文件格式
        hadoop fs -rm -r /user/simpletest/
        hadoop jar D:\hadoop\hadoop-3.2.3\share\hadoop\tools\lib\hadoop-streaming-*.jar 
            -D stream.non.zero.exit.is.failure=false 
            -files file:///D:/jupyterproject/hadoop/mapper.py 
            -files file:///D:/jupyterproject/hadoop/reducer.py 
            -input file:///D:/jupyterproject/hadoop/simpletest.csv 
            -output /user/simpletest/output 
            -mapper "D:\python\python.exe mapper.py" 
            -reducer "D:\python\python.exe reducer.py"
        ```

- combiner
    因为 mapper 会产生大量的中间数据，这些数据需要经过数据传输进行 shuffle 和 sort，而网络资源有限，大量的数据传输可能会导致作业延迟等等问题。所以 combiner 本质是在数据传输之前做一个局部的 reduce 来减少中间数据
    combiner 预先计算每个键的和，减少生成的键值对的数量，从而减少网络流量

- partitioner
    通过划分键空间将键值分配给每个 reducer，分配会尽量均匀以平衡各 reducer 的工作负载

- 工作链
    可以解决复杂的算法，将它分解为几个较小的 MapReduce 任务。开发人员必须考虑每一步计算怎样 reduce 出中间值——不仅仅是 mapper 和 reducer 之间的中间值，还包括作业之间的中间值
    - 例子：计算 Pearson 相关系数
        第一个 MapReduce 作业将计算 n 以及 x 和 y 的平均值
        
        ``` Python
        class VariablePairsMapper(Mapper):
            def map(self):
                # 计算(x, y)的个数及和
                # 输出键是x在vector中的索引
                for y, vector in self:
                    for x, i in enumerate(vector):
                        self.emit(i, (1, x, y) )
        class PairsMeanReducer(Reducer):
            def reduce(self):
                for key, values in self:
                    # 将所有的值加载到内存，这样可以迭代两次
                    values = list(values)
                    # 计算(x, y)的和及元素的个数
                    sx, sy, sn = 0
                    for (n, x, y) in values:
                        sn += n
                        sx += x
                        sy += y
                    # 计算x和y的平均值
                    xbar = sx / n
                    ybar = sy / n
                    # 发射每一个(x, y)及x和y的平均值
                    for (n, x, y) in values:
                        self.emit(key, (x, y, xbar, ybar))
        ```
        计算协方差和标准差，需要再次传入相同的输入数据，并将第一个作业的输出作为该作业的输入
        ``` Python
        import math
        class PearsonMapper(Mapper):
            def map(self):
                # 计算x和xbar的差及y和ybar的差
                # 发射差的乘积及其平方
                for i, (x, y, xbar, ybar) in self:
                    xdiff = x-xbar
                    ydiff = y-ybar
                    self.emit(i, (xdiff*ydiff, xdiff**2, ydiff**2))
        class PearsonReducer(Reducer):
            def reduce(self):
                for key, values in self:
                    # 计算差乘积的和以及平方的和
                    sxyd = 0
                    sxd2 = 0
                    syd2 = 0
                    for (xyd, x2d, y2d) in values:
                        sxyd += xyd
                        sxd2 += x2d 
                        syd2 += y2d
                # 发射相关系数
                r = sxyd / (math.sqrt(sxd2) * math.sqrt(xyd2))
                self.emit(key, r)
        ```

***

## **Spark**
    
Spark 主要通过名为弹性分布式数据集（resilient distributed dataset，RDD）的新数据模型实现高速运行，该数据模型在计算时 **存储在内存** 中，从而避免了昂贵的中间内存计算磁盘写操作。因此，Spark 程序员不是简单地指定 map 步骤和 reduce 步骤，而是在执行某个需要协调的动作（如规约或写入磁盘）之前，指定一系列将应用于输入数据的 **数据流转换**
> DAG 有向无环图，用于描述数据流步骤，步骤相连且单步不重复

- Spark 栈
    Spark 是一个计算框架，专注于计算而非数据存储，它可以利用 YARN 和 HDFS 进行集群管理和分布式存储
    - 主要组件
        Spark SQL
        Spark Streaming
        MLlib
        GraphaX

- RDD
可以根据转换过程重建、从分布式存储读取写入、高速缓存在worker节点的内存中以快速重用








***

## **分布式分析和模式**

单个运算只对数据进行多个微小的处理，而要想得到更有意义的结果，必须将这些运算组成一个被称为数据流的分步序列，数据流被描述为有向无环图（DAG）

但是许多算法都不能轻易转换为 DAG，例如在整个计算过程中 **维持或更新单个数据结
构** 的算法（需要一些共享内存），或者 **依赖中间步骤** 计算结果的算法（需要中间进程间通
信），引入循环的算法，特别是 **循环次数不限的迭代算法**，也不容易描述为 DAG

- 键计算
    **Web 日志** 记录是 Hadoop 大数据计算的典型数据源，因为它们代表每个用户的点击流式数
    据，从中可以轻松探究数据的多个方面
    ``` Python
    # 使用复合键将文本分解为两个每日时间序列，一个用于本地流量，另一个用于远程流量
    import re
    from datetime import datetime
    # 解析日志记录中的日期时间
    dtfmt = "%d/%b/%Y:%H:%M:%S %z"
    # 使用正则表达式解析日志记录
    linre = re.compile(r'^(\w+) \- \- \[(.+)\] "(.+)" (\d+) ([\d\-]+)$')
    def parse(line):
        # 使用正则表达式匹配日志记录
        match = linre.match(line)
        if match is not None:
            # 正则表达式含有分组，能提取日志源、时间戳、
            # 请求、状态码和响应字节大小
            parts = match.groups()
            # 解析日期时间，返回日志源、年和天
            date = datetime.strptime(parts[1], dtfmt).timetuple()
            return (parts[0], date.tm_year, date.tm_yday)
    ```
    理解复合数据的序列化和反序列化。序列化是指将内存中的对象转换成 **字节流**，使其可以被 **写入磁盘或通过网络传输**（反序列化是指相反的过程）
    简单地使用内置的 str 函数对不可变类型（例如元组）进行序列化
    ``` Python
    import ast
    def map(key, val):
        # 解析复合键，它是一个元组
        # literal_eval 函数评估元组字符串得到 Python 元组类型
        key = ast.literal_eval(key)
        # 以字符串写新的键
        return (str(key), val)
    ```

    - 影响键空间的几种模式
    特别是爆炸（explode）、过滤、变换和恒等（identity）模式
        - 键空间变换
            直接赋值、复合、分割和 **键值换位**
        - 爆炸 mapper
            针对单个输入键生成多个中间键值对，通过键移位（key shift）和将值拆分为多个部分来实现的
        - 过滤器 mapper
        - 恒等模型
        恒等 mapper 通常用于在数据流中执行多个 reduce。当在 MapReduce 中使用恒等 reducer 时，该作业等同于在键空间上进行排序

- 设计模式

- 迈向最后一英里
假设我们有一个新闻报道或博文的数据集，现在要预测接下来的 24 小时内的评论数量