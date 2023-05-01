from django.urls import path
from .views import news_list, news_detail

urlpatterns = [
    path('news/', news_list, name='all_news_list'),
    path('<int:id>/', news_detail, name="news_detail_page")
]