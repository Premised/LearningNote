# Flask 框架

## 谈谈对PythonWeb框架：
  - Django，大而全，重武器，内部提供；ORM、Admin、中间件、Form、ModelForm、Session、缓存、信号、CSRF；
  - Flask：短小精悍、可扩展强、第三方组件丰富Extension 
  - tornado:异步非阻塞+短小精悍。
## wsgi（web service gateway Interface）web 服务器网关接口。
  - Django：wsgiref
  - Flask：werkzeug

## Flask action
   - 装饰器实现
       - 位置
       - URL起别名(不能重复)
   - 类似django中间件的东西：before_request装饰器
   
##  前置知识点
    - threading local  
    - funtools.wraps
    - funtions.partial 
    
    - 面向对象的封装和内置函数
    
## 上下文管理（※）
  
