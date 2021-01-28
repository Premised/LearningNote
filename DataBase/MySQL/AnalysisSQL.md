# SQL分析

## 1.通过慢查询
```mysql
show processlist;
```

## 2.explain 分析SQL执行计划


## 3.show profile 分析SQL

**MySQL从5.0.37版本开始增加了对show profiles 和show profile语句的支持。show profiles 能够在做SQL优化时帮助我们了解事件都耗费到哪里了**

- 通过have_profiling参数，能够看到当前MySQL是否支持profile；
```mysql
select have_profiling;
```
默认profiling是关闭的，可以通过set语句在select级别开启profiling：
```mysql
-- 查看是否开启
select @@progiling;

-- 设置开启
set profiling=1;
```
通过profile 分析SQL

通过 show profiles 查看全部的操作指令的耗时 ，指标字段有：query_id (查询ID)，duration [耗时]， query[查询语句] 

通过 show profile [-- 选项 all、cpu...] for query id(上述show profiles 中对应的id，即查看对应的查询语句的耗时)；注意;sending data：MySQL向mysql发送请求开始到数据返回客户端的整个时间的耗费；


## 通过trace 分析优化器执行计划
**MySQL5.6提供了对SQL的跟踪trace，通过trace文件能够进一步了解为什么优化器选择A计划，而不是选择B计划**
打开trace，设置格式为JSON，并设置trace最大能够使用的内存大小















