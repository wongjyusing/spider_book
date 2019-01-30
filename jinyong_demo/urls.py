from views import index
from tornado.web import url
urlpatterns = [
    url(r'/', index.IndexHandler, name='home'),
    url(r'/chapter/(?P<slug>[\w-]+)', index.ChapterHandler, name='chapter'),
    url(r'/version/(?P<id>[\w-]+)', index.VerstionHandler, name='version'),
    url(r'/detail/(?P<slug>[\w-]+)/(?P<page>[\w-]+)', index.DetailHandler, name='detail'),
    # url(r'/detail/(?P<slug>[\w-]+)', index.DetailHandler,name='detail'),
    # url(r'/tags/(?P<slug>[\w-]+)', index.AllTagHandler,name='tags'),
]
