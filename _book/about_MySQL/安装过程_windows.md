# MySQL 5.7 安装

标签：安装过程记录

---

- 下载
    下载地址：https://mirrors.tuna.tsinghua.edu.cn/mysql/downloads/MySQL-5.7/
    在浏览器页面 按下 `Ctrl + F`，寻找关键词“win”，下载后缀为 zip 的压缩包
    自行选择解压路径

- my.ini 文件
    在解压路径下新建 my.ini 文件，内容如下：
    ``` MySQL
    [mysql]
    # 设置 MySQL 客户端默认字符集
    default-character-set=utf8
     
    [mysqld]
    # 设置 3306 端口
    port = 3306
    
    # 设置 MySQL 的安装目录
    basedir=$自己的解压路径$
    
    # 设置 MySQL 数据库的数据的存放目录（MySQL8.0+ 不需要以下配置，系统自己生成即可，否则有可能报错）
    datadir=$自己的解压路径$\data
    
    # 允许最大连接数
    max_connections=20
    
    # 服务端使用的字符集默认为8比特编码的latin1字符集
    character-set-server=utf8
    
    # 创建新表时将使用的默认存储引擎
    default-storage-engine=INNODB
    ```

- 设置密码
    打开 CMD，输入 `mysql -u root -p`
    默认无密码，直接回车
    ``` MySQL
    use mysql;    #切换到 MySQL 数据库
    
    update user set authentication_string=password('123456') where user='root';    #设置 root 用户的密码为 123456
    
    flush privileges;    #刷新 MySQL 的系统权限相关表
    ```

- 设置远程连接
    打开 CMD，输入 `mysql -u root -p`
    注意这次要输入新密码
    ``` MySQL
    use mysql;    #切换到 MySQL 数据库
    
    GRANT ALL ON *.* TO user@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;    #设置 user 用户远程访问
    
    flush privileges;    #刷新 MySQL 的系统权限相关表
    ```

***

## 参考资料
[MySQL 5.7 安装教程](https://www.cnblogs.com/swjian/p/11907600.html)
