from django.urls import path, include
from users import views as user_views
from webtoons import views as webtoon_views
from news import views as news_views
from history import views as history_views
from youtube import views as you_views

urlpatterns = [

    path('user_list/', user_views.users),
    path('signup/', user_views.signup),
    path('login/', user_views.login),
    path('id_overlap/', user_views.id_overlap),
    path('daumwebtoon/', webtoon_views.daumwebtoon),
    path('naverwebtoon/', webtoon_views.naverwebtoon),
    path('navernews/', news_views.news),
    path('history/', history_views.hisotry),

    path('recommend_nt/', history_views.recomend_naver),
    path('recommend_dt/', history_views.recomend_daum),
    path('recommend_yt/', history_views.recomend_youtube),
    path('recommend_news/', history_views.recomend_news),
    
    path('history_dt/', history_views.history_daum),
    path('history_nt/', history_views.history_naver),
    path('history_news/', history_views.history_news),
    path('history_yt/', history_views.history_youtube),

    path('youtube/',you_views.youtube),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
