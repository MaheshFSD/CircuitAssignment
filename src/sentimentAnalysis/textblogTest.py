from textblob import TextBlob

# this file will provide sentimental score based on realtime comments.
comment = input("Enter your comment")

senti = TextBlob(comment)

score= senti.sentiment.polarity

if score>0 and score <=1:
    print('positive')
elif score<0:
    print("negative")
else :
    print('neutral')