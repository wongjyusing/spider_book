
## 怎么写爬虫程序？
写爬虫程序前，先思考，你需要获取这个网站的什么信息？  
以一开始，我介绍什么是爬虫的任务为例：
### 任务  
现在有个任务给你：  
把在[http://127.0.0.1:8000/](http://127.0.0.1:8000/)上看到的所有小说（一共有45本）  
按照版本生成一个文件夹（修订版、新修版、旧版）  
然后根据书名生成一个txt文件（神雕侠侣.txt、射雕英雄传.txt、天龙八部.txt、小李飞刀.txt）  
最后通过复制粘贴成45本完整的小说。  

上面的任务简单来说就是：  
把这个网站上的小说保存成txt文件  

再回头看看我们正常的做法：
### 正常做法
如果要完成这样的任务，通常我们的做法是：  
1、 浏览器打开[http://127.0.0.1:8000/](http://127.0.0.1:8000/)，看到有3个版本，每个版本有15本小说。总共有45本小说。  
2、 在桌面上创建一个名为**修订版**的文件夹。  
3、 点击页面上的[神雕侠侣小说](http://127.0.0.1:8000/chapter/shen)，然后在修订版的文件夹创建一个**神雕侠侣小说.txt**文件。   
4 、点击[第一回 风月无情](http://127.0.0.1:8000/detail/shen/1),复制章节名到神雕侠侣小说.txt中，然后复制整个网页中的小说内容。  
5、点击[第二回 故人之子](http://127.0.0.1:8000/detail/shen/2),复制章节名到神雕侠侣小说.txt中，然后复制整个网页中的小说内容。  
6、点击[第三回 求师终南](http://127.0.0.1:8000/detail/shen/3),复制章节名到神雕侠侣小说.txt中，然后复制整个网页中的小说内容。  
……  

爬虫程式怎么写？？  
就根据上面的正常做法来写。   
大家可以把上面的正常做法当成**伪代码**  

## 分析一个网站  
请大家，按照上面的步骤做一次，感受一下流程。（记得使用浏览器的隐身窗口，养成良好的习惯。别真的做完，就6个步骤做一下）  
除了打开首页的步骤以外。（小说的章节页面和详情页面使用 右键，打开新的标签页）  

现在我们的隐身窗口哪里有5个标签页。  
观察一下这5个标签页。  
是因为什么原因导致这5个标签页的内容不同？？  
是**地址**   
首页：`http://127.0.0.1:8000/`  
神雕侠侣小说：`http://127.0.0.1:8000/chapter/shen`  
第一回 风月无情：`http://127.0.0.1:8000/detail/shen/1`  
第二回 故人之子：`http://127.0.0.1:8000/detail/shen/2`  
第三回 求师终南：`http://127.0.0.1:8000/detail/shen/3`  

把标签页切换到这个网站的首页。  
为什么我们点击网页上的**神雕侠侣**链接会导致浏览器会打开一个新的标签页呢？？  
大家把鼠标移动到链接上。  
可以发现浏览器的左下角会出现一个地址。  
`http://127.0.0.1:8000/chapter/shen`   
也就是说，我们需要获取到`chapter/shen`和我们的首页`http://127.0.0.1:8000`进行字符拼接。  
就可以得到神雕侠侣小说的章节页面。  

那么，`chapter/shen`在哪里呢？？  
把标签页切换到这个网站的首页。 右键 查看网页源代码。  
就会打开一个新的标签页  
我们按下`Ctrl` + `F`  
输入`chapter/shen`  
就可以发现原来我们所有的小说的章节链接都是被下面的这种html代码包裹住。  
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
<th scope="row"><a href="/chapter/yuan">鸳鸯刀小说</a></th>
<td>出版时间：1980年</td>
<td>出版社：三联出版社</td>
</tr>
</tbody>

<tbody>
<tr>
<th scope="row"><a href="/chapter/yi">倚天屠龙记小说</a></th>
<td>出版时间：1980年</td>
<td>出版社：三联出版社</td>
</tr>
</tbody>
```
至于怎么获取到里面的链接留到下一个小节再讲。  

继续分析这个网站。  
我们打开`http://127.0.0.1:8000/chapter/shen`  
找一下，小说的详情页的链接在哪里？
右键，查看网页源代码   
我们按下`Ctrl` + `F`  
输入`detail/shen/1`   
可以发现，我们小说的内容页的链接是被下面的html代码包裹中的：
```html
<li><a href="/detail/shen/1">第一回 风月无情</a></li>

<li><a href="/detail/shen/2">第二回 故人之子</a></li>

<li><a href="/detail/shen/3">第三回 求师终南</a></li>

<li><a href="/detail/shen/4">第四回 全真门下</a></li>

<li><a href="/detail/shen/5">第五回 活死人墓</a></li>

<li><a href="/detail/shen/6">第六回 玉女心经</a></li>
```  

继续分析我们的小说内容页。  
打开`http://127.0.0.1:8000/detail/shen/1`  
右键，查看网页源代码   
可以发现我们的小说内容都是被下面的html代码包裹中的：
```html
<p>“越女采莲秋水畔，窄袖轻罗，暗露双金钏。</p>

<p>照影摘花花似面，芳心只共丝争乱。</p>

<p>鸡尺溪头风浪晚，雾重烟轻，不见来时伴。</p>

<p>隐隐歌声归掉远，离愁引看江南岸。”</p>

<p>一阵轻柔婉转的歌声，飘在烟水蒙蒙的湖面上。歌声发自一艘小船之中，船里五个少女和歌嘻笑，荡舟采莲。她们唱的曲子是北宋大词人欧阳修所作的“蝶恋花”词，写的正是越女采莲的情景，虽只寥寥六十字，但季节、时辰、所在、景物以及越女的容貌、衣着、首饰、心情，无一不描绘得历历如见，下半阕更是写景中有叙事，叙事中夹抒情，自近而远，余意不尽。欧阳修在江南为官日久，吴山越水，柔情蜜意，尽皆融入长短句中。宋人不论达官贵人，或是里巷小民，无不以唱词为乐，是以柳永新词一出，有井水处皆歌，而江南春岸折柳，秋湖采莲，随伴的往往便是欧词。</p>
```
在下一小节，将介绍如何使用python打开一个网页和获取页面上我们想要的信息。
