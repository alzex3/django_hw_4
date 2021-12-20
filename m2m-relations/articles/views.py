from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'

    result = Article.objects.all().prefetch_related('scopes')

    context = {
        'object_list': result
    }

    return render(request, template, context)
