from django.shortcuts import render
from gastroblog.forms import CommentsForm
from gastroblog.forms import ContactoForm
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

def contacto(request):
	form = ContactoForm()
	value = False
	if request.method == "POST":
		form = ContactoForm(request.POST)
		if form.is_valid():
			value = True
			new = Contacto()

			new.name = form.cleaned_data["name"]
			new.mail = form.cleaned_data["mail"]

	context = {
		'contacto' : contacto,
        'form' : form,
		'value' : value,
    }

	return render(request, 'contacto.html', context)