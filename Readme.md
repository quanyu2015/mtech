## Introduction  
Our business goal is to identify potential customers that are willing to provide good ratings of our target hotel. To accomplish this, we scraped user and review data from TripAdvisor and build a random forest model for predicting user ratings. From this model, we found that the percentage of good ratings of a customer in his/her previous ratings, the number of cities visited, and the number of photos shared are the most important features.  
  
Our target hotel is the [Hard Rock Hotel](https://www.tripadvisor.com.sg/Hotel_Review-g294264-d1447339-Reviews-Hard_Rock_Hotel_Singapore-Sentosa_Island.html) located on Sentosa. And this analytics procedure can be easily adapted to any hotel.

## Web scraping
Architecture of scraping:  
<img src="/docs/trip.png" width = "300">  
  
Source code:  
[https://github.com/quanyu2015/mtech/blob/master/trip2.2.py](https://github.com/quanyu2015/mtech/blob/master/trip2.2.py)

## Data analysis and modeling
1. Load data from MongoDB to python
2. Exploratory data analysis
3. Predictive model  
[https://github.com/quanyu2015/mtech/blob/master/trip_analytics_2.1.ipynb](https://github.com/quanyu2015/mtech/blob/master/trip_analytics_2.1.ipynb)

