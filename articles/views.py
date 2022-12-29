from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Article
from .forms import ArticleModelForm, ArticleFormOld

def article_search_view(request):
    query = request.GET.get('q')
    try:
        query = int(query)
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context  = {
       "object": article_obj 
    }
    return render(request, "articles/search.html", context=context)

def article_list_view(request):
    if request.method == 'GET':
        article_list = Article.objects.all()
        context = {
            "object_list": article_list
        }
    return render(request, "articles/list.html", context=context)

@login_required
def article_create_view(request):
    form = ArticleModelForm(request.POST or None)
    context = {
       "form": form
    }
    if form.is_valid():
        article_obj = form.save()
        context['form'] = ArticleModelForm() #without this, validation error not showing
    return render(request, "articles/create.html", context=context)

def article_detail_view(request, id=None):
    # article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
        context = {
            "object": article_obj,
        }
    return render(request, "articles/detail.html", context=context)




"""
@login_required
def article_create_view(request):
    form = ArticleForm()
    context = {
       "form": form
    }

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        context['form'] = form  #without this, validation error not showing
        if form.is_valid():
            title   = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article_obj = Article.objects.create(title=title, content=content)
            context = {
              "object": article_obj,
              "created": True
              # "form": form
            }

    #---or---
    form = ArticleModelForm()
    if form.is_valid():
        article_obj = form.save()
        context = {
          "object": article_obj,
          "created": True
        }
    return render(request, "articles/create.html", context=context)

"""
