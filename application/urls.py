from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns=[
    url(r'^$', views.home, name='home'),
    url('profile/', views.profile, name='profile'),  
    url(r'^business/', views.business, name='business'),
    url(r'^leave_hood/$', views.leave_neighbourhood, name='leave-hood'),
    url(r'^accounts/register/complete/$', views.join, name='complete'),
    url(r'^join/(\d+)/$', views.join_btn, name='join'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)