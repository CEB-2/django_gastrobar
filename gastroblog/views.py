from django.shortcuts import render
from gastroblog.forms import CommentsForm
from gastroblog.models import Comments
from gastroblog.models import Article

def blog(request):
    form = CommentsForm()
    articles = Article.objects.all()
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            new_comment = Comments(
                id_article = form.cleaned_data['id_article'],
                user = form.cleaned_data['user'],
                comment = form.cleaned_data['comment'],
            )
            new_comment.save()
    context = {
       
        'form' : form,
        'articles' : articles
        
    }
    return render(request, 'blog.html', context)
# Create your views here.

