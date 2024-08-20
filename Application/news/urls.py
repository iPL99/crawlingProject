from django.urls import path

from . import views

urlpatterns = [
    path('main', views.main_page, name='main'), # 메인 페이지

    # 영화 목록을 표시해주는 url
    # path('요청할url패턴', '호출할View함수', name='url 패턴에 부여한 이름'),
    path('list/', views.news_list, name='news_list'),
    path('reporter-comparison/', views.reporter_comparison, name='reporter_comparison'),
    ]