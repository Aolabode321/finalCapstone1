#imports
import spacy
import pandas as pd
from textblob import TextBlob

#load dataset
df = pd.read_csv('amazon_product_reviews.csv')

#load spacy model
nlp = spacy.load('en_core_web_lg')

#select reviews.text collumn from data set and drop missing values
reviews_data = df.dropna(subset=['reviews.text'])

#function to change to root word remove stop words and punctuation
def preprocess(reviews_data):
    reviews = nlp(reviews_data)
    return ' '.join([token.lemma_.lower() for token in reviews if not token.is_stop and not token.is_punct])


#sample of reviews
sample_rev = reviews_data.sample(20, random_state=42)

#apply the preprocess function to the reviews column and put the output in new column called 'processed review
sample_rev['processed review'] = sample_rev['reviews.text'].apply(preprocess)


#function to get polarity
def getPolarity(sample_rev):
    return TextBlob(sample_rev).sentiment.polarity
    

#apply get polarity function to 'processed review and put output in a new collumn called 'review polarity'
sample_rev['review_polarity'] = sample_rev['processed review'].apply(getPolarity)


#new collumn called 'sentiment all values in sentiment collumn is neutral
sample_rev['sentiment'] = 'neutral' #-0.15 - 0.15 is neutral 
sample_rev.loc[sample_rev['review_polarity']< -0.015, 'sentiment']= 'negitive' # below -0.15 is a negitive review
sample_rev.loc[sample_rev['review_polarity']> 0.015, 'sentiment']= 'positive' # above -0.15 is a positive review


# to view new collumns 
print(sample_rev[['processed review','review_polarity','sentiment']])


# my selected reviews for similarity check
review_of_choice = nlp(reviews_data['reviews.text'][9])
review_of_choice2 = nlp(reviews_data['reviews.text'][10])

#check similarity
sim = review_of_choice.similarity(review_of_choice2)

#print similarity
print(sim)