from django.conf.urls import *
from django.conf.urls import url
from quizzy import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^home/(?P<city_name_slug>[\w\-]+)/$', views.home, name='home'),
    url(r'^home/(?P<city_name_slug>[\w\-]+)/add_pub/$', views.add_pub, name='add_pub'),
    url(r'^home/(?P<city_name_slug>[\w\-]+)/(?P<pub_name_slug>[\w\-]+)/update_pub/$', views.update_pub,
        name='update_pub'),
    url(r'^home/(?P<city_name_slug>[\w\-]+)/(?P<pub_name_slug>[\w\-]+)/update_quiz/(?P<quiz_id>\d+)/$', views.update_quiz,
        name='update_quiz'),
    url(r'^home/(?P<city_name_slug>[\w\-]+)/(?P<pub_name_slug>[\w\-]+)/add_quiz/$', views.add_quiz, name='add_quiz'),
    url(r'^home/(?P<city_name_slug>[\w\-]+)/(?P<pub_name_slug>[\w\-]+)/$', views.show_pub, name='show_pub'),
    url(r'^like/$', views.like_quiz, name='like_quiz'),
    url(r'^dislike/$', views.dislike_quiz, name='dislike_quiz'),
    url(r'^favorite/$', views.favorite_quiz, name='favorite_quiz'),
    url(r'^accounts/password/change/done/', views.password_change_done, name='password_change_done'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^profile/$', views.profile, name='profile'),

    # url(r'^quizzy/profile/$', views.profile, name='quizzy_profile'),
    url(r'^suggest/$', views.suggest_pub, name='suggest_pub'),
    url(r'^blog/comments/', include('fluent_comments.urls')),
    # url(r'^comments/', include('django_comments.urls')),
]
