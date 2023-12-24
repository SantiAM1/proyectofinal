from django.urls import path
from .views import ListaPages, DetailPage, about, plataforma, PageCreateView, PageDeleteView, ListPost, PageUpdateView


app_name = "pages"

urlpatterns = [
    path('', ListaPages.as_view(), name ="pagelist"),
    path('post/<pk>', DetailPage.as_view(), name="postdetail"),
    path('about/', about, name ="about"),
    path('plataforma/', plataforma, name="plataforma"),
    path('createpost/', PageCreateView.as_view(), name="createpost"),
    path('lista', ListPost.as_view(), name="listaplat" ),
    path('delete/<pk>', PageDeleteView.as_view(), name="deletepost"),
    path('update/<pk>', PageUpdateView.as_view(), name="updatepost")
]

