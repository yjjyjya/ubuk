### shell 脚本

---

### 一、shell 简介

shell 脚本是解释型语言（C 语言是编译型语言），是 shell 命令的有序集合

1.1 主要步骤

（1）建立 shell 文件
```
vi filename.sh
```
输入：date

（2）赋予 shell 文件执行权限
```
chmod 740 filename.sh
```
或者
```
chmod u+x filename.sh
```

（3）执行 shell 文件
```
./filename.sh
```

1.2 shell 变量

（1）用户自定义变量  
支持创建变量存储数据，但是不支持数据类型，任何赋给变量的值都是字符串
```
COUNT=1
echo ${COUNT}
```
设置只读变量：
```
myUrl="https://www.google.com"
readonly myUrl
```
删除变量用：
```
unset COUNT
```

- 字符串

单引号，只会原样输出  
双引号，里面可以有变量，可使用转义字符  
    - 获取字符串长度  
    `echo ${#string}`
    - 截取字符串（注意下标从0开始）  
    `echo ${string:1:4}`

- 数组

只支持一维数组，但是各个元素的类型可以不一致，可以使用非连续的下标，且没有范围限制
```
array_name=(value0 value1 value2 value3)
echo ${array_name[0]}    #获取第一个元素
echo ${array_name[@]}    #获取所有元素
```

- 关联数组
    ``` bash
    #!/bin/bash

    declare -A site    #定义一个关联数组site（键值的形式）
    site["google"]="www.google.com"
    site["runoob"]="www.runoob.com"
    site["taobao"]="www.taobao.com"
    ```

    > 注意：等号两边不能加空格；通常使用全大写变量

（2）位置变量  
赋予命令行参数  
`$#`，输出参数个数  
`$@`，输出所有参数，但是各个参数分开  
`$*`，输出所有参数，但是作为一个整体  
`$?`，输出前一个命令的结果  
`$$`，输出正在执行的进程的 ID 号  

（3）预定义变量  
赋予对应位置的参数  
`${0}`、`${1}`......  
``` bash
#!/bin/bash

echo "Shell 传递参数实例！";
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";
```

```
$ chmod +x test.sh 
$ ./test.sh 1 2 3
Shell 传递参数实例！
执行的文件名：./test.sh
第一个参数为：1
第二个参数为：2
第三个参数为：3
```

（4）环境变量  
`PATH=...`  
`HOME=...`  
`IFS=...`  
`TERM=...`  


### 二、shell 语句

有三大语句：说明性语句、功能性语句、结构性语句

2.1 说明性语句

用于注释
``` bash
# 这是说明
```

多行注释
``` bash
:<<EOF
注释内容...
注释内容...
注释内容...
EOF
```

2.2 功能性语句

（1）`read var`  
从标准输入读入一行，并赋值给 var  
若标准输入无数据，则会等待，直到数据到来或者程序被终止  
也可以类似 Python 解包的形式 `read var1 var2 var3`  

（2）`expr \( 10 + 10 \) \* 2`  
即计算 `(10+10)*2`，结果为 40，注意需要有反斜杠作为转义字符，运算符之间要 **有空格**  
表达式需要用反引号将表达式围起来  

（3）测试语句  
test 命令用于检查某个条件是否成立，它可以进行数值、字符和文件三个方面的测试  
`test "$answer" = "yes"`，检查变量 answer 是否为字符串 yes  
`test $num -eq 18`，检查变量 num 的值是否等于 18  
`test -d tmp`，检查 tmp 是否是变量名  
注意 **相等为 0，不等为 1**，在 shell 语言中 **0 代表 true，0 以外的值代表 false**  

- 数值测试  
    `-eq`，相等，等同于 `==`  
    `-ne`，不等  
    `-gt`，大于  
    `-ge`，大于等于  
    `-lt`，小于  
    `-le`，小于等于  

- 字符测试  
    `=` 相同，注意只有一个等号  
    `!=` 不相等  
    `-z 字符串` 字符串的长度为零则为真  
    `-n 字符串` 字符串的长度不为零则为真  

- 文件测试  
    `-e 文件名` 如果文件存在则为真  
    `-r 文件名` 如果文件存在且可读则为真  
    ......  

- 布尔运算符  
    `!` 非，`[! False]`  
    `-a` 与，`[ $a -lt 20 -a $b -gt 100 ]` 等同于 `[[ $a -lt 20 && $b -gt 100 ]]`  
    `-o` 或，`[ $a -lt 20 -o $b -gt 100 ]` 等同于 `	[[ $a -lt 20 || $b -gt 100 ]]`  
    优先度：`! > -a > -o`  

（4）echo、printf  
`echo "..." > myfile` 显示结果定向至文件  
若不希望在屏幕上显示输出结果，则可以将输出重定向到 /dev/null：`$ command > /dev/null`  
printf 功能和 echo 差不多，但是需要自己手动添加换行 `\n`  
语法是 `printf 格式 [参数...]`  

2.3 结构性语句

（1）分支语句

- 条件语句  
经常与 test 命令结合使用  

``` bash
#! /bin/bash
if [ $# -ne 1 ]    #如果输入的参数个数不等于 1 则执行 then
# 等同于 if (( $# -ne 1 ))

then
    echo "usage : $0 filename"
    exit
fi
```

配合 else、elif 语句：  
``` bash
if condition1
then
    command1
elif condition2 
then 
    command2
else
    commandN
fi
```

- 多路分支语句（类似 switch case 语句）  
``` bash
#! /bin/bash
echo -n "please choose (yes|no)?"
read R
case $R in    #注意 in
    yes | Yes | y | Y | YES)
        echo "yes"
        ;;    #表示 break 跳出 case
    no | No | n | N | NO)
        echo "no"
        ;;
    *)
        echo "wrong"
esac
```

（2）循环语句

- for 循环  
``` bash
#! /bin/bash
for I in `seq 1 2 10`
do 
    echo "$I"
done
# 循环输出1到10，且步长为2
```

- do 循环  
实例：实现拷贝当前目录下的所有文件到 backup 子目录下  
``` bash
#! /bin/bash

if [! -d $HOME/backup]

then
    mkdir $HOME/backup
fi

flist=`ls`
for file in $flist
do

    if [$# = 1]
    then

        if [$1 = $file]
        then
            echo "$file found"
            exit
    
    else
        cp $file $HOME/backup
        echo "$file copied"
    fi
done
echo Backup Completed
```

- while 循环（判断条件为 **假** 时停止）  
实例：输入 5 个数，分别判断是什么等级的  

``` bash
#! /bin/bash

I=0

while [$I -lt 5]
do

    I=`expr $I + 1`
    echo -n "input score:"
    read $S

    case `expr $S / 10` in
        9 | 10)
            echo "A"
            ;;
        6 | 7 | 8)
            echo "B"
            ;;
        *)
            echo "C"
            ;;
    esac
    echo "$I"
done
```

- until 循环（判断条件为 **真** 时停止）

（3）break 和 continue

实例：遇到偶数就跳出循环  
``` bash
#! /bin/bash

if [$# -ne 5]
then
    echo "argument 5"
    exit
fi

for I
do
    if [`expr $I % 2` -eq 1]
    then
        echo "$I"
    else
        break
    fi
done
```

`break n`，表示跳出 n 层循环  
`continue n`，表示跳转到最近 n 层循环的下一轮循环上  


### 三、shell 函数

3.1 基础

必须将函数放在脚本开始部分，其定义格式如下  
``` bash
【function】 函数名 [()]
{
    action;
    【return int;】
}
funWithReturn
echo "执行上述函数的输出为 $?"
# 【】表示是可选的
```

3.2 将函数输出传递给变量

``` bash
value_name=`function_name [arg1 arg2 ...]`
```
实例：  
``` bash
grep_user()
{
    R=`grep "$1" /etc/passwd | wc -l`
    echo $R
}

echo -n "input username:"
read USER
RET=`grep_user $USER`
echo "----return $RET----"
if [$USER -eq 1]
then
    echo "$USER exist"
else
    echo "$USER not exist"
fi
```

3.3 获取函数的返回状态

``` bash
function_name [arg1 arg2 ...]
echo $?
# 实例
grep_user()
{
    R=`grep "$1" /etc/passwd | wc -l`
    echo $R
    return $R
}

echo -n "input username:"
read USER
grep_user $USER
RET=$?
if [$USER -eq 1]
then
    echo "$USER exist"
else
    echo "$USER not exist"
fi
```

3.4 变量的作用域

- 全局作用域：在脚本的任何地方都能够访问该变量

- 局部作用域：只能在声明变量的作用域内访问  
    声明格式：
    ``` bash
    local variable_name=value
    ```


### 四、其他

一个 shell 脚本可以包含另一个

> 被包含的文件不需要可执行权限  
只需要在调用的脚本里使用 `source 被调用的脚本文件名`  