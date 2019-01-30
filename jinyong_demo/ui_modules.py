from tornado.web import UIModule
from views.db_sql_class import BaseHandler

class RightCard(UIModule,BaseHandler):
    def render(self,items):

        context = items
        return self.render_string("modules/right_card.html", context=context)
