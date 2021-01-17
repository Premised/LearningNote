四种编程范式

- 1. 面向过程的
- 2. 面向对象的
- 3. 泛型编程
  template<typename T,typename U>
  auto add3(T a,U b)->decltype(a+b){
    return a + b;
  }
- 4. lambada
    auto add4 = [](int a,int b) -> int{
      return a + b;
    }
- 2. 重载运算符
class ADD{
public 
}






## C 语言基础
## 数据结构与算法
## 计算机网络
## 操作系统



IDE 编译期 g++
    编辑器 vim
    调试器 gdb
    
C 语言编译流程: 编译 将C语言源代码转换为对象文件以.o结尾的文件 链接阶段将若干个对象文件压缩成一个可执行程序。

-E 只激活预处理,这个不生成文件,你需要把它重定向到一个输出文件里 面. 例子用法: gcc -E hello.c > pianoapan.txt gcc -E hello.c | more 
慢慢看吧,一个hello word 也要与处理成800行的代码 -S 只激活预处理和编译，就是指把文件编译成为汇编代码。 
例子用法 gcc -S hello.c 他将生成.s的汇编代码，你可以用文本编辑器察看
-c 只激活预处理,编译,和汇编,也就是他只把程序做成obj文件 
例子用法: gcc -c hello.c 他将生成.o的obj文件

nm -C 目标文件(以.o结尾)
三行说明
有数字是文件中定义的
没有数字的文件是外部文件的定义

编译阶段主要处理语法检查: 声明 过程 帮助处理语法检查

链接阶段：将不同的对象定义和索引进行链接

printf("\033[1;31;42mhelloworld\n");
第一规范，0值属性要放置在第一位，屏蔽之前属性设置对于当前属性的影响
末尾打上0 屏蔽当前属性设置对之后属性的影响。





