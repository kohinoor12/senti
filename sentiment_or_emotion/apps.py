from django.apps import AppConfig
import nltk



class SentimentOrEmotionConfig(AppConfig):
    name = 'sentiment_or_emotion'

    def ready(self):
        # Download WordNet resource
        nltk.download('wordnet')
        nltk.download('punkt')
