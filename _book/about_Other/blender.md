<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨参考资料</span> 
    </div> 
</div>

https://blog.csdn.net/fruiva/article/details/93123915

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨常用操作</span> 
    </div> 
</div>

鼠标放在区域的四个角上会变成十字，拖动可以快速分割区域  
`Ctrl + 空格键` 最大化当前所在区域  

- 游标  
    一个红白相间的圆圈  
    游标在哪里，新建的物体就在哪里  
    `Shift + 鼠标右键`快速移动游标  
    `Shift + C` 快速重置游标至 **视界中心**  
    游标可以作为物体 **旋转的轴心点**  

- 原点  
    `Alt + G` 快速将物体移动到 **原点** 位置  
    每个物体上面黄色的点，本质上是存储每一个 **物体信息** 的 **数据点**  

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨快捷操作</span> 
    </div> 
</div>

`Shift + A` 新建物体，有唯一一次机会可以更改参数  
点击物体，`Shift + S` 出现目录，选中项，移动物体  
鼠标选中某物体上，`G 键` 移动物体  
鼠标选中某物体上，`S 键` 放缩物体，再按 `Z 键` 在 Z 轴上进行放缩  
`R 键` 控制物体旋转  
`X 键` 删除物体  
`Shift + D` 复制物体  
`/` 可以进入物体内部，查看里面的物体  
`Alt + 鼠标左键` 控制视角  
`滚轮` 放大缩小
F12 进入渲染层级

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨点线面的选择和控制</span> 
    </div> 
</div>

选中模型 `Tab 键` 进入编辑模式（可以修改物体的点线面），再按一次 `Tab 键` 回到物体模式  
Tip：编辑-偏好设置-键位映射-勾选拖动时的饼菜单  

点、线、面的快捷键分别为 `1`、`2`、`3`  
选中一部分点的时候，`ctrl + I` 可以进行反选  
选中一个点，鼠标移动到相邻物体上，按下 `L 键` 相邻物体的四边面的点都能选中，但是注意如果有 **三角面**，则需要移动鼠标到三角面上再按一次 `L 键`  
选中一个点，`Alt + 鼠标左键双击`，会进行 **循环选择**，例如选中球体环绕一圈的点  
`Alt + Z` 透视模式下，框选可以选中物体背部的点  
选择点/线/面，`X 键` 进行删除或者融并，融并不会有缺口  
法向，用于标识平面的正反。打开 **面朝向** 功能，可以清晰的看出正反面，**蓝正红反**。`Shift + N` 将平面向内翻转  
法线，垂直于平面的线，也可以标识面的正反方向  

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨十大建模操作</span> 
    </div> 
</div>

### 挤出并移动 E

点模式的时候可以挤出一个线
线模式可以挤出一个面
面模式可以挤出一个体

Ctrl + 鼠标右键 实现连续的挤出
Ctrl + Z 进行撤回，鼠标右键撤销仅仅是撤销了移动，挤出还在

### 内插（向内挤出） I

与挤出操作是类似的，不过是相反的方向

### 倒角 Ctrl + B

拉出倒角，滑动鼠标滚轮可以增加细分面
使得边更加圆滑

### 循环切割 Ctrl + R

添加循环切割线，滑动鼠标滚轮可以增加切割线的数目
鼠标左键点击后就确定了线的数目，移动至合适位置后再次点击则确定位置

### 合并 M

选择两个点后，按下M，可以选择合并到中心/游标/首远点 等等

### 断开 V

将点从原本位置分离开

### 填充 F

循环选中边后，可以进行面的填充

栅格填充 ctrl + F
栅格填充要求是偶数面

### 切刀 K

实现对物体的切割
点击鼠标右键或者空格键可以退出

### 桥接 Ctrl + E

桥接必须是一个物体才可以进行
做法是shift 选中两个物体，ctrl + j 进行合并
然后循环选中边后进行桥接

### 分离 P

选中物体后，p键 分离选中项

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨常用修改器</span> 
    </div> 
</div>

修改器是非破坏性建模方式，在应用修改器之前都可以随意修改
点击物体后，右侧有个小扳手，点击选中需要的修改器

### 表面细分

表面细分将网格的面分割成更小的面，使其看起来更平滑

### 实体化

给物体增加厚度

### 倒角


---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨辅助工具</span> 
    </div> 
</div>





















---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨示例</span> 
    </div> 
</div>

### 制作蛋糕

shift + a，网格 柱体 作为蛋糕主体
s + z，在z轴上缩放
tab 键 进入编辑模式
ctrl + r 环切柱体




















<style> 
    .note { 
        background-color: #f9f9f9; 
        border: 1px solid #ddd; 
        padding: 10px; 
        border-radius: 10px; 
        display: inline-block; 
        font-weight: bold;
        margin: 10px 0px;
    }
    .note:hover {
        animation: gradient-in 0.5s forwards;
    }
    .note:not(:hover) {
        animation: gradient-out 0.5s forwards;
    }
    @keyframes gradient-in {
        0% {
            background-color: #f9f9f9;
        }
        20% {
            background-color: #f5f5f5;
        }
        100% {
            background-color: #e1e1e1;
        }
    }
    @keyframes gradient-out {
        0% {
            background-color: #e1e1e1;
        }
        80% {
            background-color: #f5f5f5;
        }
        100% {
            background-color: #f9f9f9;
        }
    }
    .title1 { 
        font-size: 24px; 
        /* color: #333;  */
    } 
    .title2 { 
        font-size: 20px; 
        /* color: #555;  */
    } 
    .title3 { 
        font-size: 16px; 
        /* color: #777;  */
    } 
    /* .note:hover [class^="title"]{
        font-size: 30px;
        opacity: 0.6;
    } */
</style>