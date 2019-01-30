from tornado.web import RequestHandler

from .book_bypass import bypass
class BaseHandler(RequestHandler):
    def cheak_id(self,id):
        sql = "SELECT id FROM version_list WHERE id=?;"
        self.application.db.execute(sql,(id,))
        content_list = self.application.db.fetchone()
        return content_list

    def get_version_alone_data(self,id):
        sql = f"SELECT id,version_name,version_info FROM version_list WHERE id=?;"
        self.application.db.execute(sql,(id,))
        content_list = self.application.db.fetchone()
        id,version_name,version_info = content_list[0],content_list[1],content_list[2]
        version_dict = {'id':id,'version_name':version_name,'version_info':version_info}

        sql = 'SELECT book_name,book_slug,book_info,book_time,version_id FROM book_list WHERE version_id = ?;'
        self.application.db.execute(sql,(id,))
        content_list = self.application.db.fetchall()
        books_dict = {}
        for each in content_list:
            book_name,book_slug,book_info,book_time,version_id = each[0],each[1],each[2],each[3],each[4]
            books_dict[book_slug] = {'book_name':book_name,'book_info':book_info,'book_time':book_time,'version_id':version_id}

        return version_dict,books_dict

    def get_version_data(self):
        sql = 'SELECT id,version_name,version_info FROM version_list;'
        self.application.db.execute(sql)
        version_list = self.application.db.fetchall()
        version_dict = {}
        for each in version_list:
            id,version_name,version_info = each[0],each[1],each[2]
            version_dict[id] = {'version_name':version_name,'version_info':version_info}

        return version_dict


    def get_booklist_data(self):
        sql = 'SELECT book_name,book_slug,book_info,book_time,version_id FROM book_list;'
        self.application.db.execute(sql)
        content_list = self.application.db.fetchall()
        books_dict = {}
        for each in content_list:
            book_name,book_slug,book_info,book_time,version_id = each[0],each[1],each[2],each[3],each[4]
            books_dict[book_slug] = {'book_name':book_name,'book_info':book_info,'book_time':book_time,'version_id':version_id}

        return books_dict


    def cheak_slug(self,slug):
        sql = "SELECT DISTINCT book_slug FROM book_list WHERE book_slug=?;"
        self.application.db.execute(sql,(slug,))
        content_list = self.application.db.fetchone()
        return content_list

    def get_chapter_data(self,slug):
        #slug = f'chapter_{slug}'
        sql = f"SELECT chapter_num,chapter_name FROM chapter_{slug};"
        self.application.db.execute(sql)
        content_list = self.application.db.fetchall()
        chapter_dict = {}
        for i in content_list:
            chapter_dict[i[0]] = i[1]


        return chapter_dict

    def get_book_data(self,slug):
        sql = "SELECT DISTINCT book_name,book_slug,book_info,book_time,version_id FROM book_list WHERE book_slug=?;"
        self.application.db.execute(sql,(slug,))
        contents = self.application.db.fetchone()
        book_name,book_slug,book_info,book_time,version_id = contents[0],contents[1],contents[2],contents[3],contents[4]

        sql = f'SELECT id,version_name,version_info FROM version_list WHERE id={version_id};'
        self.application.db.execute(sql)
        version = self.application.db.fetchone()
        id,version_name,version_info = version[0],version[1],version[2]

        book_data = {
            'book_name':book_name,
            'book_slug':book_slug,
            'book_info':book_info,
            'book_time':book_time,
            'version_id':version_id,
            'version_name':version_name,
            'version_info':version_info

        }
        return book_data

    def cheak_page(self,slug,page):
        sql = f"SELECT chapter_num FROM chapter_{slug} WHERE chapter_num={page};"

        self.application.db.execute(sql)
        content_list = self.application.db.fetchone()
        return content_list


    def get_detail_data(self,slug,page):
        sql = f'SELECT chapter_name FROM chapter_{slug} WHERE chapter_num={page};'
        self.application.db.execute(sql)
        chapter_name = self.application.db.fetchone()[0]

        sql = f'SELECT line_num,line_content FROM detail_{slug}_{page};'
        self.application.db.execute(sql)
        content_list = self.application.db.fetchall()
        chapter_dict = {}
        for i in content_list:
            chapter_dict[i[0]] = i[1]

        return chapter_dict,chapter_name
