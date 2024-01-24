# 入门

标签：CSS

---

## **简介**

CSS（Cascading Style Sheets），叠层样式表
文件扩展名：`.css`
作用是：为结构化文档（例如 html）添加样式

- 书写规则
    - 选择器 + 一条或多条声明
    - 选择器是 HTML 元素，声明是属性 : 值组成的，声明之间用分号; 隔开

注释方法：`/* 这里面写注释 */`

***

## **选择器**

注意不要以数字开头

- id 选择器
    假设某个标签里面有元素属性为 id="para1"
    ``` css
    #para1
    {
        property:value;
    }
    ```

- class 选择器
    假设标签 p 里面有属性为 class="center"
    下例中，设置所有包含 class="center" 的 p 标签都为居中
    ``` css
    p.center
    {
        text-align:center;
    }
    ```
    若上述代码中去掉 p，则不限于 p标签，而是所有包含 class="center" 类的 HTML 标签都为居中

***

## **插入样式表的方法**

- 外部样式
    使用 <link> 放在 head 里面
- 内部样式
    使用 <style> 放在 head 里面
- 内联样式
    使用 <link> 放在相应的标签里面
- 多重样式表
    取并集，且优先级为：
    内联样式 Inline style
    v
    内部样式 Internal style sheet
    v
    外部样式 External style sheet
    v
    浏览器默认样式

***

## **常见设置**

- 背景
    ``` css
    body {background-color:#b0c4de;}
    h1 {background-color:#6495ed;}
    p {background-color:#e0ffff;}
    div {background-color:#b0c4de;}
    ```
    还可以设置颜色、图像、位置、是否重复、是否固定或者滚动

- 文本
    ``` css
    body {color:red;} 
    h1 {color:#00ff00;} 
    h2 {color:rgb(255,0,0);}
    ```
    可以设置颜色、对齐方式、设置下划线、大小写转换、缩进、间距行高、阴影

- 字体
    - 通用字体
    sans-serif 的字母末端没有装饰
    Monospace 等宽字符
    - 特定字体
    ``` css
    设置字体系列，如果第一个Times New Roman不支持，则尝试Times，否则使用serif
    p {font-family:"Times New Roman", Times, serif;}
    ```
    还可以设置样式，是否斜体等
    设置字体大小：
    1. 绝对大小
    2. 相对大小
    3. 不设置则默认是普通文本段落16像素=1em
    
    公式：**px/16=em**，建议使用em
    ``` css
    使用百分比和 em 组合
    body {font-size:100%;}
    h1 {font-size:2.5em;}
    h2 {font-size:1.875em;}
    p {font-size:0.875em;}
    ```

- 链接
    ``` css
    a:link {color:#000000;} /* 未访问链接*/ 
    a:visited {color:#00FF00;} /* 已访问链接 */ 
    a:hover {color:#FF00FF;} /* 鼠标移动到链接上 */ 
    a:active {color:#0000FF;} /* 鼠标点击时 */
    注意以上的顺序
    ```
    可以设置链接的文本、颜色、字体、背景颜色等等

- 列表
    ``` css
    设置列表项标记
    ul.a {list-style-type: circle;} 
    ul.b {list-style-type: square;} 
    ol.c {list-style-type: upper-roman;} 
    ol.d {list-style-type: lower-alpha;}
    ```
    注意：无序列表一般设置标记、有序列表设置文本格式
    ``` css
    可以指定某一图像作为无序列表的标记
    ul { list-style-image: url('sqpurple.gif'); }
    ```
    ``` css
    默认情况下列表 <ul> 或 <ol> 还设置了内边距和外边距，可使用 margin:0 和 padding:0 来移除:
    ul { list-style-type: none; margin: 0; padding: 0; }
    ```

- 表格

- 盒子模型
    想象成一个盒子，包括内外边距、里面的内容
    1. margin，外边距
    2. border，盒子（边框）
    3. padding，内边距
    4. content，内容
    
    当指定一个 CSS 元素的宽度和高度属性时，只是设置了内容区域的宽度和高度。完整大小的元素还必须添加内边距，盒子和外边距
    ``` css
    div {
        width: 300px; 
        padding: 25px; 
        border: 25px solid green; 
        margin: 25px; 
    }
    ```

    - 内边距（填充）
        若设置为0，则所释放的区域为元素背景颜色
        同理可以分别指定不同侧面的边距

    - 盒子（边框）
        可以设置样式，如边框颜色、背景颜色、圆角、边数、边的样式、宽度
        ``` css
        border-style: 属性1，属性2，属性3，属性4
        ```
        分别对应上右下左
        若只有三个属性，则是对应上、左右、下
        若只有两个属性，则是对应上下、左右
        若只有一个属性，则均相同

    - 外边距
        没有颜色，完全透明
        可以分别指定不同侧面的边距

    - 轮廓
        元素周围的线，用来突出元素
        可以设置颜色、样式、宽度

- 尺寸
    设置元素的高度和宽度

- 显示与可见性
    - 隐藏且在布局消失
        ``` css
        h1.hidden {display:none;}
        ```
    - 隐藏但是仍占据空间
        ``` css
        h1.hidden {visibility:hidden;}
        ```

***

## **分组和嵌套选择器**

减少相同样式的代码
``` css
h1,h2,p
{ 
color:green; 
}
上述 h1，h2，p 的样式相同
```
``` css
p { color:blue; text-align:center; }    /* 针对所有标签 p */

.marked { background-color:red; }     /* 针对所有含有 class="marked" 的 */

.marked p { color:white; }    /* 针对所有含有 class="marked" 的内部的标签 p */

p.marked{ text-decoration:underline; }    /* 针对所有标签 p 中含有 class="marked" 的 */
```

***

## **块元素（block）和内联元素（inline）**

块元素的前后都自带换行符
例如：`<h1>、<p>、<div>`

内联元素不强制换行
例如：`<span>、<a>`

可以通过 display 更改为块或者内联元素
``` css
li {display:inline;}
span {display:block;}
```

***

## **定位**

常用值包括：static、relative、fixed、absolute、sticky
``` css
无定位
不会受到 top, bottom, left, right影响
div.static { position: static; border: 3px solid #73AD21; }
```
``` css
相对定位
元素的定位是相对其正常位置
h2.pos_left { position: relative; left:-20px; } h2.pos_right { position:relative; left:20px; }
```
``` css
相对于浏览器窗口是固定位置，即使窗口是滚动的它也不会移动
p.pos_fixed { position:fixed; top:30px; right:5px; }
```
``` css
绝对定位
元素的位置相对于最近的已定位父元素，如果元素没有已定位的父元素，那么它的位置相对于<html>
h2 { position:absolute; left:100px; top:150px; }
```
``` css
粘性定位，基于用户的滚动位置来定位
div.sticky { position: -webkit-sticky; /* Safari */ position: sticky; top: 0; background-color: green; border: 2px solid #4CAF50; }
```
`z-index` 指定元素堆叠的顺序，谁前谁后，数值越大越前面

***

## **布局**

当内容溢出元素框时需要设置，设置可见或者滚动条
visible
hidden
scroll
auto
inherit

***

## **浮动**

一般用于图像，也可用于布局
``` css
img { float:right; }
```
图像浮动到右边，文本环绕在它左边
几个浮动的元素放在一起，它们会彼此相邻，可以设置边距
可以对文本使用 clear 属性，指定其两侧不能出现浮动元素

***

## **水平&垂直对齐**

元素居中对齐
``` css
.center { margin: auto; width: 50%; border: 3px solid green; padding: 10px; }
如果没有设置 width 属性(或者设置 100%)，居中对齐将不起作用
```
文本居中对齐
``` css
.center { text-align: center; border: 3px solid green; }
```
图片居中对齐
``` css
img { display: block; margin: auto; width: 40%; }
```
还有左右对齐、垂直居中等等

***

## **组合选择符**

后代选择器（以空格     分隔），选出所有后代
子元素选择器（以大于 > 号分隔），选出所有的直接后代，就是没有再套一层东西
相邻兄弟选择器（以加号 + 分隔），选出往后的一个相邻兄弟标签
普通兄弟选择器（以波浪号 ～ 分隔），选出往后的所有兄弟标签
详见菜鸟教程上的示例

***

## **伪类（Pseudo-classes）和伪元素**

用来添加一些选择器的特殊效果
使用 :first-child 伪类来选择父元素的第一个子元素
使用 :lang 伪类定义特殊的规则
``` css
q:lang(no) {quotes: "~" "~";}
为属性值为 no 的q元素定义引号的类型
```
还有许多的伪类可以使用，例如可以用于：表单元素，选择第几个元素，在哪里插入内容等等

伪元素动态性比伪类要低得多。实际上，设计伪元素的目的就是去选取诸如元素内容第一个字（母）、第一行，选取某些内容前面或后面这种普通的选择器无法完成的工作。它本身只是基于元素的抽象，并不存在于文档中，所以叫伪元素。

***

## **各种功能**

- 导航栏

- 下拉菜单栏

- 图片廊

- 图像的各种技术
透明、拼接

- 媒体类型
    指定文件在不同媒体呈现样式
    @media 规则
    规则包括screen、print、all、tv等等

- 表单设置

***

## **属性选择器**

IE6和更低的版本不支持属性选择器
~=, |=, *= , ^=, $= 的区别：
``` css
[attribute~=value]    /* 要求独立完整的 value */

[attribute|=value]    /* 要求以 value 开头，且完整或者按照 - 分割开的 */

[attribute*=value]    /* 只要能拆出 value 就行 */

[attribute^=value]    /* 要求以 value 开头，会自动拆分 */

[attribute$=value]    /* 要求以 value 结尾 */
```

***

## **计数器**

使用 ::before 和 ::after 伪元素来插入自动生成的内容

***

## **网页布局**

头部区域、菜单导航区域、内容区域、底部区域

***

## **!important 规则**

用于增加样式的权重
使用 !important 是一个坏习惯，**应该尽量避免**，因为这破坏了样式表中的固有的级联规则，使得调试找 bug 变得更加困难了
只有在需要覆盖全站或外部 CSS 的特定页面中使用 !important

***

## **css3 的响应式 Web 设计**

利用 `min-device-width: ？px`，对不同设备分别进行设计

- 设置 Viewport
    一个常用的针对移动网页优化过的页面的 viewport meta 标签大致如下
    ``` html
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    ```
    方便移动端访问查看

- 网格视图
    很多网页都是基于网格设计的，这说明网页是按列来布局的
    使用网格视图有助于我们设计网页，使得添加元素变的更简单
    响应式网格视图通常是 12 列，宽度为100%，在浏览器窗口大小调整时会自动伸缩
    ``` css
    确保所有的 HTML 元素都有 box-sizing 属性且设置为 border-box
    确保边距和边框包含在元素的宽度和高度间
    * {
        box-sizing: border-box;
    }
    .col-1 {width: 8.33%;}
    .col-2 {width: 16.66%;}
    .col-3 {width: 25%;}
    .col-4 {width: 33.33%;}
    .col-5 {width: 41.66%;}
    .col-6 {width: 50%;}
    .col-7 {width: 58.33%;}
    .col-8 {width: 66.66%;}
    .col-9 {width: 75%;}
    .col-10 {width: 83.33%;}
    .col-11 {width: 91.66%;}
    .col-12 {width: 100%;}
    ```

- 图片
    ``` css
    img {    max-width: 100%;    height: auto;}
    图片会根据上下范围实现响应式功能，且不会超过原始大小
    ```
    ``` css
    div {    
        width: 100%;    
        height: 400px;    
        background-image: url('img_flowers.jpg');    
        background-repeat: no-repeat;    
        background-size: contain;    
        border: 1px solid red;
    }
    background-size 属性设置为 "contain", 背景图片将按比例自适应内容区域
    
    如果 background-size 属性设置为 "100% 100%" ，背景图片将延展覆盖整个区域
    
    如果 background-size 属性设置为 "cover"，虽然全覆盖了，但是背景图像的某些部分无法显示在背景定位区域中
    ```

- 视频同上

- 框架
    响应式 Web 设计框架 Bootstrap
    ``` html
    <head>
        <title>Bootstrap Example</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1"> 
         <link rel="stylesheet" href="http://apps.bdimg.com/libs/bootstrap/3.3.4/css/bootstrap.min.css">
        <script src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
        <script src="http://apps.bdimg.com/libs/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    </head>
    ```