
## **简介**
Hadoop 是一个分布式计算的解决方案，可编写和运行分布式应用，处理大规模数据
Hadoop = HDFS（文件系统，数据存储技术相关）+ MapReduce（数据处理）
开源
适合离线和大规模数据分析，但是不适合对几个记录随机读写的在线事务处理模式
处理半结构化和非结构化数据上，相比关系型数据库其更加灵活
不管任何数据形式最终会转化为key/value，key/value是基本数据单元

## **版本**
- Hadoop1.0
    - Hadoop 版本为 0.20.x、0.21.x，0.22.x 和 1.x
    - 分布式文件系统 HDFS + 分布式计算框架 MapReduce
    - HDFS 由一个 NameNode 和多个 DataNode 组成，MapReduce 由一个 JobTracker 和多个 TaskTracker 组成
- Hadoop2.0
    - Hadoop 版本为 0.23.x 和 2.x
    - 针对 Hadoop 1.0 中的 MapReduce 在扩展性和多框架支持方面的不足，提出了全新的资源管理框架 YARN，它将 JobTracker 中的资源管理和作业控制功能分开，分别由组件 ResourceManager 和 ApplicationMaster 实现
    - ResourceManager 负责所有应用程序的资源分配，而 ApplicationMaster 仅负责管理一个应用程序

## **实际应用**
facebook 用 Hive 来进行日志分析
淘宝搜索中的自定义筛选也使用的 Hive
以及 Twitter、LinkedIn 上使用 Hive 用于发现您可能认识的人，可以实现类似 Amazon.com 的协同过滤的推荐效果
商品推荐也是，天猫的推荐系统是 Hive
垃圾邮件的识别和过滤，还有用户特征建模

## **举例**
- 假设现在有一个 100M 大小的数据库备份的 sql 文件，在不导入到数据库的情况下过滤出想要的内容可以怎么做？
    - 用 linux 的命令 grep 操作，通过正则匹配
    - 通过编程来读取文件，然后对每行数据进行正则匹配

    目前上述两种方法都可以轻松应对，但如果是 1G、1T 甚至 1PB 的数据呢，上面的方法就行不通了，毕竟单台服务器的性能总有其上限
    有种解决方法就是分布式计算，分布式计算的核心就在于利用分布式算法把运行在单台机器上的程序扩展到多台机器上并行运行，从而使数据处理能力成倍增加
- Hadoop 可以很轻易的把 很多 linux 的廉价 PC 组成分布式结点，然后编程人员只需要根据 mapreduce 的规则定义好接口方法，剩下的就交给 Hadoop。它会自动把相关的计算分布到各个结点上去，然后得出结果
- Hadoop 首先把 1PB 的数据文件导入到 HDFS 中，然后编程人员定义好 map 和 reduce，也就是把文件的行定义为 key，每行的内容定义为 value，然后进行正则匹配，匹配成功则把结果通过 reduce 聚合起来返回
    Hadoop 就会把这个程序分布到 N 个结点去并行的操作，那么原本可能需要计算好几天，在有了足够多的结点之后就可以把时间缩小到几小时之内
- [腾讯大数据的文章](https://blog.csdn.net/dftgcdf45645466/article/details/89065714)
    比如说要获取 /hdfs/tmp/file1 的数据，虽然引用的是一个文件路径，但是实际的数据存放在很多不同的机器上
    MapReduce 是第一代计算引擎。Map 阶段各个机器分别处理，Reduce 阶段再将结果进行汇总。虽然好用，但是很笨重
    Tez 和 Spark 是第二代。让 Map 和 Reduce 之间的界限更模糊，数据交换更灵活，更少的磁盘读写，以便更方便地描述复杂算法，取得更高的吞吐量
    但是 MapReduce 的程序写起来很麻烦，所以有了 Pig、Hive。Pig 是接近脚本方式去描述 MapReduce，Hive 则用的是 SQL。它们把脚本和 SQL 语言翻译成 MapReduce 程序，丢给计算引擎去计算
    但是 Hive 在 MapReduce 上跑太慢了，于是 Impala，Presto，Drill 诞生了。牺牲了通用性、稳定性等特性，为了让用户更快速地处理 SQL 任务
    为了更加高速的处理，例如不断更新的热搜榜，新的计算模型 Streaming（流）计算出现了。数据流进来的时候就进行处理，很好的东西，但是无法替代上面数据仓库和批处理系统
    另外一个重要组件是调度系统。现在最流行的是 Yarn，可以看作是中央管理

***

## **Hadoop Distributed File System (HDFS)**
HDFS 基于 GFS(Google File System) 设计而出
就像很多其他的分布式文件系统一样，HDFS 保存大量数据，并且提供对分布在网络上的许多客户端的透明访问。HDFS 的优势在于通过可靠的、可扩展的方法存储大量的文件
HDFS 通过复制块并在集群中分发副本来确保可靠性。默认的复制因子是三，这意味着每个块在集群上存在三次。即使在机器发生故障时，块级复制也能实现数据可用性

NameNode 和 DataNode 进程可以在一台机器上运行，但 HDFS 集群通常指一台运行 NameNode 进程的专用服务器 + 数千台运行 DataNode 进程的机器

secondary NameNode 用来生成 NameNode 的内存结构的快照，从而降低 NameNode 发生故障时数据丢失的风险
DataNode 发生故障时，NameNode 将复制丢失的块，以确保每个块满足最小复制因子
