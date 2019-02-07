
## bs4的傻瓜教学
现在大家观察一下`http://127.0.0.1:8000/`的网页源代码。  
我们的小说链接的数据是怎样的格式?  
`<a href="/chapter/shen">神雕侠侣小说</a>`    
数据都是在**a**标签里面。   
所以，我们的解析式一定有个`a`。  
尝试运行下方的代码。  


```python
# 导入python的第三方库requests
import requests  
# 使用reqursts中的get方法打开 http://127.0.0.1:8000 把该对象命名为response
response = requests.get('http://127.0.0.1:8000/')
# 从bs4 中导入 BeautifulSoup方法 简写为bs
from bs4 import BeautifulSoup as bs
# 煲汤  使用BeautifulSoup方法处理网页源代码 ，处理方式是lxml
soup = bs(response.text,'lxml')
# 使用 汤 中的选择器方法，我们需要获取这个网页上a标签，那么就写个 a
book_list = soup.select('a')
# 把获取到的内容逐个打印出来，看一下是否是我们想要的内容。
for each in book_list:
    print(each)
```

    <a class="navbar-brand" href="/">金庸小说</a>
    <a class="nav-link" href="/">首页 <span class="sr-only">(current)</span></a>
    <a aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" id="navbarDropdown" role="button">
    小说版本
    </a>
    <a class="dropdown-item" href="/version/1">修订版</a>
    <a class="dropdown-item" href="/version/2">新修版</a>
    <a class="dropdown-item" href="/version/3">旧版</a>
    <a href="/chapter/shen">神雕侠侣小说</a>
    <a href="/chapter/yuan">鸳鸯刀小说</a>
    <a href="/chapter/yi">倚天屠龙记小说</a>
    <a href="/chapter/xiao">笑傲江湖小说</a>
    <a href="/chapter/bi">碧血剑小说</a>
    <a href="/chapter/xia">侠客行小说</a>
    <a href="/chapter/bai">白马啸西风小说</a>
    <a href="/chapter/lian">连城诀小说</a>
    <a href="/chapter/shu">书剑恩仇录小说</a>
    <a href="/chapter/yue">越女剑小说</a>
    <a href="/chapter/xue">雪山飞狐小说</a>
    <a href="/chapter/she">射雕英雄传小说</a>
    <a href="/chapter/fei">飞狐外传小说</a>
    <a href="/chapter/tian">天龙八部小说</a>
    <a href="/chapter/lu">鹿鼎记小说</a>
    <a href="/chapter/nxiao">笑傲江湖小说</a>
    <a href="/chapter/nyuan">鸳鸯刀小说</a>
    <a href="/chapter/nxia">侠客行小说</a>
    <a href="/chapter/ntian">天龙八部小说</a>
    <a href="/chapter/nfei">飞狐外传小说</a>
    <a href="/chapter/nbi">碧血剑小说</a>
    <a href="/chapter/nlu">鹿鼎记小说</a>
    <a href="/chapter/nbai">白马啸西风小说</a>
    <a href="/chapter/nshe">射雕英雄传小说</a>
    <a href="/chapter/nxue">雪山飞狐小说</a>
    <a href="/chapter/nyue">越女剑小说</a>
    <a href="/chapter/nyi">倚天屠龙记小说</a>
    <a href="/chapter/nshu">书剑恩仇录小说</a>
    <a href="/chapter/nshen">神雕侠侣小说</a>
    <a href="/chapter/nlian">连城诀小说</a>
    <a href="/chapter/ofei">飞狐外传小说</a>
    <a href="/chapter/oxia">侠客行小说</a>
    <a href="/chapter/oshe">射雕英雄传小说</a>
    <a href="/chapter/olian">连城诀小说</a>
    <a href="/chapter/otian">天龙八部小说</a>
    <a href="/chapter/oshu">书剑恩仇录小说</a>
    <a href="/chapter/olu">鹿鼎记小说</a>
    <a href="/chapter/oyuan">鸳鸯刀小说</a>
    <a href="/chapter/obai">白马啸西风小说</a>
    <a href="/chapter/obi">碧血剑小说</a>
    <a href="/chapter/oyi">倚天屠龙记小说</a>
    <a href="/chapter/oshen">神雕侠侣小说</a>
    <a href="/chapter/oxue">雪山飞狐小说</a>
    <a href="/chapter/oxiao">笑傲江湖小说</a>
    <a href="/chapter/oyue">越女剑小说</a>
    <a href="https://github.com/wongjyusing">Sing</a>
    <a href="https://www.tornadoweb.org/en/stable">Tornado</a>
    <a href="https://github.com/wongjyusing">
    <b>Sing</b>
    </a>


没有任何悬念，上面不是我们想要的内容。  
这是为什么呢？？  
因为范围太大了，而解析式的约束条件太少了。  
该如何改进呢？？  
我们再次观察网页源代码。   
看一下我们需要的内容的a标签外面的标签是什么？？  
`<th scope="row"><a href="/chapter/yi">倚天屠龙记小说</a></th>`  
不难发现是**th**标签。  
于是乎，加一个条件，解析式改写成`th a`  
尝试执行下方代码：


```python
# 导入python的第三方库requests
import requests  
# 使用reqursts中的get方法打开 http://127.0.0.1:8000 把该对象命名为response
response = requests.get('http://127.0.0.1:8000/')
# 从bs4 中导入 BeautifulSoup方法 简写为bs
from bs4 import BeautifulSoup as bs
# 煲汤  使用BeautifulSoup方法处理网页源代码 ，处理方式是lxml
soup = bs(response.text,'lxml')
# 使用 汤 中的选择器方法，我们需要获取这个网页上a标签，那么就写个 a  
# 由于直接填写a标签会导致很多我们不需要的数据
# 故此添加约束条件 获取 th标签中的a标签。
book_list = soup.select('th a')
# 把获取到的内容逐个打印出来，看一下是否是我们想要的内容。
for each in book_list:
    print(each)
```

    <a href="/chapter/shen">神雕侠侣小说</a>
    <a href="/chapter/yuan">鸳鸯刀小说</a>
    <a href="/chapter/yi">倚天屠龙记小说</a>
    <a href="/chapter/xiao">笑傲江湖小说</a>
    <a href="/chapter/bi">碧血剑小说</a>
    <a href="/chapter/xia">侠客行小说</a>
    <a href="/chapter/bai">白马啸西风小说</a>
    <a href="/chapter/lian">连城诀小说</a>
    <a href="/chapter/shu">书剑恩仇录小说</a>
    <a href="/chapter/yue">越女剑小说</a>
    <a href="/chapter/xue">雪山飞狐小说</a>
    <a href="/chapter/she">射雕英雄传小说</a>
    <a href="/chapter/fei">飞狐外传小说</a>
    <a href="/chapter/tian">天龙八部小说</a>
    <a href="/chapter/lu">鹿鼎记小说</a>
    <a href="/chapter/nxiao">笑傲江湖小说</a>
    <a href="/chapter/nyuan">鸳鸯刀小说</a>
    <a href="/chapter/nxia">侠客行小说</a>
    <a href="/chapter/ntian">天龙八部小说</a>
    <a href="/chapter/nfei">飞狐外传小说</a>
    <a href="/chapter/nbi">碧血剑小说</a>
    <a href="/chapter/nlu">鹿鼎记小说</a>
    <a href="/chapter/nbai">白马啸西风小说</a>
    <a href="/chapter/nshe">射雕英雄传小说</a>
    <a href="/chapter/nxue">雪山飞狐小说</a>
    <a href="/chapter/nyue">越女剑小说</a>
    <a href="/chapter/nyi">倚天屠龙记小说</a>
    <a href="/chapter/nshu">书剑恩仇录小说</a>
    <a href="/chapter/nshen">神雕侠侣小说</a>
    <a href="/chapter/nlian">连城诀小说</a>
    <a href="/chapter/ofei">飞狐外传小说</a>
    <a href="/chapter/oxia">侠客行小说</a>
    <a href="/chapter/oshe">射雕英雄传小说</a>
    <a href="/chapter/olian">连城诀小说</a>
    <a href="/chapter/otian">天龙八部小说</a>
    <a href="/chapter/oshu">书剑恩仇录小说</a>
    <a href="/chapter/olu">鹿鼎记小说</a>
    <a href="/chapter/oyuan">鸳鸯刀小说</a>
    <a href="/chapter/obai">白马啸西风小说</a>
    <a href="/chapter/obi">碧血剑小说</a>
    <a href="/chapter/oyi">倚天屠龙记小说</a>
    <a href="/chapter/oshen">神雕侠侣小说</a>
    <a href="/chapter/oxue">雪山飞狐小说</a>
    <a href="/chapter/oxiao">笑傲江湖小说</a>
    <a href="/chapter/oyue">越女剑小说</a>


得到的结果正确。  
## 提升能力
bs4挺简单的。不过，大家需要学多几种语法来确保以后遇到真正的网站，不会说的到太多的不需要的数据。  
首先，bs4是属于**css选择器**解析器。  
这里有三种基本元素要了解：**标签，class、id、属性**  
### 第一个例子
现在需要获取到小说的版本名，和版本介绍（红字部分）  
```html
<h3 class="version-name"><span>修订版</span>
<font>修订版,也称新版,三联版,流传最广,首次阅读推荐阅读此版本</font>
</h3>
```
假设网页上有很多个h3标签（太懒了，这个demo没做太多的混淆内容）  
解析式`h3 font`和`h3 span`无法使用  
该怎么写呢？？
写法如下：


```python
# 导入python的第三方库requests
import requests  
# 使用reqursts中的get方法打开 http://127.0.0.1:8000 把该对象命名为response
response = requests.get('http://127.0.0.1:8000/')
# 从bs4 中导入 BeautifulSoup方法 简写为bs
from bs4 import BeautifulSoup as bs
# 煲汤  使用BeautifulSoup方法处理网页源代码 ，处理方式是lxml
soup = bs(response.text,'lxml')
# 使用bs4中的css选择器方法，获取所有class=version-name的内容
# 在css中，class是用句号 点 . 来表示
# 在css中  id 是用井号来表示 #
book_versions = soup.select('.version-name')
# 逐步打印内容，来确认我们的解析式是否写对
for each in book_versions:
    # 这里使用了一个新的方法 select_one()
    # 由于可以确认，在.version-name里面的font标签只有一个
    # 如果使用了select()方法，我们获取到的内容是一个对象列表
    # 到时候的代码就要写成version_name = each.select('font')[0].text
    # select_one() 只会返回符合解析式的第一个对象
    # 为了优化代码，选择select_one()方法
    version_name = each.select_one('font').text
    version_introduction = each.select_one('span').text
    print(version_name,version_introduction)
```

    修订版,也称新版,三联版,流传最广,首次阅读推荐阅读此版本 修订版
    最新修订版，新修版，由广州出版社和花城出版社联合出版 新修版
    最初的朗声旧版 报纸连载版 旧版


### 第二个例子
回到我们最初的目标。  
获取首页中小说的链接和书名。  
现在假设我们的解析式`th a` 不能用。(假设有网页上有很多，th标签混淆我们想要的内容，简单来说，不能用th标签)  
那该怎么精准的获取我们想要的数据呢？？  
观察一下，网页源代码：
```html
<tbody>
<tr>
<th scope="row"><a href="/chapter/shen">神雕侠侣小说</a></th>
<td>出版时间：1980年</td>
<td>出版社：三联出版社</td>
</tr>
</tbody>
```  
这个时候，就可以用**属性写法了**  
看下面的例子。  


```python
# 导入python的第三方库requests
import requests  
# 使用reqursts中的get方法打开 http://127.0.0.1:8000 把该对象命名为response
response = requests.get('http://127.0.0.1:8000/')
# 从bs4 中导入 BeautifulSoup方法 简写为bs
from bs4 import BeautifulSoup as bs
# 煲汤  使用BeautifulSoup方法处理网页源代码 ，处理方式是lxml
soup = bs(response.text,'lxml')
# 使用属性解析式来获取内容
# 写法的要点：
    # 首先a标签是必须要有 得出 'a'  
    # 然后写上属性的表示方式  得出'[] a'
    # 写上属性名  得出'[scope] a'
    # 写上属性的内容 得出'[scope=row] a'
book_list = soup.select('[scope=row] a')
# 把获取到的内容逐个打印出来，看一下是否是我们想要的内容。
for each in book_list:
    print(each.text,each['href'])
```

### 第三个例子
直接阅读下面的网页源代码
```html
<tbody>
<tr>
<th scope="row"><a href="/chapter/shen">神雕侠侣小说</a></th>
<td>出版时间：1980年</td>
<td>出版社：三联出版社</td>
</tr>
</tbody>

<tbody>
<tr>
<th scope="row"><a href="/novel/smallleeflyknife">神雕侠侣小说</a></th>
<td>出版时间：1980年</td>
<td>出版社：三联出版社</td>
</tr>
</tbody>

<tbody>
<tr>
<th scope="row"><a href="/txt/shen">神雕侠侣小说</a></th>
<td>出版时间：1980年</td>
<td>出版社：三联出版社</td>
</tr>
</tbody>
```
上面这种情况时有发生。  
网站为了反爬经常会使用js来加载真正的数据。  
而网页源代码会混淆很多的假数据。  
如同第二个的内容中，small、lee、fly、knife，小李飞刀都有。  
这个真的可怕。  
这次，我们需要获取到真正的章节链接该怎么做呢？？  
首先确认我们需要的数据是`/chapter/shen`的形式。  




```python
response_text = """<tbody>
<tr>
<th scope="row"><a href="/chapter/shen">神雕侠侣小说</a></th>
<td>出版时间：1980年</td>
<td>出版社：三联出版社</td>
</tr>
</tbody>

<tbody>
<tr>
<th scope="row"><a href="/novel/smallleeflyknife">神雕侠侣小说</a></th>
<td>出版时间：1980年</td>
<td>出版社：三联出版社</td>
</tr>
</tbody>

<tbody>
<tr>
<th scope="row"><a href="/txt/shen">神雕侠侣小说</a></th>
<td>出版时间：1980年</td>
<td>出版社：三联出版社</td>
</tr>
</tbody>

                """
from bs4 import BeautifulSoup as bs
# 煲汤  使用BeautifulSoup方法处理网页源代码 ，处理方式是lxml
soup = bs(response_text,'lxml')
# 使用属性解析式来获取内容
# 写法的要点：
    # 写上属性的表示方式  得出'[]'
    # 写上属性名  得出'[href]'
    # 由于是需要以chapter开头 小说名字拼音结束的类型，得出 [href^="/chapter/"]
    # href^ 这种属于是bs4中的正则表达式用法

    # 在这里href^="/chapter/"  匹配任何以/chapter/开头的数据
    # 在这里href$="shen"  匹配任何以 shen 结束的数据
    # 在这里href*="txt"  匹配含有 txt 的数据

    # 大家可以把上面的例子替换一下 下面的解析式 感受一下

book_list = soup.select('[href^="/chapter/"]')
# 把获取到的内容逐个打印出来，看一下是否是我们想要的内容。
for each in book_list:
    print(each.text,each['href'])
```

    神雕侠侣小说 /chapter/shen


## 进阶  
学习bs4的形式，最好是直接阅读[bs4的官方文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors)  
除了学习bs4 还需要学习其他解析方法。  
没有最好的解析方法，只有最适合的解析方法。  
我这里说一个bs4的缺点吧。  
如果你遇到的网站是**gbk**编码的话，绝对不要使用bs4来进行解析网页。  
很大可能会出现短斤缺两的现象。  
原因是一些编码问题，`\u3000`之类导致的。  

在合适的环境选择合适的网页解析方法是非常重要的。  
下面，我将演示使用pandas获取[127.0.0.1:8000/](http://127.0.0.1:8000/)上的小说数据。  
任务需求：
把首页上的数据生成一个我们python中的字典。  
要求：
根据版本号把页面上的数据整合成一个**大字典**。  
具体运行下面的代码就知道了。  


```python
import pandas as pd
import requests  
from bs4 import BeautifulSoup as bs
response = requests.get('http://127.0.0.1:8000/')

soup = bs(response.text,'lxml')
version_dict = {}
version_index = 0
version_content = soup.select('.version-content')
for each in version_content:
    version_name = each.select_one('h3 span').text
    version_introduction = each.select_one('h3 font').text
    novel_data = pd.read_html(response.text)[version_index]
    novel_dict = novel_data.to_dict(orient='index')
    books = version_content[version_index].select('th a')
    book_count = len(books)
    for book_num in range(0,book_count):
        novel_dict[book_num]['网页链接'] = books[book_num]['href']
        #print(books[book_num]['href'])
    novel_dict
    version_dict[version_index] = {'版本名':version_name,'版本介绍':version_introduction,'小说列表':novel_dict}
    version_index+=1
print(version_dict)
```


上面的代码可以生成一个大字典方便我们资料的调用。  
上面的注释我就删掉了。  
以后大家等能力提高后，再写上去。  
我演示pandas的用法并不是说pandas很强。  
只是想告诉大家，每一种解析器都要学，在合适的时机选择合适的解析器。  
甚至，有些时候，我们还需要调用其他语言或工具来辅助爬虫获取信息。  
有机会，我会做一些更复杂的网站给大家进行练习，强迫大家使用更多的方法、语言来实现爬取。  
