## **安装**

1、Java 环境，jdk 版本不低于 1.8
下载地址：https://www.oracle.com/java/technologies/downloads/#java8-windows（需要注册 Oracle 账号），也可以在百度网盘上下载[^jdk下载]

2、Hadoop
下载地址：http://archive.apache.org/dist/hadoop/core/
例如下载 hadoop-3.2.3 这个版本的
注意还要下载在 windows 环境下的第三方包：[winutils](https://github.com/steveloughran/winutils)

3、Spark
下载地址：http://archive.apache.org/dist/spark/
例如下载 spark-3.1.2-bin-hadoop3.2 这个版本的

***

## **配置**

1、配置 jdk 的环境变量
打开环境变量界面，在下面的系统变量中新建一个变量
变量名：`JAVA_HOME`
变量值：jdk 的路径，例如：`D:\java\jdk1.8`
然后双击 Path 变量添加两条
`%JAVA_HOME%\bin`
`%JAVA_HOME%\jre\bin`

2、配置 hadoop 的环境变量
在系统变量中新建一个变量
变量名：`HADOOP_HOME`
变量值：hadoop 的路径，例如：`D:\hadoop\hadoop-3.2.3`
然后双击 Path 变量添加
`%HADOOP_HOME%\bin`

3、配置 spark 的环境变量
变量名：`SPARK_HOME`
变量值：spark 的路径，例如：`D:\spark\spark-3.1.2-bin-hadoop3.2`
然后双击 Path 变量添加两条
`%SPARK_HOME%\bin`
`%SPARK_HOME%\sbin`

4、修改 hadoop 的配置文件
来到 `D:\hadoop\hadoop-3.2.3` 路径下，创建 tmp、data 文件夹
进入 `D:\hadoop\hadoop-3.2.3\data` 路径创建 dfs 文件夹，并进入 dfs 文件夹创建 namenode、datanode 节点存储目录
来到 `D:\hadoop\hadoop-3.2.3\etc\hadoop` 路径下
① 修改：core-site.xml
```
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:50000</value>
    </property>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/D:/hadoop/hadoop-3.2.3/tmp</value>
        <description>Abase for other temporary directories.</description>
    </property>
</configuration>
```
② 修改：hdfs-site.xml
```
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/D:/hadoop/hadoop-3.2.3/data/dfs/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/D:/hadoop/hadoop-3.2.3/data/dfs/datanode</value>
    </property>

    <property>
        <name>dfs.http.address</name>
        <value>localhost:50070</value>
    </property>
    <property>
        <name>dfs.namenode.secondary.http-address</name>
        <value>localhost:50090</value>
    </property>
    <property>
        <name>dfs.namenode.secondary.https-address</name>
        <value>localhost:50091</value>
    </property>
    <property>
        <name>dfs.datanode.socket.write.timeout</name>
        <value>6000000</value>
    </property>
    <property>
        <name>dfs.socket.timeout</name>
        <value>6000000</value>
    </property>
    <property>
        <name>dfs.datanode.max.transfer.threads</name>           
        <value>8192</value>
    </property>
</configuration>
```
③ 重命名 mapred-site.xml.template 为 mapred-site.xml，修改：
```
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>

    <property>
        <name>mapreduce.jobhistory.address</name>
        <value>localhost:10020</value>
    </property>
    <property>
        <name>mapreduce.jobhistory.webapp.address</name>
        <value>localhost:19888</value>
    </property>
    <property>
        <name>yarn.app.mapreduce.am.env</name>
        <value>HADOOP_MAPRED_HOME=/D:/hadoop/hadoop-3.2.3</value>
    </property>
    <property>
        <name>mapreduce.map.env</name>
        <value>HADOOP_MAPRED_HOME=/D:/hadoop/hadoop-3.2.3</value>
    </property>
    <property>
        <name>mapreduce.reduce.env</name>
        <value>HADOOP_MAPRED_HOME=/D:/hadoop/hadoop-3.2.3</value>
    </property> 
</configuration>
```
④ 修改：yarn-site.xml
```
<configuration>
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>localhost</value>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>

    <property>
        <name>yarn.application.classpath</name>
        <value>
            %HADOOP_HOME%\etc\hadoop,
            %HADOOP_HOME%\share\hadoop\common\*,
            %HADOOP_HOME%\share\hadoop\common\lib\*,
            %HADOOP_HOME%\share\hadoop\mapreduce\*,
            %HADOOP_HOME%\share\hadoop\mapreduce\lib\*,
            %HADOOP_HOME%\share\hadoop\hdfs\*,
            %HADOOP_HOME%\share\hadoop\hdfs\lib\*,          
            %HADOOP_HOME%\share\hadoop\yarn\*,
            %HADOOP_HOME%\share\hadoop\yarn\lib\*
        </value>
    </property>
</configuration>
```
hdfs 负责分布式存储，mapreduce 负责分布式计算，yarn 负责资源调度，基本的（伪）分布式环境初步建立

***

## 测试使用

1、格式化 namenode 的 hdfs 目录
`hdfs namenode –format`
注意删除路径 `D:\hadoop\hadoop-3.2.3\data\dfs\` 两个文件夹下面的内容
可能遇到的问题：https://blog.csdn.net/chasonsp/article/details/115349728  
https://blog.csdn.net/weixin_43718641/article/details/117907516  
https://zhuanlan.zhihu.com/p/140389153  

2、启动 hadoop
注意若有 VMware 虚拟机需要先禁用网络
先定位到 sbin 目录 `D:\hadoop\hadoop-3.2.3\sbin`
输入 `start-all.cmd`
这时候会弹出 4 个窗口，输入 `jps` 查看进程情况
浏览器访问 http://localhost:8088/ 查看 hadoop 的启动情况
http://localhost:50070/

3、hdfs 的使用
在路径 `D:\hadoop\hadoop-3.2.3\sbin` 下创建文件夹
`Hadoop fs –mkdir /user` 或者 `hdfs dfs –mkdir /user`
`Hadoop fs –mkdir /user/input`
上传文件
`Hadoop fs –put e:/test.txt /user/input`
查看文件内容
`Hadoop fs –cat /user/input/test.txt`

4、词频计算
`Hadoop jar D:/hadoop/hadoop-3.2.3/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.3.jar wordcount /user/input/ /user/output`
查看运行结果 `Hadoop fs -ls /user/output/` 注意不需要提前创建 output 文件夹
将输出复制到本地 `hdfs dfs -get /user/output 本地路径`

> Windows 修改用户名：
1、打开控制面板，点击用户账户下的更改账户类型，里面可以更改账户名称
2、然后需要修改 User 目录下的用户目录，有些麻烦，要小心注意[^Users文件夹的修改]
3、cmd 输入 netplwiz，双击用户名进行修改，电脑需要重启

5、停止服务
`D:\hadoop\hadoop-3.2.3\sbin\stop-all.cmd`

***

## **遇到的问题**
https://blog.csdn.net/superice_/article/details/102689227
https://jingyan.baidu.com/article/cdddd41cb0d76f53ca00e144.html
``` batch
@echo off

pushd "%~dp0"

dir /b C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum >List.txt

dir /b C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum >>List.txt

for /f %%i in ('findstr /i . List.txt 2^>nul') do dism /online /norestart /add-package:"C:\Windows\servicing\Packages\%%i"

pause
```
https://blog.csdn.net/qq_36470475/article/details/115670312

***

## **参考链接**

https://blog.csdn.net/hawkzy/article/details/83867384
https://blog.csdn.net/luoye4321/article/details/90552674





[^jdk下载]: https://blog.csdn.net/weixin_43252521/article/details/119119646

[^Users文件夹的修改]:https://www.cnblogs.com/Run2948/p/Windows10_User_Name_Folder_Reame.html#:~:text=Windows%2010%20%E4%BF%AE%E6%94%B9%E7%94%A8%E6%88%B7%E5%90%8D%E5%8F%8AUsers%E6%96%87%E4%BB%B6%E5%A4%B9%201.%E4%BF%AE%E6%94%B9%E7%99%BB%E5%BD%95%E8%B4%A6%E6%88%B7%E5%90%8D%20%E6%8E%A7%E5%88%B6%E9%9D%A2%E6%9D%BF%20-%3E,%E7%94%A8%E6%88%B7%E8%B4%A6%E6%88%B7%20-%3E%20%E6%9B%B4%E6%94%B9%E8%B4%A6%E6%88%B7%E5%90%8D%E7%A7%B0%20-%3E%20%E8%BE%93%E5%85%A5%E6%9B%B4%E6%94%B9%E5%8D%B3%E5%8F%AF%202.%E4%BF%AE%E6%94%B9%E7%94%A8%E6%88%B7%E5%90%8D%E6%96%87%E4%BB%B6%E5%A4%B9
