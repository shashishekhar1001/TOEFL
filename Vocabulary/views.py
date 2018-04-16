from django.shortcuts import render

# Create your views here.
def build_vocab(request):
    return render(request, "build_vocab.html", {})