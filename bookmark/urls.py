from django.urls import path
from .views import *

app_name = 'bookmark'

urlpatterns = [
    path('', list, name='list'), # '':아무것도 없는 첫 main 화면에 list: 라는 view 함수를 실행해라. 이 주소를 찾고 싶다면 list라는 이름으로 불러라.
    path('new/', new, name='new'),
    path('edit/<int:pk>', edit, name='edit'), # edit라는 path로 받을 때 bookmark의 고유한 번호 PK를 변수로 받아와서 
    path('delete/<int:pk>', delete, name='delete'),
]