from tornado.web import RequestHandler
from .db_sql_class import BaseHandler
from .book_bypass import bypass


class IndexHandler(BaseHandler):
    def get(self):


        self.render(template_name='index.html',context=bypass)

class VerstionHandler(BaseHandler):
    def get(self,id):
        id = self.cheak_id(id)
        if id == None:
            self.render(template_name='404.html')
        else:
            context,book_data = self.get_version_alone_data(id[0])
            print(context)
            self.render(template_name='verstion.html',context=context,book_data=book_data)

class ChapterHandler(BaseHandler):
    def get(self,slug):

        slug = self.cheak_slug(slug)
        print(slug)
        if slug == None:
            self.render(template_name='404.html')
        else:
            book_data = self.get_book_data(slug[0])
            context = self.get_chapter_data(slug[0])

            self.render(template_name='chapter.html',context=context,book_data=book_data)

class DetailHandler(BaseHandler):
    def get(self,slug,page):
        slug = self.cheak_slug(slug)

        if slug == None:
            self.render(template_name='404.html')
        else:
            print(slug,page)
            page = self.cheak_page(slug[0],page)
            if page == None:
                self.render(template_name='404.html')
            else:
                book_data = self.get_book_data(slug[0])
                context,chapter_name = self.get_detail_data(slug[0],page[0])
                book_data['chapter_name'] = chapter_name
                print(book_data)
                self.render(template_name='detail.html',context=context,book_data=book_data)
