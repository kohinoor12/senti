from django.apps import AppConfig
import nltk


class EmotionConfig(AppConfig):
    name = 'emotion'

    def ready(self):
        # Download WordNet resource
        nltk.download('wordnet')
        nltk.download('punkt')
