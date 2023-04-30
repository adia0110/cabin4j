import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def identify_intent(sentence):
    sentiment_scores = analyzer.polarity_scores(sentence)
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

sentence = input('Enter a sentence: ')

intent = identify_intent(sentence)

print('The intent of the sentence is:', intent)
