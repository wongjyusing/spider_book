## 学习爬虫的错误方法  
0、 遇到问题不谷歌不百度。  
1、 边看视频边抄代码。  
2、 看不懂代码就抄十遍代码，直到看懂为止。  
3、 抄来的代码运行不成功就再抄一遍。  
4、 写代码，不思考，只会抄。  
## 学习的正确姿势  
下面是我悟出来的学习方法，学习python的web开发也通用：  
0、 遇到问题自行谷歌解决问题，实在无法解决再去问人。  
1、 以爬虫的教学视频为例，看视频不敲任何代码，先理解这个视频的**开发思路**，怎么爬，怎么分析网站，而不是去看代码怎么写。看完以后，尝试自己分析网页构造，尝试用自己的方式写爬虫代码。  
2、 拿到一份可用的代码不是怎么去抄它，而是看代码，然后写注释，把整份代码的开发思路，运行过程全部写上注释，如同下面的例子。  
```python
# 从Django的快捷方法中导入 渲染、要么获取对象要么404方法
from django.shortcuts import render,get_object_or_404
# 从当前目录下的models.py中导入Blog类
from .models import Blog

# 所有博客列表方法 首页的处理方法
def blog_list(request):
    context = {}   # 生成一个空字典，用于装载内容
    context['blogs'] = Blog.objects.all() # 获取Blog中的所有对象

    # request 请求 意思是当我们在浏览器中访问 http://127.0.0.1:8000
    # 就相当于发送了一个请求给Django，当请求成功后
    # django就把context的内容在blog_list.html中渲染并返回给这个请求。
    return render(request,'blog_list.html',context)

# 文章详情页内容的处理方法
def blog_detail(request,slug): # 接收请求和slug参数
    context = {}  # 生成一个空字典,用于装载内容

    # 在Blog也就是我们的数据库中寻找有没有slug字段和传进来的slug字段匹配的
    # 没有，则返回404,有则返回该对象的内容
    context['blog'] = get_object_or_404(Blog, slug=slug)
    # 把context的内容在blog_detail.html中渲染，并返回该请求给用户
    return render(request,'blog_detail.html',context)
```
上面是我以前学习django的时候写的注释，这里算少了。  
刚开始学习爬虫写过的写的代码文件里面的注释更多。   
我可以很自豪的说，我python、javascript、ruby、css 、html、ruby的代码量不超过15000行。  
而我写过的注释超过5万多行。  
理解一份代码永远比抄代码重要。  
3、 每隔一两个月，回头看一下之前写过的代码。尝试重构一次代码。  
下面是我写出的第一条爬虫代码：
```python
import urllib.request
import os
import re

def url_open(url):#网页打开函数，以防被禁
    req = urllib.request.Request(url)
    req.add_header('User-Agent',"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36")
    response = urllib.request.urlopen(url)
    html = response.read()

    return html

def get_url(url):#获得章节数
    html = url_open(url).decode('gbk')

    reg = r'<a href="/cang/(.*?).html">.*?</a>'
    html = re.findall(reg, html)

    return html




def txt_book(chapter):#正文函数
    html = url_open(chapter).decode('gbk')
    reg = r'<div class="nr_con">(.*?)<div class="syz">'
    txtbook = re.findall(reg, html, re.S)
    print(txtbook)
    return txtbook

def save_book(folder,getbook):#保存正文函数

    file = open("cang.txt", 'a')

    file.writelines(getbook)#个人感觉这里应该是少了个参数，但找不到该用什么来保存全本小说。
    file.close()
def down_txt(folder='txtbook',page=1):#这是主函数
    os.mkdir(folder)
    os.chdir(folder)
    os.mknod("cang.txt")
    url = 'http://www.gulongwang.com/cang/'
    txt_num = get_url(url)#获得章节数
    url_num =int(len(txt_num))
    i=0
    print(url_num)
    while i!=url_num:


        for a in txt_num:

            print(a)


            chapter = url + a +'.html'#拼接小说正文url

            print(chapter)#打印小说url，测试程序
            getbook = txt_book(chapter)
            save_book(folder, getbook)
            i += 1
```
虽然，代码真的很样衰，爬取下来的小说带有html的标签。  
但是，这份代码除了在保存txt文件的方面问了一下人，其他都是完全靠自己观察网页，不断的谷歌在写代码过程中的问题，完完全全靠自己解决。  
我每隔一段时间，就会重构一次上面的代码。  
今天，我想爬这种**三层结构的小说网站**（书名列表页、章节列表页，小说详情页）。
只需要填写6个信息（需要爬取的链接、是否为绝对路径、网站的编码格式、书名列表的解析式、章节列表的解析式，小说详情的解析式），到我写好的一个爬虫框架以后，即可实现全站爬取。   

这个框架在最后会让大家参考一下。
