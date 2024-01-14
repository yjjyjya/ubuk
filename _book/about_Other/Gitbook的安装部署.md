# 参考资料

部署教程：https://www.mapull.com/gitbook/comscore/  
使用指南：https://zha0cai.github.io/gitbookPublic/gitbook-guide/  
关于插件：https://blog.csdn.net/qq_43514847/article/details/86598399  
关于公式：https://blog.csdn.net/qq_42898299/article/details/106779945  
http://www.zhaowenyu.com/gitbook-doc/default-files/book-json.html  
部署：https://dvel.me/posts/deploy-blog-in-cloudflare-pages/  

# 安装 nodejs

下载地址：https://nodejs.org/en/download/releases  
安装配置指南：https://blog.csdn.net/zhouyan8603/article/details/109039732  

> 卸载 nodejs  
`C:\ProgramData\Microsoft\Windows\Start Menu\Programs` 找到 nodejs，进行 uninstall  
删除对应目录下的文件  
删除 c 盘用户下的缓存  
删除环境变量  


# 简单配置

查看版本  
`node -v` `npm -v`  

将缓存和仓库建在其他盘，比如 d 盘  
需要在 node.exe 所在目录下创建文件夹 node_global 和 node_cache  
再执行  
`npm config set prefix "D:\nodejs\node_global"` 和 `npm config set cache "D:\nodejs\node_cache"`  

配置镜像网站  
`npm config set registry=http://registry.npm.taobao.org`  

配置环境变量  
增加 NODE_PATH 变量 `D:\nodejs\node_global\node_modules`  
在 path 中添加如下两条 `D:\nodejs` `D:\nodejs\node_global`  

查看所有配置信息  
`npm config list`  

测试  
`npm install vue -g` 将包下载到 global 全局目录中  


# 安装 gitbook

推荐下载 10 或者 11 版本的 nodejs  

`gitbook init` 可能会出现的问题：  
https://www.cnblogs.com/eternalnight/p/15192585.html  
https://blog.csdn.net/qq_30033537/article/details/113738575  
一般来说都是没问题的，可能下载需要等待较长一段时间  


# 部署 gitbook

可以使用以下平台：  
1、Gitee pages  
2、glitch.me  
3、GitHub pages  
4、cloudflare：https://dash.cloudflare.com/2e55d48f8306baee004a3e7e40f5a8e9/pages/new/provider/github  
&emsp;&emsp;mymail_yjj@qq.com 12345678@

先切换路径到：D:\mybook_ubuk 执行：  
`gitbook init`        //初始化，时间可能比较久  
`gitbook install`    //用于安装插件  
`gitbook build --log=debug`  
`gitbook serve`  

遇到的问题  
https://blog.csdn.net/K_Lily/article/details/105291511  
修改文件 `C:\Users\magicclannad\.gitbook\versions\3.2.3\lib\output\website\copyPluginAssets.js`  
之后以管理员身份重启 cmd 进行 build  
.gitignore 放在哪里，对应的里面路径就是哪里，不要管 book.json 中的 root  

可能使用到的插件  
这里手动下载：https://www.npmjs.com/  
``` json 
"plugins": [
    "splitter",  
    "favicon",
    "insert-logo",
    "code",
    "-lunr", "-search", "search-pro",
    "back-to-top-button",
    "mathjax-pro",
    "auto-scroll-table",
    "popup",
    "tbfed-pagefooter",
    "flexible-alerts",
    "accordion",
    "zymplayer" 
],
```
在 book.json 中添加以上内容  
然后执行 `gitbook install`，或者使用 NPM 安装，例如 `npm install gitbook-plugin-page-treeview`，也可以从源码 GitHub 地址中下载，放到 node_modules 文件夹里  

推送到 gitee  
`git remote -v`  
`git remote remove origin`  
`git remote add origin https://gitee.com/？？？/ubuk.git`  
`git add .`  
`git commit -m "？？？"`  
`git push -u origin main`  

> 关于 git 推送的文件忽略  
先修改 .gitignore 中的内容，再执行 `git rm -r -f --cached .`  
之后重新提交、推送即可  

