from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
=======
    url(r'^aipyweb/latest\.html$', views.index),
>>>>>>> 1a7ce2e7043b9ae5bf06962fad6c4dcf27f3b183
]
