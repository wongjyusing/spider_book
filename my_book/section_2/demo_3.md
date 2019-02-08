
## 函数化代码
回顾一下，我们之前的正常做法：  
如果要完成这样的任务，通常我们的做法是：  
1、 浏览器打开[http://127.0.0.1:8000/](http://127.0.0.1:8000/)，看到有3个版本，每个版本有15本小说。总共有45本小说。  
2、 在桌面上创建一个名为**修订版**的文件夹。  
3、 点击页面上的[神雕侠侣小说](http://127.0.0.1:8000/chapter/shen)，然后在修订版的文件夹创建一个**神雕侠侣小说.txt**文件。   
4 、点击[第一回 风月无情](http://127.0.0.1:8000/detail/shen/1),复制章节名到神雕侠侣小说.txt中，然后复制整个网页中的小说内容。  
5、点击[第二回 故人之子](http://127.0.0.1:8000/detail/shen/2),复制章节名到神雕侠侣小说.txt中，然后复制整个网页中的小说内容。  
6、点击[第三回 求师终南](http://127.0.0.1:8000/detail/shen/3),复制章节名到神雕侠侣小说.txt中，然后复制整个网页中的小说内容。  
……  
把上面的步骤替换成代码：  


```python
import requests
from bs4 import BeautifulSoup as bs
response = requests.get('http://127.0.0.1:8000/')
soup = bs(response.text,'lxml')  
book_list = soup.select('th a')
for each in book_list:
    book_slug = each['href']
    book_url = f'http://127.0.0.1:8000{book_slug}'
    chapter_response = requests.get(book_url)
    chapter_list = bs(chapter_response.text,'lxml')
    for chapter in chapter_list.select('[href^="/detail/"]'):
        print(chapter.text,chapter['href'])
```

像上面这种写法很样衰，而且不能重复利用。  
总结就是：唉，太丑了。  
让我们改写一下上面的代码。  
注释我就不写上去，你们自己补上。  
要求和之前的示例代码一样。  
希望大家认认真真写好注释。  
你们的能力提升速度会更快。  
下面的函数写法直接跳过基本教程。  
采取**通用三层结构的小说网站的爬虫框架**的写法。  
只要大家认认真真理解。  
相信不是很难。

### 打开网页函数
下面的这种写法是升级版。
可以应用到大部分的网站。  
用法在后面会有介绍


```python
import requests

def get_response(url,encoding_type):
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    response = requests.get(url=url,headers=header)
    response.encoding = encoding_type     
    return response

```

### 获取链接名和链接函数  
结合现在的这个网站demo直接把获取章节列表和获取小说正文列表的部分，二合一写法。  


```python
import requests
from bs4 import BeautifulSoup as bs

def get_name_and_link(base_url,urls,item_dict,analytic,item_name,item_slug_name):
    response = get_response(urls,encoding_type)
    soup = bs(response.text,'lxml')
    for each in soup.select(analytic):
        item_dict[item_name] = each.text
        item_dict[item_slug_name] = each['href']
        yield item_dict   
```

### 获取小说正文内容函数
下面很多地方大家肯定一下子无法理解，需要下一章节结合我做出来的框架进行理解。  
你们的任务就是理解以后去写注释


```python
import requests
from bs4 import BeautifulSoup as bs

def get_detail(item_dict,analytic):
    response = get_response(f'{base_url}{item_dict['chapter_slug']}')
    soup = bs(response.text,'lxml')
    content = soup.select(analytic)

    book_name = item_dict['book_name']
    title = item_dict['chapter_name']
    with open(f'{book_name}.txt','a',encoding='utf-8')as txt_file:

      txt_file.write('\n'+title+'\n')
      for line in content:
          txt_file.write(line.text + '\n')
    print(f'{ title } 写入到{ book_name }.txt 完成')

```
