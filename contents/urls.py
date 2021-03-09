from django.urls import path, include
from users import views as user_views
from webtoons import views as webtoon_views
from news import views as news_views


urlpatterns = [

    path('user_list/', user_views.users),
    path('signup/', user_views.signup),
    path('login/', user_views.login),
    path('id_overlap/', user_views.id_overlap),
    path('daumwebtoon/', webtoon_views.daumwebtoon),
    path('naverwebtoon/', webtoon_views.naverwebtoon),
    path('navernews/', news_views.news),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
