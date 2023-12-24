from django.urls import path
from .views import signup, user_login, user_logout, user_edit

app_name = "accounts"

urlpatterns = [
    path('signup/', signup, name ="signup"),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('user_edit/', user_edit, name="user_edit")
]