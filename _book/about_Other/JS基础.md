# *基础知识*

## 为什么学习 JavaScript?

HTML 定义了网页的内容  
CSS 描述了网页的布局  
JavaScript 控制了网页的行为  
JS 可以配合 HTML 和 CSS 一起工作  

## 简介

是脚本语言  
轻量级的编程语言  
可插入 HTML 页面  

## 用法

Javascript 脚本代码可被放置在 HTML 页面的 `<body>` 和 `<head>` 部分中，要求位于 `<script>` 与 `</script>` 标签之间  
但是若要外部引用脚本，则将 `<script src="？？？.js"></script>` 放在 `<head>` 内即可  

## 输出

JavaScript 没有任何打印或者输出的函数，数据只能通过以下方式显示：  
1、使用 window.alert() 弹出警告框  
2、使用 document.write() 方法将内容写到 HTML 文档中  
3、使用 innerHTML 写入到 HTML 元素  
4、使用 console.log() 写入到浏览器的控制台  

## 语法

- 字面量  
    即固定值  
- 变量  
    用于存储数据值，用关键字 `var` 来声明变量  
    可以在声明的同时赋值，也可以之后再赋值  
- 操作符  
    例如 `=  +  -  *  /  ==  !=  <  >` 等
- 语句  
    用于向浏览器发出命令，语句用分号分隔（不过用分号来结束语句是可选的）  
- 关键字  
    JavaScript 有一些保留的关键字，例如 `if else float try` 等等  
- 注释  
    单行注释 `//`，多行注释 `/**/`  
- 数据类型  
    数字，表达式，字符串，数组，对象（类似于 Python 字典）等等  
    字符串可以使用 **单引号或双引号**  
- 函数  
- 字母大小写  
    JavaScript 对大小写敏感  
- 字符集  
    JavaScript 使用 Unicode 字符集  

## 数据类型

值类型(基本类型)  
字符串（String）、数字(Number)、布尔(Boolean)、空（Null）、未定义（Undefined）、Symbol（表示独一无二的值）  

引用数据类型（对象类型）  
对象(Object)、数组(Array)、函数(Function)，还有两个特殊的对象：正则（RegExp）和日期（Date）  

JavaScript 同 Python 一样拥有动态类型
``` js
var x;              // x 为 undefined
var x = 5;          // 现在 x 为数字
var x = "John";     // 现在 x 为字符串
```
查看数据类型  
``` js
var x = "John";
typeof x            // 返回 string
```

- JavaScript 数组  
    创建名为 cars 的数组  
    ``` js
    var cars = new Array();
    cars[0] = "Saab";    //注意下标从 0 开始
    cars[1] = "Volvo";
    cars[2] = "BMW";
    ```
    
    或者 (condensed array)
    ``` js
    var cars = new Array("Saab","Volvo","BMW");
    ```
    
    或者 (literal array)
    ``` js
    var cars = ["Saab","Volvo","BMW"];
    ```

Undefined 表示变量不含有值  
可以通过将变量的值设置为 `null` 来清空变量  
当声明新变量时，可以使用关键词 `new`  

- JavaScript 对象  
    是拥有属性和方法的数据  
        
    ``` js
    var person = {
        firstName:"John",
        lastName:"Doe",
        age:50,
        eyeColor:"blue"
    };


    // 访问对象属性
    // 实例 1
    person.lastName;
    // 实例 2
    person["lastName"];
    ```

## 函数

函数就是包裹在花括号中的代码块  
使用关键词 function 且必须是 **小写**  
``` js
function myfunction(var1, var2)
{
    // 代码
}

// 调用
myfunction(arg1, arg2)
```

- 局部 JavaScript 变量  
在 JavaScript 函数内部声明的变量（使用 var）是局部变量，所以只能在函数内部访问它  
只要函数运行完毕，局部变量就会被删除  

- 全局 JavaScript 变量  
在函数外声明的变量是全局变量，网页上的所有脚本和函数都能访问它

如果给尚未声明的变量值赋，该变量将被自动作为 window 的一个属性  
可以通过 `window.属性名` 访问  
非严格模式下给未声明变量赋值创建的全局变量是可以删除的？？？  

## 作用域

作用域是可访问变量的集合  
在 JavaScript 中, 对象和函数同样也是变量  

- 变量生命周期  
    在它声明时初始化  
    局部变量在函数执行完毕后销毁  
    全局变量在页面关闭后销毁  

- 优先度  
    局部变量 > 全局变量 > window变量  

## 事件

HTML 事件是发生在 HTML 元素上的事情  
当在 HTML 页面中使用 JavaScript 时， JavaScript 可以触发这些事件  

常见的 HTML 事件  

| 事件 | 描述 |
| --- | --- |
| onchange | HTML 元素改变 |
| onclick | 用户点击 HTML 元素 |
| onmouseover | 鼠标指针移动到指定的元素上时发生 |
| onmouseout | 用户从一个 HTML 元素上移开鼠标时发生 |
| onkeydown | 用户按下键盘按键 |
| onload | 浏览器已完成页面的加载 |

## 字符串

使用内置属性 length 来计算字符串的长度
``` js
var txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var sln = txt.length;
```
字符串可以是对象
``` js
var x = "John"
typeof x    //返回 String 类型

// 使用 new 关键字将字符串定义为一个对象
var y = new String("John")
typeof y    //返回 Object 类型
```
注意最好不要创建 String 对象，它会拖慢执行速度，并可能产生其他副作用  
> `===` 为绝对相等，即数据类型与值都必须相等  

字符串有相应的属性和方法  
常见的有获取长度、返回指定位置的字符、连接字符、正则表达式匹配、切片、大小写转换、去除空白字符等等  

## 运算符

和 C 语言类似  
包括算术运算符、赋值运算符、比较运算符、逻辑运算符、条件运算符  
注意：如果把数字与字符串相加，结果将成为字符串  

- 条件运算符  
    ``` js
    variablename = (condition)?value1:value2 
    ```
    若满足括号里面的条件condition，则将value1赋值给变量，反之，用value2赋值  

## 条件语句

``` js
if (条件1)
{
    当条件 1 为 true 时执行的代码
}
else if (条件2)
{
    当条件 2 为 true 时执行的代码
}
else
{
  当条件 1 和 条件 2 都不为 true 时执行的代码
}
```

## switch 语句

``` js
function myFunction()
{
	var x;
	var d = new Date().getDay();     //获取今天的日期
	switch (d)
    {
  		case 6:x="今天是星期六";
    	break;
  		case 0:x="今天是星期日";
    	break;
  		default:
    	x="期待周末";    //如果匹配不到，则输出default的值
  	}
	document.getElementById("demo").innerHTML=x;
}
```

## for 语句

``` js
for (var i=0; i<5; i++)
{
    x = x + "该数字为 " + i + "<br>";
}
```

``` js
var person = {fname:"Bill",lname:"Gates",age:56}; 

for (x in person)  // x 为属性名
{
    txt = txt + person[x];
}
```

## while 语句

``` js
while (条件)
{
    满足条件则执行的代码
}
```

``` js
do
{
    需要执行的代码
}
while (条件);    //也是一样，满足条件才继续循环
```

## break、continue 语句

类似 C 语言  
特殊用法：有了 **标签**，可以使用 break 和 continue 在多层循环的时候控制外层循环  
``` js
outerloop:
for (var i = 0; i < 10; i++)
{
    innerloop:
    for (var j = 0; j < 10; j++)
    {
        if (j > 3)
        {
            break;
        }
        if (i == 2)
        {
            break innerloop;
        }
        if (i == 4)
        {
            break outerloop;
        }
        document.write("i=" + i + " j=" + j + "");
    }
}
// 方便控制跳出内层/外层循环
```

## 数据类型

在 JavaScript 中，数组是一种特殊的对象类型。 因此 `typeof [1,2,3,4]` 返回 object  
在 JavaScript 中 null 表示 "什么都没有"，是只有一个值的特殊类型。表示一个空对象引用  
在 JavaScript 中，undefined 是一个没有设置值的变量  
``` js
var x = null;
typeof x;    //输出 object
```
``` js
var y;
typeof y;    //输出 undefined
```
``` js
null === undefined    //输出 false，值相同，类型不同
null == undefined    //输出 true
```
> null 和 undefined 的值相等，但类型不等  
可以设置为 null 或者 undefined 来清空对象  
数据类型之间可以进行转换  

## 正则表达式

``` js
var patt = /hello/i
```
其中 /hello/i 是一个正则表达式  
hello 是一个正则表达式主体 (用于检索)  
i 是一个修饰符 (搜索不区分大小写)  

| 修饰符 | 描述 |
| :---: | :---: |
| i | 对大小写不敏感 |
| g | 全局匹配（查找所有匹配而非在找到第一个匹配后停止），贪心？？？ |
| m | 多行匹配 |

``` js
var str = "Hello World!"; 
var n = str.search(/hello/i);    //输出结果为 0
var txt = str.replace(/world/i, "你好");    //进行字符替换
```
此外还有  
test() 方法用于检测一个字符串是否匹配某个模式，如果字符串中含有匹配的文本，则返回 true，否则返回 false  
exec() 方法用于检索字符串中的正则表达式的匹配  

## 错误

``` js
try {
    ...    //异常的抛出
} catch(e) {
    ...    //异常的捕获与处理
} finally {
    ...    //结束处理，不管是否出现异常都要执行
}
```

## this

在 JavaScript 中 this 不是固定不变的，它会随着执行环境的改变而改变  
    在方法中，this 表示该方法所属的对象  
    如果单独使用，this 表示全局对象  
    在函数中，this 表示全局对象  
    在函数中，在严格模式下，this 是未定义的(undefined)  
    在事件中，this 表示接收事件的元素  

``` js
var person1 = {
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }    //不需要设置参数
}
var person2 = {
  firstName:"John",
  lastName: "Doe",
}
person1.fullName.call(person2);  // 返回 "John Doe"
```

## let、const

- 变量作用域
    - 全局的：在函数外声明的变量
    - 局部的：在函数内声明的变量

let 在 {} 内声明的变量只在其内有效，在 **{} 之外不能访问**  
let 无法实现变量提升  
const 用于声明一个或多个常量，声明时 **必须进行初始化**  
使用 const 定义的对象或者数组，可以对其内部的元素进行 **修改**  

## JSON

JavaScript Object Notation，是用于存储和传输数据的格式，通常用于 **服务端向网页传递数据**  

- JSON 语法规则  
    数据为 键/值 对  
    数据由逗号分隔  
    大括号保存对象  
    方括号保存数组  

``` js
var text = '{ "sites" : [' +
    '{ "name":"Runoob" , "url":"www.runoob.com" },' +
    '{ "name":"Google" , "url":"www.google.com" },' +
    '{ "name":"Taobao" , "url":"www.taobao.com" } ]}';
    
obj = JSON.parse(text);
document.getElementById("demo").innerHTML = obj.sites[1].name + " " + obj.sites[1].url;
```
`JSON.parse()`，用于将一个 JSON 字符串转换为 JavaScript 对象  
`JSON.stringify()`，用于将 JavaScript 值转换为 JSON 字符串  

## void

void 关键字，不返回任何值，但是括号内的表达式还是要运行
如 `void(alert("Warnning!"))`

- `href="#"` 与 `href="javascript:void(0)"` 的区别  
    `#` 包含了一个位置信息，默认的锚是 `#top` 也就是网页的上端  
    而 `javascript:void(0)`，仅仅表示一个 **死链接**  
    在页面很长的时候会使用 `#` 来定位页面的具体位置，格式为：`# + id`  
    如果要定义一个死链接，用 `javascript:void(0)`  


# *异步编程*

异步（Asynchronous, async）是与同步（Synchronous, sync）相对的概念  
在我们学习的传统单线程编程中，程序的运行是同步的（同步不意味着所有步骤同时运行，而是指步骤在一个控制流序列中按顺序执行）。而一个异步过程的执行将不再与原有的序列有顺序关系  
简单来理解就是：同步按你的代码顺序执行，异步 **不按照代码顺序执行**，异步的执行 **效率更高**  
异步就是从主线程发射一个子线程来完成任务  
适用于：遇到死循环的时候，防止失去响应，或者读取什么较大的内容或者发送一个请求等等  
``` js
setTimeout(function () {
    document.getElementById("demo").innerHTML="RUNOOB!";
}, 3000);
```


# *es6 知识*

## 用于声明变量的关键字

let 只在所在代码块内有效  
var 全局范围内有效  
const 用于声明只读的常量，之后不能修改  

for 循环内部很适合用 let 关键字  
每轮循环，声明的变量都是新的  
js 引擎内部会记住前一个循环的值  

let 声明的变量不能提升  
var 的则可以，变量在声明之前已经存在  

const 声明的时候需要初始化赋值
> 注意  
在代码块内，若出现 let 和 const 关键字，会使得所声明的变量在块内是封闭的  
就算在块外定义过也没用  

const 怎么做到使得定义的变量不允许改变？  
其实是使变量对应的内存地址所保存的数据不允许改变  
> 注意  
简单类型和复杂类型变量保存值的方式是不同的  
简单类型的，例如数值、字符串、布尔值等，变量指向的内存地址就是值  
复杂类型的，例如对象、数组、函数等，变量指向的内存地址是一个指针，这个指针指向的才是真正的值  
所以，需要注意的是，用const定义复杂类型的变量时，只能保证指针是不变的  

## 解构赋值

数组解构  
``` js
let [a, b, c] = [1, 2, 3]
let [a, [[b], c]] = [1, [[2], 3]];
let [a, , b] = [1, 2, 3];    //a=1, b=3
let [a, ...b] = [1, 2, 3];    //a=1, b=[2,3]
let [a, b, c, d, e] = 'hello';    //分别等于对应的字符
// 结构的目标 = 解构的源
// 相当于 Python 的解包
```

对象解构
``` js
let { foo, bar } = { foo: 'aaa', bar: 'bbb' };
let {a = 10, b = 5} = {a: 3};    //a = 3; b = 5;
```

## Symbol 关键字

表示独一无二的值
用来作为对象的属性名，保证属性不重名

``` js
let sy = Symbol("key1");

let syObject = {};
syObject[sy] = "hello";    //注意Symbol作为属性名需要用方括号，不用点号
console.log(syObject);    //{Symbol(key1): "hello"}
```

> 注意  
Symbol 值作为属性名时，是公有属性，在类的外部可以访问  
但是不会出现在 for 循环遍历中  
要读取一个对象的Symbol属性，使用 `Object.getOwnPropertySymbols(对象);`

## Map

| Object | Map |
| --- | --- |
| 键值：字符串/Symbols | 键值：任意值 |
| 键无序 | 键有序，先进先出原则 |
| 手动计算键值对数 | size属性求键值对数 |
| 键名可能冲突 | 不会冲突 |

``` js
var myMap = new Map();
myMap.set(键1, 值1);
myMap.set(键2, 值2);

// 通过键获取值
值1 = myMap.get(键1);
值2 = myMap.get(键2);

// 循环遍历
// .entries() 确保按照键值对的插入顺序进行遍历
for (var [key, value] of myMap.entries()) {
    console.log(key + "=" + value);
}

myMap.forEach(
    function(k, v) {
        console.log(k + "=" + v);
    },
    myMap
)

myMap.keys()
myMap.values()
```

> 注意  
虽然 NaN !== NaN 是 true，但是 NaN 作为 Map 的键却是没有区别的  

二维数组可以转为 Map 对象
``` js
var myMap = new Map([[键1,值1], [键2,值2]]);

// 逆变换
var myArray = Array.from(myMap);
```

克隆 Map，直接 `新Map = new Map(旧Map);` 这样会产生新的对象

合并 Map
``` js
var Map1 = new Map([。。。省略]);
var Map2 = new Map([。。。省略]);
var merged_map = new Map([...Map1, ...Map2]);
// 注意 ... 操作符
// 有相同键的情况下，后出现的值会覆盖过去
```

## Set

Set 存储的值是唯一的，可以存储任何类型的值（原始值/对象引用）  
用于去重、求并集、交集、差集  

``` js
let mySet = new Set();

mySet.add(1);
mySet.add(2);
mySet.add("hello");
mySet.add({a:1, b:2});

mySet.has(1);    //true
```

二维数组可以转为 Set 对象
``` js
var mySet = new Set([[1, "hello", 3]]);

// 逆变换
var myArray = [...mySet];
// 注意 ... 操作符
```

## Proxy

对目标对象进行拦截，然后进行某些处理  
不直接操作对象  
Proxy对象包括：target、handler  
``` js
let target = {
    name: 'Tom',
    age: 24
}
let handler = {
    get: function(target, key, receiver) {
        console.log('getting '+key);
        return target[key]; // 不是target.key
    },
    set: function(target, key, value, receiver) {
        console.log('setting '+key);
        target[key] = value;
    }
}
let proxy = new Proxy(target, handler)
proxy.name     // 实际执行 handler.get
proxy.age = 25 // 实际执行 handler.set
// 有点像Python的class中的init方法和类中定义的方法
```

## 函数

当存在某些参数赋予了默认值的时候，不允许使用同名参数

赋予参数null值是有效的

不定参数
``` js
function (...values){
    。。。
}
// 不确定参数个数的时候可以使用 ...
// 例如不知道传入的列表中有多少元素
```

箭头函数
``` js
// 参数 => 函数体

var f = (a,b) => a+b;
// 等同于
var f = function(a,b){
    return a+b;
}
```

维护 this 的上下文
``` js
// 回调函数
var Person = {
    'age': 18,
    'sayHello': function () {
      setTimeout(function () {
        console.log(this.age);
      });
    }
};
var age = 20;
Person.sayHello();  // 20
 
var Person1 = {
    'age': 18,
    'sayHello': function () {
      setTimeout(()=>{
        console.log(this.age);
      });
    }
};
var age = 20;
Person1.sayHello();  // 18
```
对比：
``` js
var Person = {
    'age': 18,
    'sayHello': ()=>{
        console.log(this.age);
      }
};
var age = 20;
Person.sayHello();  // 20
// 此时 this 指向的是全局对象
 
var Person1 = {
    'age': 18,
    'sayHello': function () {
        console.log(this.age);
    }
};
var age = 20;
Person1.sayHello();   // 18
// 此时的 this 指向 Person1 对象
```
箭头函数里面没有 this 对象，this 是外层的 this 对象  

## class

实现更像面向对象的写法
本质是function

``` js
class example{
    // constructor（构造函数）相当于init函数
    constructor(a){
        this.a = a;
        // 默认范围实例对象this，也可以自己指定
    }
    // 静态方法
    static sum(a, b) {
        console.log(a+b);
    }
    // 原型方法
    minus(a,b){
        console.log(a-b);
    }
}
// class也可以是匿名的
```

> 注意  
类不会提升，访问前就要定义好  
类中的方法不需要function关键字  
方法之间不需要分号  

> `instanceof` 查看两个对象的类型是否相同

``` js
// 类的实例化，必须new关键字
new myc1 = example();
new myc2 = example();
// 注意 myc1 和 myc2 是共享原型方法的

// 获取实例的原型对象
Object.getPrototypeOf(myc1)
```

封装
``` js
class Example1{
    constructor(a, b) {
        this.a = a;
        this.b = b;
    }
    get a(){
        console.log('getter');
        return this._a;
    }
    set a(a){
        console.log('setter');
        this._a = a;
    }
}
let exam1 = new Example1(1,2); // 只输出 setter , 不会调用 getter 方法
console.log(exam1._a); // 1, 可以直接访问
```

继承，extends关键字
``` js
class Father {
    test(){
        return 0;
    }
    static test1(){
        return 1;
    }
}
class Child extends Father {
    constructor(){
        super();    //只能在子类的constructor函数中
    }
}
class Child1 extends Father {
    constructor(){
        super();
        // 调用父类普通方法
        console.log(super.test()); // 0
    }
    static test3(){
        // 调用父类静态方法
        return super.test1+2;
    }
}
Child1.test3(); // 3
```

## 模块

%accordion% 每一个模块内声明的变量都是局部变量 %accordion%

``` js
/*-----export [test.js]-----*/
let myName = "Tom";
let myAge = 20;
let myfn = function(){
    return "My name is" + myName + "! I'm '" + myAge + "years old."
}
let myClass =  class myClass {
    static a = "yeah!";
}
export { myName as name1, myAge, myfn, myClass }
// 使用大括号指定所要输出的一组变量写在文档尾部，明确导出的接口
```

``` js
/*-----import [xxx.js]-----*/
import { name1, myAge, myfn, myClass } from "./test.js";    //不管出现几次，只会执行一次
console.log(myfn());// My name is Tom! I'm 20 years old.
console.log(myAge);// 20
console.log(myName);// Tom
console.log(myClass.a );// yeah!
```

%/accordion%


# *高级编程*

Promise  
Generator  
async  


# *参考资料*

https://www.runoob.com/js/js-tutorial.html
