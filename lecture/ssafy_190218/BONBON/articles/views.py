from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# 1. /articles -> 모든 글을 보여주는 곳(제목)
def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})
    
# 2. /articles/1 -> 글 상세하게 보는 곳
def detail(request, article_id):
    article = Article.objects.filter(id=article_id).first()
    return render(request, 'articles/detail.html', {'article': article})
    
# 3. /articles/new -> 새 글을 작성
def new(request):
    return render(request, 'articles/new.html')
    
# 4. /articles/create -> 새 글을 저장
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    author = request.GET.get('author')
    
    Article.objects.create(title=title, content=content, author=author)
    return render(request, 'articles/success.html')
    
# 5. /articles/1/edit -> 글 편집
def edit(request, article_id):
    article = Article.objects.filter(id=article_id).first()
    return render(request, 'articles/edit.html', {'article': article})
    
# 6. /articles/1/update -> 글을 수정
def update(request, article_id):
    article = Article.objects.filter(id=article_id).first()
    title = request.GET.get('title')
    content = request.GET.get('content')
    author = request.GET.get('author')
    
    article.title = title
    article.content = content
    article.author = author
    article.save()
    return redirect('articles:detail', article_id=article_id)
    
# 7. /articles/1/delete -> 글을 삭제
def delete(request, article_id):
    article = Article.objects.filter(id=article_id).first()
    article.delete()
    
    # return redirect('/articles/')
    return redirect('articles:index')