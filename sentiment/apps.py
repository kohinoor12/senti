from django.apps import AppConfig
import nltk


class SentimentConfig(AppConfig):
    name = 'sentiment'

    def ready(self):
        # Download WordNet resource
        nltk.download('wordnet')
