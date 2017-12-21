from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^learnmore.html$', views.learnmore, name='learnmore'),
    url(r'^accounts/login/$', login, {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', logout),
]
