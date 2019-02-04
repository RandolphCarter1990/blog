from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.views import BaseView,ArticlePage
from django.conf import settings

from . import views

urlpatterns = [
    path('', BaseView.as_view(), name='index'),
    path('article/<int:article_id>/', ArticlePage.as_view(), name='article'),    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


  

