
## 如何用python打开一个网页
在python中我们可以使用urllib、requests、scrapy、pyspider、pandas等库来打开一个网页。  
初学者最好是先学习requests这个库。  
后面可以进阶学习scrapy和pyspider。  
urllib这个库可以不学。  
pandas呢，可以用来针对性爬取表格类型的网站（例如我们现在要爬取的首页）。  
现在主要以requests这个库来进行教学。  
下面是requests打开网页的基本代码。  
详情看注释

### requests打开一个网页


```python
# 导入python的第三方库requests
import requests  
# 使用reqursts中的get方法打开 http://127.0.0.1:8000 把该对象命名为response
response = requests.get('http://127.0.0.1:8000/')
# 打印response对象中的status_code属性 status_code是 状态码
print(response.status_code)
# 打印response对象中的text属性  text是  文本或者说 网页源代码
print(response.text)
```



### 如何从网页源代码中获取需要的信息？？
通常这个过程，称为**解析网页源代码**。  
网页源代码其实就一个文本文件。  
说白了就一个html文件。  
解析html的工具有：re、字符串、bs4、xpath、pyquery、pandas。  
下面我将简单演示re、bs4、xpath、pyquery的解析代码该怎么写。  
下一章节将详细介绍bs4的select方法。  
字符串这里无法使用就不介绍了。  
pandas在后面的scrapy爬虫教学里示范。  

#### re 正则表达式
这是无敌的一种解析方法，无论什么文本都可以使用正则表达式来获取我们想要的信息。  
不过学习成本高，难度高，同时很重。
能不用就不用。  
我的正则一般都是用最无脑写法。  
例如需要获取`<th scope="row"><a href="/chapter/shen">神雕侠侣小说</a></th>`中的`/chapter/shen`和`神雕侠侣小说`。  
正则解析式就写成`<th scope="row"><a href="(.*?)">(.*?)</a></th>`  
把想要的内容替换成`(.*?)`  


```python
# 导入python的第三方库requests
import requests  
# 使用reqursts中的get方法打开 http://127.0.0.1:8000 把该对象命名为response
response = requests.get('http://127.0.0.1:8000/')
# 导入正则表达式方法
import re
# 以最无脑的方式编写正则表达式
req = r'<th scope="row"><a href="(.*?)">(.*?)</a></th>'
# 使用re中的 寻找所有方法，req 正则表达式、 网页源代码、 re.S 换行寻找
book_list = re.findall(req,response.text,re.S)
# 逐步打印出需要获取的内容。
for i in book_list:
    book_name = i[0]
    book_url = i[1]
    print(book_name,book_url)
```

#### bs4
bs4全名Beautiful Soup，中文名 美味的汤。  
这是我最喜欢用的解析方法。我是广东人，有空没事煲个汤。  
不过呢，我一直搞不懂一个问题。  
为什么那么多人一开始都学了find方法而不学select方法？  
select是最无脑的解析方式。详细的教程将在下一章节。  
下面只作为示例。


```python
from bs4 import BeautifulSoup as bs
soup = bs(response.text,'lxml')
for each in soup.select('th a'):
    print(each.text,each['href'])
```


## xpath
全称XML Path Language  
xml文档路径语言
这个解析库的解析式也是非常简单。  
不过我用得很少,写的不是很好。  
下面的是示例（随意写的，不要模仿）


```python
# 导入python的第三方库requests
import requests  
# 使用reqursts中的get方法打开 http://127.0.0.1:8000 把该对象命名为response
response = requests.get('http://127.0.0.1:8000/')
# 从lxml库中 导入 元素树方法。
from lxml import etree
# 使用元素树方法中的HTML方法处理网页源代码。  
response_text = etree.HTML(response.text)
# 使用response_text对象中的xpath方法通过解析式获取内容
book_list = response_text.xpath('//th/a')
# 逐步打印出我们需要的内容
for each in book_list:
    print(each.text,each.xpath('@href')[0])
```


#### pyquery  
pyquery的语法和jQuery很像,我个人很强烈推荐使用这款解析器。  
如果你会jQuery，建议你直接阅读pyquery的[官方文档](https://pythonhosted.org/pyquery/)，相信你很快可以上手。  
只是由于我个人喜欢煲汤，所以不是经常用这款解析器。  
不过，bs4中的select方法和pyquery最后用到的解析式使用一样的写法。  
因为他们都是css选择器。  
至于如何写解析式，下一章节将讲解最无脑写法。  
下面是pyquery的示例。


```python
# 导入python的第三方库requests
import requests  
# 使用reqursts中的get方法打开 http://127.0.0.1:8000 把该对象命名为response
response = requests.get('http://127.0.0.1:8000/')
# 从pyquery导入PyQuery方法 简写成pq
from pyquery import PyQuery as pq
# 使用pq解析器处理我们的网页源代码
html_doc = pq(response.text)
# 通过解析式解析网页，并获取其中的内容
book_list = html_doc('th a').items()
# 逐步打印出获取到的内容
for each in book_list:
    print(each.text(),each.attr['href'])
```

    
