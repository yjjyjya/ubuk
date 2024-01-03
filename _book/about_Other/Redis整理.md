# *基本命令*

## 启动服务端和客户端

`redis-server --service-start`  
`redis-cli -h 127.0.0.1 -p 6379`  

## 关闭客户端

`redis-server --service-stop`  

## 字符串

`set mykey helloworld`  
`get mykey`  
`getrange mykey 0 5`  
`type mykey`  
`getset mykey 23333`  
`del mykey`  

## 哈希

`hmset mysite name "tjhd" url "https://tjhd.com" visitors 10`  
`hkeys mysite`  
`hlen mysite`  
`hget mysite name`  
`hgetall mysite`  
`hexists mysite visitors`  
`hset mysite visitors 100`  
`hdel mysite visitors`  
`hsetnx mysite visitors 100`  

## 列表

`lpush mylist sql`  
`lpush mylist mysql`  
`lpush mylist postgresql`  
`lrange mylist 0 10`  
`llen mylist`  
`lset mylist 0 sqlserver`  

## 集合

元素都是唯一的  
`sadd myset mongodb`  
`sadd myset db2`  
`sadd myset db1`  
`smembers myset`  
`scard myset` 获取集合的成员数  

## 有序集合

`zadd mysortedset 1 qingtong`  
`zadd mysortedset 2 baiyin`  
`zadd mysortedset 3 huangjin`  
`zadd mysortedset 4 bojin`  
`zadd mysortedset 5 zhuanshi`  
`zrange mysortedset 0 10 withscores`  
`zrem mysortedset qingtong`  
`zrange mysortedset 0 10 withscores`  
`zcard mysortedset`  
`zrank mysortedset zhuanshi`  

## HyperLogLog

比如数据集 {1, 3, 5, 7, 5, 7, 8}， 那么这个数据集的基数集为 {1, 3, 5 ,7, 8}, 基数(不重复元素)为5  
基数估计就是在误差可接受的范围内，快速计算基数  
`pfadd myhll redis`  
`pfadd myhll redis`  
`pfadd myhll mongodb`  
`pfadd myhll mysql`  
`pfcount myhll`  

## 发布订阅

发送者（在Redis术语中称为发布者）发送消息，而接收者（订阅者）接收消息  
需要开启两个客户端  

- 第一个作为接收者：  
    `subscribe mychannel`  

- 第二个作为发布者：  
    `publish mychannel "test"`  
    `publish mychannel "hello world"`  
    `publish mychannel "thank you"`  

## 事务

MULTI 用来组装一个事务  
EXEC 用来执行一个事务  
DISCARD 用来取消一个事务  
WATCH 用来监视一些 key，一旦这些 key 在事务执行之前被改变，则取消事务的执行  
将一系列的语句放入缓存队列中，然后一起执行  


# *面试题*

https://redis.com.cn/redis-interview-questions.html

- 什么是Redis？  
    Redis(Remote Dictionary Server)是一个开源的使用 ANSI C 语言编写、遵守 BSD 协议、支持网络、可基于内存亦可持久化的日志型、Key-Value 数据库，并提供多种语言的 API 的 **非关系型数据库**  
    
    传统数据库遵循 ACID 规则。而 Nosql（Not Only SQL 的缩写，是对不同于传统的关系型数据库的数据库管理系统的统称） 一般为分布式，而分布式一般遵循 CAP 定理  
    
- Redis支持的数据类型  
    Redis 可以存储键和不同类型的值之间的映射。键的类型只能为字符串，值常见有五种数据类型：字符串、列表、集合、散列表、有序集合  

- 什么是Redis持久化？Redis有哪几种持久化方式？优缺点是什么？  
    持久化就是 **把内存的数据写到磁盘中去，防止服务宕机了内存数据丢失**  
    Redis 提供了两种持久化方式:RDB（默认） 和AOF  
    
    - RDB：  
        rdb是Redis DataBase缩写  
        本质是内存和磁盘交互  
        功能核心函数rdbSave(生成RDB文件)和rdbLoad（从文件加载内存）两个函数  
    
    - AOF:  
        Aof是Append-only file缩写  
        本质是服务端和磁盘交互  
        每当执行服务器(定时)任务或者函数时flushAppendOnlyFile 函数都会被调用， 这个函数执行以下两个工作  
        aof写入保存：  
        WRITE：根据条件，将 aof_buf 中的缓存写入到 AOF 文件  
        SAVE：根据条件，调用 fsync 或 fdatasync 函数，将 AOF 文件保存到磁盘中  

- 用途  
    Redis 的数据是存在内存中的，所以读写速度非常快，因此 redis 被广泛应用于缓存，每秒可以处理超过 10 万次读写操作，是已知性能最快的 Key-Value 数据库  
    **计数器** 可以对 String 进行自增自减运算，从而实现计数器功能。Redis 这种内存型数据库的读写性能非常高，很适合存储频繁读写的计数量  
    **缓存** 将热点数据放到内存中，设置内存的最大使用量以及淘汰策略来保证缓存的命中率  
    **会话缓存** 可以使用 Redis 来统一存储多台应用服务器的会话信息  
    **全页缓存（FPC）** 除基本的会话 token 之外，Redis 还提供很简便的 FPC 平台。以 Magento 为例，Magento 提供一个插件来使用 Redis 作为全页缓存后端。此外，对 WordPress 的用户来说，Pantheon 有一个非常好的插件 wp-redis，这个插件能帮助你以最快速度加载你曾浏览过的页面  
    **查找表** 例如 DNS 记录就很适合使用 Redis 进行存储。查找表和缓存类似，也是利用了Redis快速的查找特性。但是查找表的内容不能失效，而缓存的内容可以失效，因为缓存不作为可靠的数据来源  
    **分布式锁实现** 在分布式场景下，无法使用单机环境下的锁来对多个节点上的进程进行同步。可以使用 Redis 自带的 SETNX 命令实现分布式锁，除此之外，还可以使用官方提供的 RedLock 分布式锁实现  
    **其它** Set 可以实现交集、并集等操作，从而实现共同好友等功能。ZSet可以实现有序性操作，从而实现排行榜等功能  

