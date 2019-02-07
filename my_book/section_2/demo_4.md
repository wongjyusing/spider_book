
## 三层结构的小说网站爬取通用框架
在关键点我会写上说明，大家后续需要的是 理解和写注释  


```python
import requests
from bs4 import BeautifulSoup as bs

def get_response(url,encoding_type):
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    response = requests.get(url=url,headers=header)
    response.encoding = encoding_type     
    return response

def get_name_and_link(base_url,urls,item_dict,analytic,item_name,item_slug_name):
    response = get_response(urls,encoding_type)
    soup = bs(response.text,'lxml')
    for each in soup.select(analytic):
        item_dict[item_name] = each.text
        item_dict[item_slug_name] = each['href']
        yield item_dict

def get_detail(item_dict,analytic):
    response = get_response(f'{base_url}{item_dict["chapter_slug"]}',encoding_type)
    soup = bs(response.text,'lxml')
    content = soup.select(analytic)

    book_name = item_dict['book_name']
    title = item_dict['chapter_name']
    with open(f'{book_name}.txt','a',encoding='utf-8')as txt_file:
    #设置文件编码，避免写入时乱码
    # 每一次写入章节名时进行换行
        txt_file.write('\n'+title+'\n')
        for line in content:
            txt_file.write(line.text + '\n')
    print(f'{ title } 写入到{ book_name }.txt 完成')

# 基础url 通常我们都会遇到相对路径的网页结构，所以需要基础url进行拼接
# 如果是 绝对路径 那就写成空字符串
base_url = 'http://127.0.0.1:8000'

# 需要爬取的url
urls = 'http://127.0.0.1:8000'

# 网站编码，大多数中文网站都是utf-8或gbk编码
encoding_type = 'utf-8'

# 书名列表解析式，一般是用在网站首页，用于获取书名和章节列表的网页后缀
book_analytic = 'th a'

# 章节列表解析式

chapter_analytic = '[href^="/detail/"]'

# 详情列表解析式
detail_analytic = '.detail-content p'    

# 主函数
def main():
    items = {}
    book_list = get_name_and_link(base_url,urls,items,book_analytic,'book_name','book_slug')
    for each in book_list:
        book_url = f'{base_url}{each["book_slug"]}'
        chapter_dict = get_name_and_link(base_url,book_url,items,chapter_analytic,'chapter_name','chapter_slug')
        for each in chapter_dict:
            get_detail(each,detail_analytic)
main()
```



上面的代码，只会保存成15本小说，不能按照版本名进行分目录来保存。  
原因是我们没有指定到路径到`get_detail`函数。  
具体如何给到它保存路径  
我给出几个思路，大家自己想办法实现。  

1、 利用列表切片，手动创建三个目录，把从首页换取到的book_list进行切片后，在get_detail函数添加目录的路径。  
重复三次后，方可实现按照版本来保存小说文件。（不推荐）  
2、 改写get_name_and_link函数。在函数中添加一个获取版本名的代码。传参给get_detail函数，让其实现分目录保存小说文件。  
3、 不从首页入手，从**按版本分类的书名列表**开始爬取（有规则的，很建议大家试试）  
4、 利用之前介绍过的pandas解析法进行全站爬取。（建议有爬虫基础的试一试）  
5、 生成一个版本号的列表或者字典，利用索引的形式在框架中实现自动生成目录和传参给get_detail函数。  
6、 理解这个框架的思路，写出自己的代码（极力推荐，自己的才是最好的）  
……    
还有两三种思路，自己思考吧。  
## 框架的使用
这个框架的用法很简单，把代码中的：
```python
base_url = 'http://127.0.0.1:8000'

# 需要爬取的url
urls = 'http://127.0.0.1:8000'

# 网站编码，大多数中文网站都是utf-8或gbk编码
encoding_type = 'utf-8'

# 书名列表解析式，一般是用在网站首页，用于获取书名和章节列表的网页后缀
book_analytic = 'th a'

# 章节列表解析式

chapter_analytic = '[href^="/detail/"]'

# 详情列表解析式
detail_analytic = '.detail-content p'   
```
替换成正确的内容就可以使用。    


## 举个例子

爬取[金庸作品集](http://jinyong.zuopinj.com/)  
我们只需要改写框架中下面的内容即可爬取：
```python
base_url = ''

# 需要爬取的url
urls = 'http://jinyong.zuopinj.com'

# 网站编码，大多数中文网站都是utf-8或gbk编码
encoding_type = 'utf-8'

# 书名列表解析式，一般是用在网站首页，用于获取书名和章节列表的网页后缀
book_analytic = '#cols-1 h3 a'

# 章节列表解析式

chapter_analytic = '.book_list a'

# 详情列表解析式
detail_analytic = '#htmlContent p'  
```  


```python
import requests
from bs4 import BeautifulSoup as bs

def get_response(url,encoding_type):
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    response = requests.get(url=url,headers=header)
    response.encoding = encoding_type     
    return response

def get_name_and_link(base_url,url,item_dict,analytic,item_name,item_slug_name):
    response = get_response(url,encoding_type)
    soup = bs(response.text,'lxml')
    for each in soup.select(analytic):
        item_dict[item_name] = each.text
        item_dict[item_slug_name] = each['href']
        yield item_dict

def get_detail(item_dict,analytic):
    response = get_response(f'{base_url}{item_dict["chapter_slug"]}',encoding_type)
    soup = bs(response.text,'lxml')
    content = soup.select(analytic)

    book_name = item_dict['book_name']
    title = item_dict['chapter_name']
    with open(f'{book_name}.txt','a',encoding='utf-8')as txt_file:
    #设置文件编码，避免写入时乱码
    # 每一次写入章节名时进行换行
        txt_file.write('\n'+title+'\n')
        for line in content:
            txt_file.write(line.text + '\n')
    print(f'{ title } 写入到{ book_name }.txt 完成')

# 基础url 通常我们都会遇到相对路径的网页结构，所以需要基础url进行拼接
# 如果是 绝对路径 那就写成空字符串
base_url = ''

# 需要爬取的url
#urls = 'http://jinyong.zuopinj.com'
urls = 'http://gulong.zuopinj.com'
# 网站编码，大多数中文网站都是utf-8或gbk编码
encoding_type = 'utf-8'

# 书名列表解析式，一般是用在网站首页，用于获取书名和章节列表的网页后缀
book_analytic = '#cols-1 h3 a'

# 章节列表解析式

chapter_analytic = '.book_list a'

# 详情列表解析式
detail_analytic = '#htmlContent p'      

# 主函数
def main():
    items = {}
    book_list = get_name_and_link(base_url,urls,items,book_analytic,'book_name','book_slug')
    for each in book_list:
        book_url = f'{base_url}{each["book_slug"]}'
        chapter_dict = get_name_and_link(base_url,book_url,items,chapter_analytic,'chapter_name','chapter_slug')
        for each in chapter_dict:
            get_detail(each,detail_analytic)
main()
```


嘿嘿嘿，是不是很爽？  
一下子获取到了15本小说。  
尝试一下把上面的urls改写成`urls = 'http://gulong.zuopinj.com'`   
运行代码。  
嘿嘿嘿,80本小说到手。  
## 注意  
不要高兴太早，大家有没有发现一个问题。  
爬取我写的这个网站速度很快，而现在爬取互联网上的网站很慢啊？？  
这是为什么呢？？  
因为我写的这个网站是运行在本地，而其他的网站是在互联网上。  
但是这个框架爬取速度是在是太慢了。（我的这个小框架是单线程）  
想要更快的话，我们需要多线程，多进程等技术来让爬虫以更快的速度来快速爬取数据。  
这个方面的话，自己去谷歌。  
## 后续  
后续将介绍scrapy框架。敬请期待。  
现在是2019年的2月8号。  
下一次的scrapy教学没什么意外的话，会在2019年3月份放出。  
在此之前，希望大家对数据库有所了解。  
最好是postgresql数据库。
