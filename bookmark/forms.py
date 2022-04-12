# urls.py에서 만들고 views.py에서 작동시키는데 forms.py의 내용을 가져다가 사용하는 흐름!

from django import forms
from .models import Bookmark

class BookmarkForm(forms.ModelForm):
    site_name = forms.CharField(label='사이트명')
    url = forms.CharField(label='주소')

    class Meta: # 클래스 전체의 옵션을 잡아주는 역할
        model = Bookmark
        fields = '__all__'