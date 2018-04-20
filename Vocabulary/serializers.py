from .models import Word
from rest_framework import serializers

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('url', 'word_vocab', 'meaning', 'image_url', 'category', 'example', 'audio')