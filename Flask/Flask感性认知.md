# Flask框架学习

## 1.环境与工具

1.环境：Python3.8 & Flask1.1.2

2.工具 Pycharm集成开发工具

## 2.结构认知

### **认识app.py**

```python
@app.route('/')
def index():
    return 'Index page'
```

@app.route('/') 使用route装饰器来把函数绑定到URL

默认的为'/'根目录，可以根据实际业务需求进行对应的界面URL路径。

### **变量规则**

通过将URL的一部分标记为<variable_name>就可以在URL中添加变量。

标记的部分会作为关键字参数传递给函数。可以通过使用 \<converter:variable_name\>,可以选择性的加上一个转换器，为变量指定规则。

```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
```

![image-20201027165151310](C:\Users\lml65\AppData\Roaming\Typora\typora-user-images\image-20201027165151310.png)

### **唯一的URL/重定向行为**

下述的两条规则的不同之处在于是否使用尾部的斜杠：

```python
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

projects 的 URL 是中规中矩的，尾部有一个斜杠，看起来就如同一个文件夹。 访问一个没有斜杠结尾的 URL 时 Flask 会自动进行重定向，帮你在尾部加上一个斜杠。

about 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这个 URL 时添加了尾部斜杠就会得到一个 404 错误。这样可以保持 URL 唯一，并帮助 搜索引擎避免重复索引同一页面。常见的索引下的建议使用about格式的，省略最后的/。

### URL构建

url_for()函数用于构建指定函数的URL，他把函数名称作为第一个参数。它可以接受任意个关键字参数，每个关键字对应URL中的变量。未知变量将添加到URL中作为查询参数。

*问题：为什么不把URL写死在模板中，而要使用反转函数url_for()动态构建？*

1.反转通常比硬编码URL的描述性更好。

2.可以只在一个地方改变URL，而不用导出乱找

3.URL创建会处理特殊字符的转义和Unicode数据，比较直观。

4.生产的路径总是绝对路径，可以避免相对路径产生副作用。

5.当应用是放在URL根路径之外的位置(不在/中)，url_for()会自动妥善处理

我们可以使用test_request_context()方法来尝试使用url_for()。

test_request_context()告诉Flask正在处理一个请求。

```Python
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

```
/
/login
/login?next=%2F
/user/John%20Doe
```

### HTTP 方法

Web 应用使用不同的 HTTP 方法处理 URL 。当你使用 Flask 时，应当熟悉 HTTP 方法。 缺省情况下，一个路由只回应 `GET` 请求。 可以使用 [`route()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.route) 装饰器的 `methods` 参数来处理不同的 HTTP 方法:

```Python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

如果当前使用了 GET 方法， Flask 会自动添加 `HEAD` 方法支持，并且同时还会 按照 [HTTP RFC](https://www.ietf.org/rfc/rfc2068.txt) 来处理 `HEAD` 请求。同样， `OPTIONS` 也会自动实现。

### 静态文件

动态的 web 应用也需要静态文件，一般是 CSS 和 JavaScript 文件。理想情况下你的 服务器已经配置好了为你的提供静态文件的服务。但是在开发过程中， Flask 也能做好 这项工作。只要在你的包或模块旁边创建一个名为 `static` 的文件夹就行了。 静态文件位于应用的 `/static` 中。Pycharm默认自动创建static文件夹和templates文件夹

使用特定的 `'static'` 端点就可以生成相应的 URL

```Python
url_for('static', filename='style.css')
```

这个静态文件在文件系统中的位置应该是 `static/style.css` 。

### 渲染模板

在 Python 内部生成 HTML 不好玩，且相当笨拙。因为你必须自己负责 HTML 转义， 以确保应用的安全。因此， Flask 自动为你配置 [Jinja2](http://jinja.pocoo.org/) 模板引擎。使用 [`render_template()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.render_template) 方法可以渲染模板，你只要提供模板名称和需要 作为参数传递给模板的变量就行了。

下面是一个简单的模板渲染例子:

```Python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```























































