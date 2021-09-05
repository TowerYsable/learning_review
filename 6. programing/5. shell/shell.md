https://myshell-note.readthedocs.io/en/latest/

# 一、基础知识

## 一、Shell简介

Shell 是一个 C 语言编写的脚本语言，它是用户与 Linux 的桥梁，用户输入命令交给 Shell 处理， Shell 将相应的操作传递给内核（Kernel），内核把处理的结果输出给用户。

程序=指令+数据

## 二、Shell分类

### 2.1 图形界面 Shell（GUI Shell）

GUI 为 Unix 或者类 Unix 操作系统构造一个功能完善、操作简单以及界面友好的桌面环境。主流桌面环境有 KDE，Gnome 等。

### 2.2 命令行界面 Shell（CLI Shell）

CLI 是在用户提示符下键入可执行指令的界面，用户通过键盘输入指令，完成一系列操作。

在 Linux 系统上主流的 CLI 实现是 Bash，是许多 Linux 发行版默认的 Shell。还有许多 Unix 上Shell。

```
[root@10-234-2-128 pyworkspace]# cat /etc/shells
/bin/sh
/bin/bash
/sbin/nologin
/usr/bin/sh
/usr/bin/bash
/usr/sbin/nologin
```

**Shell的分类:**

```
* Bourne Shell（/usr/bin/sh或/bin/sh）
* Bourne Again Shell（/bin/bash）
* C Shell（/usr/bin/csh）
* K Shell（/usr/bin/ksh）
* Shell for Root（/sbin/sh）
```

**脚本命名:**

注意：见名知意，后缀规范为`.sh`

## 三、第一个Shell

```
#!/bin/bash
echo "this is my first shell script"
```

`#!` 告诉系统其后路径所指定的程序即是解释此脚本文件的 Shell 程序 `/bin/bash` 指定使用的是那种shell `echo`在终端打印出内容

## 四、执行Shell的三种方法

### 4.1 直接bash执行

```
[root@shell workspace]# ll
total 4
-rw-r--r-- 1 root root 44 Sep  3 14:16 01-scripts.sh
[root@shell workspace]# cat 01-scripts.sh
#!/bin/bash

echo "this is my first script"
[root@shell workspace]# bash 01-scripts.sh
this is my first script
```

### 4.2 ./执行

```
[root@shell workspace]# ./01-scripts.sh
-bash: ./01-scripts.sh: Permission denied
[root@shell workspace]# chmod +x 01-scripts.sh
[root@shell workspace]# ll
total 4
-rwxr-xr-x 1 root root 44 Sep  3 14:16 01-scripts.sh
[root@shell workspace]# ./01-scripts.sh
this is my first script
```

这种方式默认根据脚本第一行指定的解释器处理，如果没写以当前默认 Shell 解释器执行。

### 4.3 source执行

```
[root@shell workspace]# source 01-scripts.sh
this is my first script
```

## 五、Shell变量

变量名+内存空间

变量赋值：`name=value`

弱类型变量，所有变量类型视为字符串类型，对于数值相加自动转换为数组类型，无需实现声明

### 5.1 变量命名规则：

- 命名只能使用英文字母，数字和下划线，首个字符不能以数字开头。
- 中间不能有空格，可以使用下划线（_）。
- 不能使用标点符号。
- 不能使用bash里的关键字（可用help命令查看保留关键字）
- 做到见名知意

环境变量作用范围：当前shell进程及其子进程

本地变量作用范围：当前shell

局部变量作用范围：代码片段

利用export将本地变量导入到环境，扩大作用范围

### 5.2 系统内置变量

在命令行提示符直接执行`env、set`查看系统或环境变量。`env` 显示用户环境变量，`set` 显示 Shell 预先定义好的变量以及用户变量。可以通过 `export` 导出成用户变量。

还可通过`printevn/declare -x`

```
$SHELL      默认 Shell

$HOME       当前用户家目录

$IFS        内部字段分隔符

$LANG       默认语言

$PATH       默认可执行程序路径

$PWD        当前目录

$UID        当前用户 ID

$USER       当前用户

$HISTSIZE   历史命令大小，可通过 HISTTIMEFORMAT 变量设置命令执行时间

$RANDOM     随机生成一个 0 至 32767 的整数

$HOSTNAME   主机名
```

**特殊变量**

```
${1..n} 指定第n个输入的变量名称
$0      脚本自身名字

$?      返回上一条命令是否执行成功，0 为执行成功，非 0 则为执行失败

$#      位置参数总数

$*      所有的位置参数被看做一个字符串

$@      每个位置参数被看做独立的字符串

$$      当前进程 PID

$!      上一条运行后台进程的 PID
```

**相同点**：都是引用所有参数。

**不同点**：只有在双引号中体现出来。假设在脚本运行时写了三个参数 1、2、3，，则 ” * ” 等价于 “1 2 3”（传递了一个参数），而 “@” 等价于 “1” “2” “3”（传递了三个参数）。

profile 类型： * 定义全局变量 * 运行命令或脚本

bashrc 类型： * 定义本地变量 * 定义命令别名

交互式登录shell： 加载顺序：/etc/profile -> /etc/profile.d/* -> ~/.bash_profile -> ~/.bashrc -> /etc/bashrc

非交互式登录shell： 加载顺序：~/.bashrc -> /etc/bashrc -> /etc/profile.d/*

### 5.3 用户自定义变量

- 普通变量

```
[root@shell workspace]# var=normal
[root@shell workspace]# echo $var
normal
```

- 临时环境变量

在当前shell下定义的变量，只对当前shell有效，新的bash已经其子bash无法使用当前定义的shell，如果在本shell存在的情况下，使用`export`来导入到系统变量中，如果当前shell终端终端，那么导入的变量将全部失效，永久生效需要写入linux配置文件中。

- 只读变量

```
[root@shell ~]# var='test'
[root@shell ~]# echo $var
test
[root@shell ~]# readonly var
[root@shell ~]# var='bbb'
-bash: var: readonly variable
```

- 删除变量

```
unset variable_name
```

变量被删除后不能再次使用。unset 命令不能删除只读变量。

### 5.4 变量引用

- = 变量赋值
- += 变量相加

```
[root@shell data]# var=123
[root@shell data]# var+=234
[root@shell data]# echo $var
123234
```

为避免特殊字符及变量与字符连接使用，建议引用变量添加大括号

## 六、引号

单引号是告诉 Shell 忽略特殊字符，而双引号则解释特殊符号原有的意义，比如$、！。

```
[root@xuel-tmp-shell www]# var1="aaa"
[root@xuel-tmp-shell www]# echo '$var1'
$var1
[root@xuel-tmp-shell www]# echo "$var1"
aaa
[root@xuel-tmp-shell www]# var2="aa"
[root@xuel-tmp-shell www]# var3='bb $var2'
[root@xuel-tmp-shell www]# echo $var3
bb $var2
[root@xuel-tmp-shell www]# var4="bb $var2"
[root@xuel-tmp-shell www]# echo $var4
bb aa
```

## 七、注释

- 单行注释使用`#`
- 多行注释固定函数格式

```
:<<EOF
内容...
内容...
EOF
```

# 二、字符串与数组

## 一、字符串常用操作

### 1.1 获取字符串长度

利用`${#var}`来获取字符串长度

```
[root@xuel-tmp-shell ~]# var='abcstring'
[root@xuel-tmp-shell ~]# echo ${#var}
9
```

### 1.2 字符串切片

格式：

${parameter:offset} ${parameter:offset:length}

截取从 offset 个字符开始，向后 length 个字符。

```
[root@xuel-tmp-shell ~]# var="hello shell"
[root@xuel-tmp-shell ~]# echo ${var:0}
hello shell
[root@xuel-tmp-shell ~]# echo ${var:0:5}
hello
[root@xuel-tmp-shell ~]# echo ${var:6:5}
shell
[root@xuel-tmp-shell ~]# echo ${var:(-1)}
l
[root@xuel-tmp-shell ~]# echo ${var:(-2)}
ll
[root@xuel-tmp-shell ~]# echo ${var:(-5):2}
sh
```

### 1.3 字符串替换

格式：${parameter/pattern/string}

```
[root@xuel-tmp-shell ~]# var="hello shell"
[root@xuel-tmp-shell ~]# echo ${var/shell/world}
hello world
```

### 1.4 字符串截取

格式：

${parameter#word} # 删除匹配前缀

${parameter##word}

${parameter%word} # 删除匹配后缀

${parameter%%word}

\# 去掉左边，最短匹配模式，##最长匹配模式。

% 去掉右边，最短匹配模式，%%最长匹配模式。

```
[root@xuel-tmp-shell ~]# url="https://www.baidu.com/index.html"
[root@xuel-tmp-shell ~]# echo ${url#*/}
/www.baidu.com/index.html
[root@xuel-tmp-shell ~]# echo ${url##*/}
index.html

[root@xuel-tmp-shell ~]# echo ${url%/*}
https://www.baidu.com
[root@xuel-tmp-shell ~]# echo ${url%%/*}
https:
```

### 1.5 变量状态赋值

${VAR:-string} 如果 VAR 变量为空则返回 string

${VAR:+string} 如果 VAR 变量不为空则返回 string

${VAR:=string} 如果 VAR 变量为空则重新赋值 VAR 变量值为 string

${VAR:?string} 如果 VAR 变量为空则将 string 输出到 stderr

```
[root@xuel-tmp-shell ~]# url="https://www.baidu.com/index.html"
[root@xuel-tmp-shell ~]# echo ${url:-"string"}
https://www.baidu.com/index.html
[root@xuel-tmp-shell ~]# echo ${url:+"string"}
string
[root@xuel-tmp-shell ~]# unset url
[root@xuel-tmp-shell ~]# echo $url

[root@xuel-tmp-shell ~]# echo ${url:-"string"}
string
[root@xuel-tmp-shell ~]# echo ${url:+"string"}


找出/etc/group下的所有组名称
for i in `cat /etc/group`;do echo ${i%%:*};done
```

## 二、数组

bash支持一维数组（不支持多维数组），并且没有限定数组的大小。数组是相同类型的元素按一定顺序排列的集合。 类似与 C 语言，数组元素的下标由 0 开始编号。获取数组中的元素要利用下标，下标可以是整数或算术表达式，其值应大于或等于 0。

### 2.1 数组定义

在 Shell 中，用括号来表示数组，数组元素用“空格”符号分割开

```
[root@xuel-tmp-shell ~]# args1=(aa bb cc 1123)
[root@xuel-tmp-shell ~]# echo $args1
aa

[root@xuel-tmp-shell ~]# echo ${args1[@]}
aa bb cc 1123
```

### 2.2 数组元素读取

```
[root@xuel-tmp-shell ~]# args1=(aa bb cc 1123)
[root@xuel-tmp-shell ~]# echo ${#args1[@]}     #获取数组元素个数
4
[root@xuel-tmp-shell ~]# echo ${args1[0]}
aa
[root@xuel-tmp-shell ~]# echo ${args1[1]}
bb

[root@monitor workspace]# filelist=($(ls))
[root@monitor workspace]# echo ${filelist[*]}
check_url_for.sh check_url_while01.sh check_url_while02.sh func01.sh func02.sh func03.sh urllist.txt

获取数组元素的下标
[root@monitor workspace]# echo ${!filelist[@]}
0 1 2 3 4 5 6
```

遍历文件

```
filelist=($(ls));for i in ${!filelist[@]};do echo ${filelist[$i]};done
```

## 三、字符显示颜色

| 字体颜色      | 字体背景颜色                                              | 显示方式        |
| ------------- | --------------------------------------------------------- | --------------- |
| 30：黑        | 40：黑                                                    |                 |
| 31：红        | 41：深红                                                  | 0：终端默认设置 |
| 32：绿        | 42：绿                                                    | 1：高亮显示     |
| 33：黄        | 43：黄色                                                  | 4：下划线       |
| 34：蓝色      | 44：蓝色                                                  | 5：闪烁         |
| 35：紫色      | 45：紫色                                                  | 7：反白显示     |
| 36：深绿      | 46：深绿                                                  | 8：隐藏         |
| 37：白色      | 47：白色                                                  |                 |
| 格式：        |                                                           |                 |
| \033[1;31;40m | # 1 是显示方式，可选。31 是字体颜色。40m 是字体背景颜色。 |                 |
| \033[0m       | # \| 恢复终端默认颜色，即取消颜色设置。 \|                |                 |

- 显示方式

```
for i in {1..8};do echo -e "\033[$i;31;40m hello world \033[0m";done
```

- 字体颜色

```
for i in {30..37};do echo -e "\033[$i;40m hello world \033[0m";done
```

- 背景颜色

```
for i in {40..47};do echo -e "\033[47;${i}m hello world! \033[0m";done
```

# 三、运算符

## 一、Shell表达式

### 1.1 整数比较符

| 比较符                | 描述       | 示例                |
| --------------------- | ---------- | ------------------- |
| -eq，equal            | 等于       | [ 1 -eq 1 ]为 true  |
| -ne，not equal        | 不等于     | [ 1 -ne 1 ]为 false |
| -gt，greater than     | 大于       | [ 2 -gt 1 ]为 true  |
| -lt，lesser than      | 小于       | [ 2 -lt 1 ]为 false |
| -ge，greater or equal | 大于或等于 | [ 2 -ge 1 ]为 true  |
| -le，lesser or equal  | 小于或等于 | [ 2 -le 1 ]为 false |

```
[root@monitor ~]# [ 1 -gt 1 ] && echo true || echo false
false
[root@monitor ~]# [ 1 -ne 1 ] && echo true || echo false
false
[root@monitor ~]# [ 1 -eq 1 ] && echo true || echo false
true
[root@monitor ~]# [ 1 -ne 1 ] && echo true || echo false
false
[root@monitor ~]# [ 1 -gt 1 ] && echo true || echo false
false
[root@monitor ~]# [ 2 -gt 1 ] && echo true || echo false
true
[root@monitor ~]# [ 2 -lt 1 ] && echo true || echo false
false
[root@monitor ~]# [ 2 -le 1 ] && echo true || echo false
false
```

### 1.2 算术运算符

假定变量 a 为 10，变量 b 为 20： 注意：运算符两边有空格

```
A=3
B=6
1、let 算术运算表达式
let C=$A+$B
2、$[算术运算表达式]
C=$[$A+$B]
3、$((算术运算表达式))
C=$(($A+$B))
4、expr 算术运算表达式，表达式中各操作数及运算符之间要有空格，而且要使用命令引用
C=`expr $A + $B`
```

### 1.3 布尔运算符

### 1.4 逻辑运算符

| 运算符 | 说明       | 举例                                     |
| ------ | ---------- | ---------------------------------------- |
| &&     | 逻辑的 AND | [[ a -lt 100 && ​b -gt 100 ]] 返回 false  |
| \|\|   | 逻辑的 OR  | [[ $a -lt 100 || $b -gt 100 ]] 返回 true |

### 1.5 文件测试运算符

### 1.6 字符串测试

假定变量 a 为 “abc”，变量 b 为 “efg”：

# 四、流程控制

## 一、if语句

### 1.1 单分支

```
if condition
then
    command1
    command2
    ...
    commandN
fi
```

eg:

```
if [ `ps -ef |grep /usr/sbin/sshd|grep -v grep|wc -l` -eq 1 ];then echo "sshd server exist";fi
```

### 1.2 双分支

```
if condition
then
    command1
    command2
    ...
    commandN
else
    command
fi
```

eg:

```
if [ `ps -ef |grep /usr/sbin/sshd|grep -v grep|wc -l` -eq 0 ];then echo "sshd server exist";else echo "sshd server not exist";fi
```

### 1.3 多分支

```
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

eg:

```
#! /bin/bash

cmd=`rpm -q centos-release|cut -d- -f3`

if [ $cmd -eq 6 ];then
    echo "sysversion is $cmd"
elif [ $cmd -eq 7 ];then
    echo "sysversion is $cmd"
else
    echo "sysversion is `rpm -q centos-release`"
fi
```

## 二、for循环

```
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done
```

eg1:

```
for i in /*;
do
    echo -e "   \c";
    find $i |wc -l|sort -nr;
done
```

eg2:

```
#!/bin/bash
for i in {1..3};
do
    echo $i
done
```

eg3:

```
#!/bin/bash
for i in "$@"; {    # $@是将位置参数作为单个来处理
echo $i
}
```

默认 for 循环的取值列表是以空白符分隔，也就是第一章讲系统变量里的$IFS:

```
#!/bin/bash
OLD_IFS=$IFS
IFS=":"
for i in $(head -1 /etc/passwd); do
echo $i
done
#!/bin/bash

for ip in 192.168.1.{1..254}; do

    if ping -c 1 $ip >/dev/null; then

        echo "$ip OK."

    else

        echo "$ip NO!"

    fi

done
```

读取文件,判断url可用性

```
#!/bin/bash
#function:check url
filename=urllist.txt
for url in $(cat $filename)
do
status=`curl -I $url -s|awk '/HTTP/{print $2}'`
if [ $status == "200" ];then
    echo "Url:$url is ok!status is $status"
else
    echo "Url:$url is error!status is $status"
fi
done
```

## 三、while语句

格式：

```
while 条件表达式:do
    command
done
```

eg1:

```
#!/bin/bash
N=0
while [ $N -lt 5 ]; do
let N++
echo $N
done
```

条件表达式为 true，将会产生死循环,利用此可以将脚本一直放在后台进行执行 eg2:

```
#!/bin/bash
IP=10.75.128.8
dir="/DATA/oracle/netdir/"
if [ ! -d ${dir} ];then
    mkdir -p ${dir}
fi
echo 1 > ${dir}ping.lock
while true
do
    Time=`date +%F`
    TIME="${Time} 23:59"
    if [ "${data}" == "${TIME}" ];then
        mkdir ${dir}${Time} && mv ${dir}ping2.log ${dir}${Time}-ping2.log
        mv ${dir}${Time}-ping2.log ${dir}${Time}
    fi
    find ${dir} -mtime +7 -name "*-ping2.log" -exec rm -rf {} \;
    find ${dir} -mtime +7 -type d -exec rm -rf {} \;

    data=`date +%F' '%H:%M`
    data1=`date +%F' '%H:%M:%S`
    echo "------------${data1}---------------">>${dir}ping2.log
    ping -c 10 ${IP} >>${dir}ping2.log
    if [ $? -eq 1 ];then
        STAT=`cat ${dir}ping.lock`
        if [ ${STAT} -eq 1 ];then
            /usr/bin/python /DATA/oracle/netdir/GFweixin.py xuel GLP-VPN "GLP from PDC(172.16.6.1
50) ping 金融云(10.75.128.8)中断，请检查深信服VPN！ \n TIME:${data1}"            echo 0 > ${dir}ping.lock
        else
            continue
        fi
    else
        STAT=`cat ${dir}ping.lock`
        if [ ${STAT} -eq 0 ];then
            /usr/bin/python /DATA/oracle/netdir/GFweixin.py xuel GLP-VPN "GLP from PDC(172.16.6.1
50) ping 金融云(10.75.128.8)恢复！ \n TIME:${data1}"          echo 1 > ${dir}ping.lock
        else
            continue
        fi
    fi


done
```

文件处理

eg3:

```
#!/bin/bash
#function:check url
filename=urllist.txt
cat $filename | while read url;do
status=`curl -I $url -s|awk '/HTTP/{print $2}'`
if [ $status == "200" ];then
        echo "Url:$url is ok!status is $status"
else
        echo "Url:$url is error!status is $status"
fi
done
```

或

```
#!/bin/bash
#function:check url
filename=urllist.txt
while read url;
do
status=`curl -I $url -s|awk '/HTTP/{print $2}'`
if [ $status == "200" ];then
        echo "Url:$url is ok!status is ${status}"
else
        echo "Url:$url is error!status is ${status}"
fi
done <$filename
```

## 四、break 和 continue 语句

break跳出循环

```
#!/bin/bash

N=0
while true; do
    let N++
    if [ $N -eq 5 ]; then
    break
    fi
    echo $N
done
```

continue

```
#!/bin/bash
N=0
while [ $N -lt 5 ]; do
    let N++
    if [ $N -eq 3 ]; then
        continue
    fi
    echo $N
done
```

## 五、case语句

语句

```
case 模式名    in
    模式 1)
        命令
        ;;
    模式 2)
        命令
        ;;
    *)
        不符合以上模式执行的命令
esac
```

eg

```
#!/bin/bash
case $1 in
    start)
        echo "start."
        ;;
    stop)
        echo "stop."
        ;;
    restart)
        echo "restart."
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
esac
```

# 五、函数

## 一、概念

linux shell 可以用户定义函数，然后在shell脚本中可以随便调用,以此来重复调用公共函数，减少代码量。

## 二、格式

```
[ function ] funname()
{
    action;
    [return int;]
}
```

说明：

- function 关键字可写，也可不写。
- 参数返回，可以显示加：return返回，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n(0-255）,hell 函数返回值只能是整形数值，一般是用来表示函数执行成功与否的，0表示成功，其他值表示失败。因而用函数返回值来返回函数执行结果是不合适的。如果要硬生生地return某个计算结果，比如一个字符串，往往会得到错误提示：“numeric argument required”。 如果一定要让函数返回一个或多个值，可以定义全局变量，函数将计算结果赋给全局变量，然后脚本中其他地方通过访问全局变量，就可以获得那个函数“返回”的一个或多个执行结果了。

```
#!/bin/bash
function output_data() {
    DATA=$((1+1))
    return $DATA
}
output_data
echo $?
#!/bin/bash
# function:add number
function add_num() {
    echo "请输入第一个数："
    read number01
    echo "请输入第二个数字"
    read number02
    if [[ "$number01" =~ ^[0-9]+$ ]] && [[ "$number02" =~ ^[0-9]+$ ]];then
        sum=$(($number01+$number02))
        echo "$number01 + $number02 = $sum"
    else
        echo "input must be number"
    fi
}
add_num
```

## 三、函数参数

将函数写成无状态的，将数据当做参数进行传入

```
#!/bin/bash
funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
    echo "作为一个字符串输出所有参数 $@ !"

}
funWithParam `seq 1 20`
${1..n} 指定第n个输入的变量名称
$0      脚本自身名字

$?      返回上一条命令是否执行成功，0 为执行成功，非 0 则为执行失败

$#      位置参数总数

$*      所有的位置参数被看做一个字符串

$@      每个位置参数被看做独立的字符串

$$      当前进程 PID

$!      上一条运行后台进程的 PID
```

eg:函数炸弹

```
:(){ :|:& };:
```

| [\|](https://myshell-note.readthedocs.io/en/latest/shell-05-函数.html#id5): | 表示每次调用函数“:”的时候就会生成两份拷贝。 |
| :----------------------------------------------------------- | ------------------------------------------- |
|                                                              |                                             |

& 放到后台

递归调用自身，直至系统崩溃

# 六、正则表达式

## 一、基本正则表达式

### 1.1 字符匹配

- .:匹配任意单个字符

- 

- [^]: 匹配指定范围外的任意单个字符

- [:digit:]匹配元字符

```
posix字符
[:alnum:] 字母数字[a-z A-Z 0-9]
[:alpha:]字母[a-z A-Z]
[:blank:]空格或制表键
[:cntrl:] 任何控制字符
[:digit:] 数字 [0-9]
[:graph:] 任何可视字符（无空格）
[:lower:] 小写 [a-z]
[:print:] 非控制字符
[:punct:] 标点字符
[:space:] 空格
[:upper:] 大写 [A-Z]
[:xdigit:] 十六进制数字 [0-9 a-f A-F]
特殊字符
\w 匹配任意数字和字母，等效[a-zA-Z0-9_]
\W 和\w相反，等效[^a-zA-Z0-9_]
\b 匹配字符串开始或结束，等效\<和\>
\s 匹配任意的空白字符
\S 匹配非空白字符
```

### 1.2 次数匹配

用在制定的字符后面，表示制定前面的字符出现多少次 * *:匹配前面的字符任意次（0次获无数次） * ?:匹配前面的字符0次或1次 * +:匹配前面的字符至少1次 * {m,}:匹配前面的字符至少m次（默认工作在贪婪模式下，?取消贪婪模式） * {m,n}:匹配前面的字符至少m次，至多n次 eg:

```
.*:匹配任意字符任意次数
```

### 1.3 位置锚定

- ^:行首锚定，用于模式最左边
- $:行尾锚定,用于模式最右边
- \<或:raw-latex:b:锚定词首，用于单词模式左侧
- \>或:raw-latex:b:锚定词尾，用于单词模式右侧

eg:

```
^$:锚定空行
```

### 1.4 分组引用

分组 * ():将一个或多个字符当成一个整体来进行后续处理

引用 * 1：从左侧起，引用第一个左括号以及与之匹配右括号之间的模式所匹配到的字符，后向引用

exercises:

```
1.显示/etc/init.d/functions文件中以大小s开头的行(使用两种方式)
grep '^[Pp]' /etc/init.d/functions
grep -i "^p" /etc/init.d/functions

2.显示/etc/passwd文件中不以/bin/bash结尾的行
grep -v "/bin/bash$" /etc/passwd

3.显示/etc/passwd文件中ID号最大用户的用户名
sort -t: -k3 -n /etc/passwd |tail -1 |cut -d: -f1

4.如果root用户存在,显示其默认的shell程序
id root && grep '^\<root\>' /etc/passwd |awk -F: '{print $NF}'

5.找出/etc/passwd中的两位或三位数
grep -o -E "[0-9]{2,3}" /etc/passwd
grep -o "[0-9]\{2,3\}" /etc/passwd

6.显示/etc/rc.d/rc.sysinit文件中,至少以一个空白字符开头的且后面存非空白字符的行:
grep '^[[:space:]]\+[^[:space:]]' /etc/rc.d/rc.sysinit


7.找出"netstat -tan"命令的结果以"LISTEN"后跟0,1或多个空白字符结尾的行
netstat -tan|grep 'LISTEN[[:space:]]*$'

8.如果root用户登录了系统,就显示root用户在线,否则说明未登录
w |grep '^\<root\>'>/dev/null && echo "root在线"|| echo "root未登录"

9.找出/etc/rc.d/init.d/functions文件中某单词后面跟一对小括号的行
grep '[[:alpha:]]*()' /etc/rc.d/init.d/functions

10.使用echo输出一个路径,使用egrep取出基名
 echo /tmp/tmp1/vmstat.8.gz |grep -E  -o '[^/]+/?$'|cut -d/ -f1
echo /tmp/tmp1/vmstat.8.gz |awk -F'/' '{print $NF}'

11.匹配PPID开头，行中又再次出现PPID的内容。/etc/init.d/functions
grep -E "(PPID).*\1" /etc/init.d/functions

12.利用awk找出/etc/ssh/sshd_config内出过空行与以#开头的行
awk '!/^#/ && !/^$/{print}' /etc/ssh/sshd_config
grep -v -E '^#|^$' /etc/ssh/sshd_config
```