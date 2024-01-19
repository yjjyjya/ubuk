切换路径到：D:\mybook_ubuk  


### *执行*  

gitbook init    //gitbook一些初始化，时间可能比较久  
gitbook install    //用于安装插件  
gitbook build --log=debug  
gitbook serve  


### *遇到的问题*  

https://blog.csdn.net/K_Lily/article/details/105291511  
C:\Users\magicclannad\.gitbook\versions\3.2.3\lib\output\website\copyPluginAssets.js  
修改完后以管理员身份重启cmd进行build  
.gitignore放在哪里，对应的里面路径就是哪里，不要管book.json中的root  

关于公式：https://blog.csdn.net/qq_42898299/article/details/106779945  


### *使用的插件*  

https://blog.csdn.net/qq_43514847/article/details/86598399  
在book.json中添加以下内容。然后执行gitbook install，或者使用NPM安装npm install   gitbook-plugin-page-treeview，也可以从源码GitHub地址中下载，放到node_modules文件夹里（GitHub地址在进入插件地址右侧的GitHub链接）  

"anchor-navigation-ex"
"flexible-alerts"
"back-to-top-button",  
"code",  
"splitter", 
"popup", 
"-lunr",  
"-search",  
"search-pro",  
"page-treeview",  
"zymplayer"  
"-highlight",
"prism",



### *推送到 gitee*  

gitbook在build的时候需要把.gitignore 文件中的 docs/ 注释掉
提交到远程仓库的时候再取消注释，只需要提交_book文件夹即可

在gitee page服务中，需要在book.json的路径中使用绝对路径，assets/music/musicList.json文件中也同理

步骤：
本地进行build，注意一些可能不能出现的内容需要忽略掉
先修改.gitignore 内容，执行
git rm -r -f --cached .
git remote -v  
git remote remove origin  
git remote add origin https://gitee.com/gitee_tjhd/ubuk.git  
<!-- https://github.com/yjjyjya/ubuk.git -->
git add .  
git commit -m "......"  
git push -u origin main  


### *其他*

<div id="pic1" class="img_container" style="margin: 0px auto 20px auto; width: 100%; height: auto;">
    <img src=".png" style="display: block; box-shadow: 2px 0px 10px rgba(0, 0, 0, 0.5);">
</div>


### *参考资料*  

https://zha0cai.github.io/gitbookPublic/gitbook-guide/  
https://blog.csdn.net/baidu_33146219/article/details/125460234