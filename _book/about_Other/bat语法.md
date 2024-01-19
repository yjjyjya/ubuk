推荐还是自己将这些语句进行测试  
毕竟还是存在很多问题  


# *简介*

批处理文件是以 `.bat` 结尾的文本文件，这个文件的每一行都是一条 DOS 命令  
大小写不敏感(命令符忽略大小写)  
文件扩展名为 `.bat` 或 `.cmd`  
可以先创建一个 txt 文件，之后再将后缀修改为 `.bat`  
双击该批处理文件，系统就会调用 Cmd.exe 来运行该文件  

支持通过 `if` 和 `goto` 来控制流程，也可以使用 `for` 循环  
但是编程能力远不如 C 语言等编程语言，也十分不规范  

`C:\AUTOEXEC.BAT` 是每次系统启动时都会自动运行的，可以将每次启动时都要运行的命令放入该文件中  


# *常用语句*

## 参数

- 系统参数

- 传递参数  
    参数下标从 1 开始，通过百分号加数字表示  
    ``` batch
    call test2.bat "hello" "haha"
    
    在 test2.bat 文件里写:
    echo %1 (打印 "hello"，对应传入的第一个参数)
    echo %2 (打印 "haha")
    echo %0 (打印 test2.bat)
    echo %19 (打印 "hello"9)
    ```

## 获取当前所在路径

`%~dp0`，其中 `d` 为 Drive 的缩写，即为驱动器，磁盘。`p` 为 Path 缩写，即为路径，目录  
`cd %~dp0` 进入批处理文件所在的目录  
`cd %~dp0bin\` 进入批处理所在目录的 bin 目录  

> bat 文件中若单行代码太长可以使用 `^` 进行换行  
shell 脚本中则可以使用 `\`  

## 获取命令帮助

`xxx /?`  
例如 `ping /?`

## 终止进程

`taskkill /f /im ???.exe`
taskkill /f /im ???.exe 是一个用于终止进程的Windows命令。

/f 参数表示强制终止进程，即无需提示用户确认即可终止进程。
/im 参数后面跟着的是进程的映像名称（Image Name），用于指定要终止的进程。
在命令中的 ??? 部分需要替换为具体的进程映像名称，例如 notepad.exe 或 chrome.exe。
使用 taskkill 命令终止进程需要管理员权限

## echo 命令

echo 命令类似于 print 函数，也可以配合重定向符号使用，将输出的内容写入文件中  

`echo off` 使得命令行窗口 **在其之后的命令** 只显示脚本运行结果，而不会显示每个命令的具体执行过程。用于隐藏命令行窗口中的冗余输出，使输出结果更加简洁  
`@` 符号表示不显示 **当前该行** 的命令  
所以常常将二者结合使用：`@echo off`  

## Goto 命令

`goto label`  
指定跳转到 label 标签行，找到标签行后，程序将处理从 **下一行开始** 的命令  
label 标签的名字最好是有意义的，字母前必须加个 **冒号** `:` 来表示这个字母是标签  
经常与 `if` 配合使用，根据不同的条件来执行不同的命令组  

## Rem 命令

`Rem Message...`  
起到一个 **注释** 的作用，便于自己和别人理解命令含义  

> 小技巧  
可以用 `::` 代替 `rem`  

## Pause 命令

会暂停批处理的执行并在屏幕上显示 `Press any key to continue...` 的提示，等待用户按任意键后继续  
`pause` 命令会使程序挂起  

## Call 命令

调用 **另一个** 批处理程序，并且 **不终止** 当前的父批处理程序  
如果不用 `call` 而直接调用别的批处理文件，那么执行完那个批处理文件后 **将无法返回** 当前文件并执行当前文件的后续命令  
无法在脚本或批处理文件外使用 `call`  
例子：`call="%cd%\test2.bat" arg1 arg2 arg3` 调用指定目录下的 `test2.bat`，并传入 3 个参数  

> 注意  
可以调用自身，但是注意死循环、递归  

## start 命令

调用外部程序，所有的 **DOS 命令** 和 **命令行程序** 都可以由 `start` 命令来调用  

- 常用参数  
    - `MIN` 开始时窗口最小化  
    - `WAIT` 启动应用程序并等候它结束  

例子：`start /MIN e:\"program files"\hello\world.exe arg1 arg2`，用于调用某个目录下的 `.exe`，并传入 2 个参数，且 `/MIN` 参数使得窗口最小化  

> 注意  
文件路径名有空格时，就利用双引号  

## If 命令

`if [not] "某参数" == "字符串" (命令)`  
若某参数等于指定字符串的条件成立，则运行指定命令，否则跳过，运行下一句  

`if exist 某文件 type 某文件`  
如果存在某文件，则显示它的内容  

`if [not] errorlevel <数字> (命令)`  
若错误码 errorlevel（或称返回码）等于指定的数字，则条件成立，运行指定命令，否则跳过，运行下一句  
返回值必须按照 **从大到小** 的顺序排列  

``` batch
if 条件1 (条件1成立时执行的命令)
^ else if 条件2 (条件2成立时执行的命令)
^ else (都不成立时执行的命令)`
```
注意换行后面的 `^`  

> 比较运算符  
EQU - 等于 (一般使用“==”)  
NEQ - 不等于 (没有 “!=”,改用“ if not 1==1 ”的写法)  
LSS - 小于  
LEQ - 小于或等于  
GTR - 大于  
GEQ - 大于或等于  

## choice 命令

此命令可以让用户输入一个字符（用于选择），从而根据用户的选择返回不同的 `errorlevel`（choice的返回值是环境变量errorlevel的值）  
然后配合 `if errorlevel` 选择运行不同的命令  

例如：
``` batch
choice /c abc /n
::应先判断数值最高的错误码
if errorlevel 3 goto defrag
if errorlevel 2 goto mem
if errorlevel 1 goto end
```
并且限定用户只能输入"a"、"b"、"c"这三个选项中的一个  
当你选择a时，a是第1个选项，所以errorlevel的值为1当你选择b时，b是第2个选项，所以errorlevel的值为2当你选择c时，c是第3个选项，所以errorlevel的值为3  

## for 命令

主要用于参数在指定的范围内 **循环执行命令**  

> `skip=n` 指在文件开始时忽略的行数  
`m-n` 表示一个范围  

- 例子  
    - 显示当前目录下所有以 bat 或者 txt 为扩展名的文件名  
        `for %%c in (*.bat *.txt) do (echo %%c)`  

    - 显示 E 盘 test 目录下所有以 bat 或者 txt 为扩展名的文件名  
        `for /R E:\test %%b in (*.txt *.bat) do (echo %%b)`  

    - 显示当前目录下所有包含有 e 或者 i 的目录名  
        `for /D %%a in (*e* *i*) do (echo %%a)`  

    - 遍历当前目录下所有文件  
        `for /r %%c in (*) do (echo %%c)`  

    - 产生序列 1 2 3 4 5  
        `for /L %%c in (1,1,5) do (echo %%c)`  

    - 显示当前的年月日和时间  
        `for /f "tokens=1-3 delims=-/. " %%j in ('Date /T') do (echo %%j年%%k月%%l日)`  
        `for /f "tokens=1,2 delims=: " %%j in ('TIME /T') do (echo %%j时%%k分)`  

    - 读取记事本里的内容  
        `for /f "delims=" %%a in (zhidian.txt) do (echo %%a)`  

    - 把记事本中的内容每一行前面去掉 8 个字符  
        ``` batch
        setlocal enabledelayedexpansion
        for /f %%i in (zhidian.txt) do (
        set atmp=%%i
        set atmp=!atmp:~8!
        if {!atmp!}=={} ( echo.) else (echo !atmp!)
        )
        ```

## continue、break 命令

例子  
``` batch
for /F ["options"] %variable IN (command) DO (
这里是一些命令
if ... goto continue
if ... goto break
这里是一些命令
:continue    ::这里打上标签，goto 可以进行跳转，直接进行下一次循环
)

:break    ::同理这里打上标签，直接跳出 for 循环
```

## 字符串处理

- 分割字符串  
    ``` batch
    "%time%" 显示如："11:04:23.03" (完整的时间"hh:mm:ss.tt")
    :: 注意索引从 1 开始
    "%time:~0,5%" 显示"hh:mm"(即"11:04")
    "%time:~0,8%" 显示标准时间格式"hh:mm:ss"(即"11:04:23"，前8个字符串)
    "%time:~3,-3%"显示"mm:ss"(即从第4个开始,截去最后3个的字符串)
    "%time:~3%" 显示"04:23.03"(即去掉前3个字符串)
    "%time:~-3%" 显示".tt"(即最后3个字符串)
    ```

- 替换字符串  
    ``` batch
    set a="abcd1234"
    echo %a%    ::显示："abcd1234"
    set a=%a:1=kk%    ::替换“1”为“kk”
    echo %a%    ::显示："abcdkk234"
    ```

- 计算字符串长度  
    写一个 for 循环来计算  
    ``` batch
    set testStr=This is a test string
    :: 将 testStr 复制到str，str 是个临时字符串
    set str=%testStr%
    :: 标签，用于goto跳转
    :next1
    :: 判断str是不是空，如果不是则执行下边的语句
    if not "%str%"=="" (
    :: 算术运算，使num的值自增1，相当于num++或者++num语句
    set /a num+=1
    :: 截取字符串，每次截短1
    set "str=%str:~1%"
    :: 跳转到next1标签: 这里利用goto和标签，构成循环结构
    goto next1
    )
    :: 当以上循环结构执行完毕时，会执行下边的语句
    echo testStr=%testStr%
    echo testStr的长度为：%num%
    ```

- 字符串合并  
    没有直接的字符串合并函数  
    `set str1=%str1%%str2%    ::(合并 str1 和 str2)`  


- 截取字符串时，需要传递参数  
    ``` batch
    setlocal enabledelayedexpansion
    echo !args:~%num%,-5!    ::截取出从第num+1开始到倒数第5个结束的字符串
    ```


# *参考资料*

https://www.cnblogs.com/zhaoqingqing/p/4620402.html  