from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment

# Create your views here.


def posting_list(request):
    postings = Posting.objects.all().order_by('updated_at')

    return render(request, 'sns/list.html', {
        'postings': postings,
    })


def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.all().order_by('-created_at')

    return render(request, 'sns/detail.html', {
        'posting': posting,
        'comments': comments,
    })


def create_posting(request):
    if request.method == "POST":
        posting = Posting.objects.create(
            content=request.POST.get('content'),
            icon=request.POST.get('icon'),
            image=request.FILES.get('image')
        )

        return redirect('sns:posting_detail', posting.id)
    else:
        return redirect('sns:posting_list')


def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)

    if request.method == "POST":
        comment = Comment()
        comment.content = request.POST.get('comment')
        comment.posting = posting
        comment.save()

    return redirect('sns:posting_detail', posting_id)
