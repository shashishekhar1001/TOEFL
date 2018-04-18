from .models import Word
from .serializers import WordSerializer
from rest_framework import viewsets

class Word_ViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer