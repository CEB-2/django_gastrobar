from django.shortcuts import render
from gastroblog.forms import CommentsForm
from gastroblog.models import Comments
from gastroblog.models import Article

def blog(request):
    form = CommentsForm()
    articles = Article.objects.all()
    comments = Comments.objects.all()

    context = {
       
        'form' : form,
        'articles' : articles,
        'comments' : comments
    }

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            new_comment = Comments(
                article_id = form.cleaned_data['article_id'],
                user = form.cleaned_data['user'],
                comment = form.cleaned_data['comment'],
            )

            new_comment.save()

    return render(request, 'blog.html', context)