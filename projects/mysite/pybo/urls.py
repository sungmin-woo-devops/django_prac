from django.urls import path
from . import views

app_name = 'pybo' # app_name는 네임스페이스를 의미

urlpatterns = [
    # 빈칸인 이유
    # 이미 config/urls.py에서 전체 URL이 pybo/로 시작하고 있기 때문에
    # pybo/가 중복되어서는 안되기 때문이다.
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create')
]