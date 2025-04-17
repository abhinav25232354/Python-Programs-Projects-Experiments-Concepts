# Suggestion Bot tells answer in yes or no

# from transformers import pipeline

# classifier = pipeline("zero-shot-classification",
#                       model="facebook/bart-large-mnli")

# sentence = "I don't think this will work"
# labels = ["positive", "negative", "neutral", "doubt", "question", "behavior"]

# result = classifier(sentence, labels)
# print(result)
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")
# print(sentiment_pipeline("I don't think this is going to work."))
report = sentiment_pipeline("I don't think it will work")
print(report)
print(report[0]['label'])
print(report[0]['score'])
