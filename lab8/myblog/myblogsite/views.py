from django.shortcuts import render
from django.forms.models import model_to_dict

from .forms import ContactForm
from .models import Article


def index(request):
    context = {"articles": Article.objects.all()}
    return render(request, "index.html", context=context)


def about(request):
    return render(request, "about.html")


def contacts(request):
    context = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            context = {"success": 1}
    else:
        form = ContactForm()
    context["form"] = form
    return render(request, "contacts.html", context=context)


def article_view(request, pk: int):
    article = Article.objects.get(pk=pk)
    return render(request, "article.html", model_to_dict(article))
