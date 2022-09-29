
from django.urls import path
from.views import article_list,art_detail,Artapiview,Detailview,Generic



urlpatterns = [
    # path('art/',article_list),
    # path('detail/<int:pk>/',art_detail),
    path('detail/<int:id>/',Detailview.as_view()),
    path('art/', Artapiview.as_view()),
    path('gen/art/<int:id>/',Generic.as_view()),
]
