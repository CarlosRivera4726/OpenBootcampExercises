from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date
# Create your views here.


def index(request):
    return HttpResponse("Todo Ok!")


def create(request):
    reporter = Reporter(first_name="Carlos",
                        last_name="Rivera", email="carlos@mail.com")
    reporter.save()

    article1 = Article(headline="Primer Articulo",
                       pub_date=date(2022, 5, 5), reporter=reporter)
    article1.save()

    article2 = Article(headline="Segundp Articulo",
                       pub_date=date(2022, 5, 7), reporter=reporter)
    article2.save()

    article3 = Article(headline="Tercer Articulo",
                       pub_date=date(2022, 7, 9), reporter=reporter)
    article3.save()

    #result = article1.reporter.first_name
    result = reporter.article_set.all()

    return HttpResponse(result)
