### Amazon Review Sentiment Analysis

## Description
This is the customer reviews of Amazon products data set. This dataset is a list of over 34,000 consumer reviews for Amazon products like the Kindle, 
Fire TV Stick, and more provided by Datafiniti's Product Database. The dataset includes basic product information, rating, review text, and more for each product.

## Processing steps
Before I was able to use sentiment analysis on this data, the data must be cleaned. The steps I took to clean this data were removing all missing values with .dropna, I made all words lower case with .lower(), I used .lemma_ to change words to base form and I removed all the stop words with .is_stop.

## Evaluation results
I set the function so a polarity review of < -0.15 would mean the sentiment of the review is negative, a polarity review of 0.15 > would mean the sentiment of the review is positive. In- between -0.15 – 0.15 would be classed as a neutral review. Most of the reviews in the sample is classed as positive.

<img width="640" alt="Screenshot 2024-03-12 at 11 29 33" src="https://github.com/Aolabode321/finalCapstone1/assets/156569217/ff0b8ee5-da0d-4325-be67-9c66b35c2f49">


## Insights
The model does what it is supposed to do which is good however a limitation is that it is only getting fed a sample which would decrease the accuracy. For a more accurate prediction from the model I would need to feed it allot more information. Another way to improve accuracy would be to split the reviews into different groups depending on the type of amazon product, right now I am preforming the sentiment analysis I the reviews.text column as a whole
