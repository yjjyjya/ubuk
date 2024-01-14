# *基本知识*

Docker 是一种容器化技术，可以 **将应用程序及其依赖项打包成一个独立的容器**，是一个开源的软件部署解决方案  
Docker 本身是跨平台的，可以在 Linux、Windows 和 macOS 等操作系统上运行  
但是，使用 Docker 部署的项目需要基于 Linux 系统。这是因为 Docker 容器是 **基于 Linux 内核的虚拟化技术**，它利用了 **Linux的命名空间和控制组** 等特性来实现隔离和资源管理  
因此，如果使用 Docker 来打包和部署项目只能在 Linux 系统上运行  

- 镜像、容器、仓库  
    仓库中集中存放各种镜像文件  
    有镜像才能创建对应的容器  
    需要在容器中运行代码  

Docker 简化了运维工程师的工作，进行集群部署的时候就不需要一台一台地安装所需的环境  
Docker 部署只需要创建一个镜像，安装好环境，再复制到集群的各个机器上，**快捷并且保证了部署的一致性**  


# *使用 Docker 的好处*

手动部署项目的时候我们通常会先把代码上传到服务器、然后安装相关依赖、配置环境、最后启动项目。通常这些过程都需要我们手动敲入命令，每次部署的时候都需要重新敲一遍  
而 docker 做的工作就是将这些 **命令记录下来**，在部署的时候再逐个执行  
上述过程与自己写个部署脚本没有什么区别  
但是 docker 还能够保证每次运行的 **环境都是一致的**，并且 **与宿主机的环境进行隔离**  




# *Windows 下载安装*

https://docs.docker.com/desktop/install/windows-install/  


# *Dockerfile 怎么写？*

docker 会根据 Dockerfile 来构建环境并生成一个 **镜像**，最后通过运行镜像来完成项目部署  
  
1、FROM  
FROM 用来指定基础镜像。可以理解为所需要的的操作系统  
```
# 比如下面这行代码就指定了带有 python 环境的镜像
# 我们可以在构建好的镜像中直接使用 python 而不需要额外安装
FROM python:3.6
```

2、MAINTAINER  
```
# 指定了 Dockerfile 的作者，或者说维护者
# 可填可不填
MAINTAINER yourname
```

3、ENV  
```
# 用来设置环境变量
ENV PRODUCTION_ENV 1
```

4、ADD  
用来向镜像中添加我们需要的文件，比如配置文件、代码、资源文件等等  
```
ADD ./database.ini /root    #路径是 Dockerfile 所在目录的相对路径
ADD ./src /root
ADD http://www.baidu.com /root    #路径也可以使用 URL
ADD code.tar /root    #tar 压缩包的话会被自动解压成目录
```

5、COPY  
COPY 的功能和 ADD 相似  
不过 COPY 不能用 URL 只能复制本地的文件到镜像中，并且不会自动解压 tar 压缩包  

6、EXPOSE  
声明容器中要使用的端口，仅仅做声明，没有实际作用  
```
EXPOSE 80
EXPOSE 80 8080
```

7、ENTRYPOINT  
**容器启动** 时执行的命令，并且不会被 docker run 的参数覆盖  
如果指定了多个 ENTRYPOINT 只有最后一个会被执行  
```
ENTRYPOINT ["可执行文件", "参数1", "参数2"]
ENTRYPOINT 命令 参数1 参数2
```

8、WORKDIR  
指定工作目录，后续的所有命令都会在这个目录下面执行  

9、RUN  
RUN 表示要执行的命令  
```
WORKDIR /root/project
RUN pip isntall -r requirements.txt    #安装依赖
```

10、VOLUME  
声明容器中的挂载点，在运行的时候通过 -v 绑定到宿主机目录，注意需要提供完整的目录路径  


# *实践*

先来创建一个项目，目录结构如下  
```
httpServer/
│  log/
│  http.py
└─ Dockerfile
```

## 编写 Dockerfile

```
# 指定带有 python 3.6 环境的镜像
FROM python:3.6
# 作者
MAINTAINER geebos
# 将当前目录所有文件添加到要构建的镜像中
COPY . /root/httpServer
# 声明容器中的 /root/httpServer/log 目录为挂载点
VOLUME /root/httpServer/log
# 设置工作目录
WORKDIR /root/httpServer
# 绑定端口
EXPOSE 8000
# 设置启动命令
ENTRYPOINT python http.py
```

## 构建镜像

首先运行 `docker build -t http-server:1.0 .` 构建镜像  
其中 `-t http-server:1.0` 指定了镜像的名字和版本号为 `http-server:1.0`  

然后运行  
```
docker run -id -v d:/dockerTest/httpServer/log:/root/httpServer/log \
-p 8000:8000 --name http-server-container http-server:1.0
```
来启动容器，其中：  
`-d` 表示后台启动  
`-v d:/dockerTest/httpServer/log:/root/httpServer/log` 绑定挂载目录  
`-p 8000:8000` 指定端口映射  
`--name http-server-container` 指定容器的名称为 `http-server-container`  

启动之后我们可以访问 `http://127.0.0.1:8000`  
访问之后查看 `d:/dockerTest/httpServer/log/log.txt` 中会发现我们的请求记录被保存到宿主机上了  

可以使用 `docker exec -it http-server-container /bin/bash` 进入到容器内部  

##  常用 docker 命令

```
在镜像之上启动容器  
docker build：构建镜像
常用格式：docker build -t 镜像名 Dockerfile所在路径
示例：dcoker build -t image-name .

docker run：基于镜像启动容器
常用格式：docker run -id -t --name 容器名 镜像名/镜像ID
示例：docker run -id -t --name container-name image-name

docker ps：显示所有容器信息

docker stop：停止容器运行

docker start：重新运行一个已停止的容器

docker rm：删除容器，删除之前要先确保容器已经停止运行。可以指定多个容器
示例：docker rm container-name

docker images：显示所有镜像信息

docker rmi：删除镜像，删除之前要确保没有基于该镜像的容器存在。可以指定多个镜像
示例：docker rmi image-name/image-id

docker exec：在容器中执行命令
示例：docker exec -it container-name /bin/bash。这命令可以启动容器内的 bash
```


# *参考资料*

https://zhuanlan.zhihu.com/p/385852508  
https://docker-practice.github.io/zh-cn/install/ubuntu.html  








