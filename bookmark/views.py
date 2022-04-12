from django.shortcuts import render, redirect, get_object_or_404
# redirect : 함수의 내용이 다 수행되고 나서 마지막으로 가야할 페이지 정의
# get_object_or_404 : 내용을 가져올 때 원하는 내용이 없다면 404 뿌려줌
# urls.py에서 여기 있는 함수들 호출할 거야

from .models import Bookmark
from .forms import BookmarkForm

def list(request):
    list = Bookmark.objects.all() # bookmark에서 전체 내용을 가져와

    return render(request, 'bookmark/list.html', {
        'list':list, # html 파일에 리스트 보낼게
    })

def new(request):
    if request.method == 'POST': # POST 방식으로 값을 받았다면 데이터베이스와 연동시켜서 폼으로 받은 내용을 데이터베이스 필드에 집어넣는다. 
        form = BookmarkForm(request.POST) # 북마크 폼 생성
        if form.is_valid(): # 이 내용이 있다면
            bookmark = Bookmark() # 북마크 객체 생성
            bookmark.site_name = form.cleaned_data['site_name'] # 폼으로 받은 이름으로 정의
            bookmark.url = form.cleaned_data['url']
            bookmark.save()
            return redirect('bookmark:list') # (1) 이 bookmark는 (2) list는
    else:
        form = BookmarkForm() # 최초의 페이지를 열었다면 빈 form 태그가 나올 것이고,
    return render(request, 'bookmark/new.html',{
        'form':form,
    })
'''
urls.py 파일
app_name = 'bookmark' (1) app_name을 의미하고,

urlpatterns = [
    path('', list, name=list), (2) list라는 이름의 path name 의미한다.
    path('new/', new, name=new),
    path('edit/<int:pk>', edit, name=edit), 
    path('delete/<int:pk>', delete, name=delete)),
]
'''

def edit(request, pk): # 수정할 때는 아무 글이나 수정하면 안 되기 때문에 bookmark의 고유한 값 pk 를 받아서 수정할 것
    bookmark = get_object_or_404(Bookmark, pk=pk) # 전달 받은 pk 값이 없다면 404 에러 페이지를 뿌려줄 것

    if request.method == 'POST':
        form.BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.url = form.cleaned_data['url']
            bookmark.save()
            return redirect('bookmark:list')
    else:
        form = BookmarkForm(instance=bookmark) # 수정 전 기본 페이지 보여짐
    return render(request, 'bookmark/edit.html', {
        'bookmark':bookmark, 
        'form':form,
    })            


def delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)

    if request.method == 'POST':
        bookmark.delete()
        returnredirect('bookmark:list')