from django.urls import path, include
from users import views as user_views



urlpatterns = [

    path('user_list/', user_views.users),
    path('signup/',user_views.signup),
    path('login/', user_views.login),
    path('id_overlap/',user_views.id_overlap),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
