from textblob import TextBlob
import textblob

review = TextBlob("I LOVE LISTENING TO MUSIC")

happiness_score = review.sentiment.polarity

print(f"the sentiment score is: {happiness_score}")