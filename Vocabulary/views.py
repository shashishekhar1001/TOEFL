from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from Vocabulary.models import *

# Create your views here.
def build_vocab(request):
    query_set = Word.objects.get_queryset().order_by('id')
    paginator = Paginator(query_set, 1) # Show 3 words per page
    page = request.GET.get('page')
    words = paginator.get_page(page)
    return render(request, "build_vocab.html", {"query_set":query_set, "words": words})