import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

def home_view(request, *args, **kwargs):
    rand_num = random.randint(1,3)
    article_obj = Article.objects.get(id=rand_num)
    article_list = Article.objects.all()
    context = {
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content,
        "object_list": article_list,
    }
    
    HTML_STRING = render_to_string("home-view.html",context=context)
    # HTML_STRING = """
    # <h1> {title}! - {content} - id: {id}</h1>
    # """.format(**context)
    return HttpResponse(HTML_STRING)



