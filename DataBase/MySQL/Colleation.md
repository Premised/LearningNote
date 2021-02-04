- 数据库事务sql

```mysql
1：查看当前的事务
SELECT * FROM INFORMATION_SCHEMA.INNODB_TRX;

2：查看当前锁定的事务

SELECT * FROM INFORMATION_SCHEMA.INNODB_LOCKS;

3：查看当前等锁的事务
SELECT * FROM INFORMATION_SCHEMA.INNODB_LOCK_WAITS;

4. show full processlist; 

杀死进程id（就是上面命令的trx_mysql_thread_id列）

kill 线程ID
```

- 授权服务器MySQL远程访问

> grant all privileges on \*.\* to 'root'  @'%' identified by 'password';
>
> flush privileges ; 
>
> delimiter 'char' // 声明分隔符，默认是;

- 存储过程

> 存储过程存储在mysql数据库中，查看存储过程
>
> select  name  from mysql.proc  where db='db_name';
>
> show procedure status;
>
> show create procedure db.pro_test1;
>
> // 查询结果赋值给变量 set 赋值
>
> declare num int;
>
> select count(\* ) into value from table;
>
> while
>
> repeat
>
> loop 
>
> C:loop
>
> leave c;
>
> end loop

