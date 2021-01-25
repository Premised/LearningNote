# Hadoop 集群搭建

## Linux 操作命令
### scp命令 secure copy 
- 命令格式： scp -r user@hadoop@host:$dir/$filename  user@hadoop@host:$dir
### rsync 命令 
#### 区别于scp的命令：rsync只是增量更新有修改的文件，只拷贝差异化的内容
- 命令格式：rsync -rvl[r 递归 v 查过过程 l 软符号] user@hadoophost:$fir/$filename  user@hadoophost:$dir/

### xsync 集群分发脚本 (当某一个配置文件变动，可以同步到所有服务器上进行修改)
- 1.需求：循环复制文件到所有节点的相同目录下；
- 2 需求分析
    - a rsync命令原始拷贝
    - b 期望脚本
    xsync 要同步的文件名称
    - c 在/home/hadoop/bin 这个目录下存放的脚本，hadoop用户可以在系统任何地方直接执行，
- 3 脚本实现
    - a 
    >   #!/bin/bash
        #1 获取输入参数的个数，如果没有参数，直接推出
        pcount=$#
        if((pcount==0));then
        echo no args;
        exit;
        fi

        #2 获取文件名称
        p1=$1
        fname=`basename $p1`
        echo fname=$fname

        #3 获取上级目录到绝对路径
        pdir=`cd -P $(dirname $p1); pwd`
        echo pdir=$pdir


        #4 获取当前用户名称
        user=`whoami`


        #5 循环
        for((host=103;host<105;host++)); do
            echo -----------------hadoop$host-------------------
            rsync -rvl $pdir/$fname $user@hadoop$host:$pdir
        done
        
    - b 将xsync放到/usr/local/bin 目录下
    
    
### 完全分布式运行模式环境搭建
#### 1. 配置集群
- 1.1 核心配置文件 
    - 配置core-site.xml
    
    <!-- 指定HDFS中NameNode的地址 -->
    <proerty>
        <name>fs.defaultFS</name>
        <value>hdfs://hadoop02:9000</value>
    </property>

    <!-- 指定Hadoop运行时产生文件的存储目录 -->
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/opt/module/hadoop-2.7.7/data/tmp</value>
    </property>
    
    - **HDFS配置文件**
    - 配置hadoop-env.sh
    
    ```shell
    # The java implementation to use.
    export JAVA_HOME=/opt/module/jdk1.8.0_73
    ```
    
    配置hdfs-site.xml
    ```shell
    <!-- 指定Hadoop的副本数，默认是3 -->
    <property>
        <name>dfs.replication</name>
        <value>3</value>
    </property>

    <!-- 指定Hadoop辅助名称节点主机配置 -->
    <property>
        <name>dfs.namenode.secondary.http-address</name>
        <value>hadoop04:50090</value>
    </property>

    ```
    - 配置YARN文件
    - yarn-env.sh
    添加配置JAVA_HOME的变量
    ```shell
    # some Java parameters
    export JAVA_HOME=/opt/module/jdk1.8.0_73

    ```
    
    - 配置yarn-site.xml
    ```shell
    <!-- Reducer获取数据的方式 -->
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>

    <!-- 指定yarn的resourceManager的地址 -->
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>hadoop03</value>
    </property>
    ```
    - 配置MapReduce配置文件
    - 配置mapred-env.sh
    ```shell
    export JAVA_HOME=/opt/module/jdk1.8.0_73
    ```
    
    - 配置mapred-site.xml
    ```shell
    cp mapred-site.xml.template mapred-site.xml
    
    vim mapred-site.xml
    
    <!-- 指定MR运行在yarn上 -->
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>

    ```
    
- 在集群上分发配置好的Hadoop配置文件
    - xsync hadoop/
    
#### 启动集群
- 初始化
    ```shell
    cd /opt/module/hadoop-2.7.7/
    bin/hdfs namenode -format
    ```
    
- 查看服务JPS命令

- 启动集群
    - 1. sbin/hadoop-daemon.sh start namenode(hadoop101)
    - 2. sbin/hadoop-daemon.sh start datanode (hadoop101\102\103都执行)
### ssh免密登录
    - 原理浅析 
        - 服务器A 1.ssh-key-gen 生成密钥对，私钥保存在自己 
        - 2.服务器A将公钥发送给服务器B（拷贝），服务器B保存公钥到Authorized_keys 
        - 3.服务器Assh访问服务器B(数据用私钥A加密)
        - 4. 服务器B接受数据后，去授权key中查找A的公钥，并解密数据
        - 5. 服务器B采用A公钥加密数据返回给服务器A
        - 6. 服务器A接受到B发送的数据后用自己的私钥A解密数据
    - 操作步骤：
        - 先回到家目录 cd 
        - ls -al  找到 .ssh目录
        - cd .ssh
        - 生成密钥对 ： ssh-keygen -t rsa  连续三次回车就好，rsa 加密算法
        - ll 查看生成的文件
            - id_rsa
            - id_rsa.pub
        - copy 公钥到其他服务器 命令： ssh-copy-id hadoop103  (其他服务器)
        
    - NameNode节点和ResourceNode都需要进行对应的公钥拷贝
    - 102 即namenode节点配置root的ssh
    
### 群起集群
- 配置slaves
```shell 
cd /opt/module/hadoop-2.7.7/etc/hadoop/slaves
vim slaves
# 添加对应的DataNode节点的ip/域名

xsync slaves
```
- 启动集群
```shell
# NM 启动
sbin/start-dfs.sh 

# RM 节点启动
sbin/start-yarn.sh 
```
    
    
