from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
# from IPython import embed

# Create your views here.


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.all()
    return render(request, 'board/detail.html', {
        'article': article,
        'comments': comments,
    })


# def new_article(request):
#     return render(request, 'board/new.html')


def create_article(request):
    if request.method == 'GET':
        return render(request, 'board/new.html')
    else:  # request.method == 'POST'
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('board:article_detail', article.id)


# def edit_article(request, article_id):
#     pass


def update_article(request, article_id):
    if request.method == 'GET':
        article = get_object_or_404(Article, id=article_id)
        return render(request, 'board/edit.html', {
            'article': article,
        })

    else:  # request.method == 'POST'
        article = get_object_or_404(Article, id=article_id)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('board:article_detail', article.id)


def delete_article(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
    return redirect('board:article_list')


def create_comment(request, article_id):
    if request.method == 'POST':
        comment = Comment()
        comment.article = get_object_or_404(Article, id=article_id)
        comment.content = request.POST.get('comment')

        comment.save()
    return redirect('board:article_detail', article_id)


def delete_comment(request, article_id, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()

    return redirect('board:article_detail', article_id)
