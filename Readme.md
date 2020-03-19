# 2020  
## 1. Twitter sentiment analysis using Doc2Vec  

[https://github.com/quanyu2015/mtech/blob/master/doc2vec.ipynb](https://github.com/quanyu2015/mtech/blob/master/doc2vec.ipynb)

---   
# 2019   

## 1. Text generation using LSTM   
I used Harry Potter as the corpus to train a language model. Then this model can be used to generate new sentences.  
[https://github.com/quanyu2015/mtech/blob/master/lstm_model_train.ipynb](https://github.com/quanyu2015/mtech/blob/master/lstm_model_train.ipynb)    
[https://github.com/quanyu2015/mtech/blob/master/lstm_text_generation.ipynb](https://github.com/quanyu2015/mtech/blob/master/lstm_text_generation.ipynb)

---    
# 2018
## 1. Final year project
Why E-commerce? A research by Temasek and Google in 2017 shows that the market size of E-commerce will rise to 88 billion by 2025.   
[E-conomy SEA Spotlight 2017](https://www.blog.google/documents/16/Google-Temasek_e-Conomy_SEA_Spotlight_2017.pdf)    
[E-Conomy SEA 2018: Southeast Asia's internet economy hits an inflection point](https://www.thinkwithgoogle.com/intl/en-apac/tools-research/research-studies/e-conomy-sea-2018-southeast-asias-internet-economy-hits-inflection-point/)
     
<img src="/docs/market.png" width = "650">    

### Sentiment analysis
[https://github.com/quanyu2015/mtech/blob/master/sentiment_2019.ipynb](https://github.com/quanyu2015/mtech/blob/master/sentiment_2019.ipynb)

### Market share of phone brands
[https://github.com/quanyu2015/mtech/blob/master/market_phone.ipynb](https://github.com/quanyu2015/mtech/blob/master/market_phone.ipynb)

## 2. Action classification using CNN 
UTD Multimodal Human Action Dataset ([UTD-MHAD](http://www.utdallas.edu/~cxc123730/UTD-MHAD.html)) was collected using a Microsoft Kinect and a wearable inertial sensor. Four types of sensor data were used in this study: RGB video, depth video, skeleton and inetial sensor data. A deep learning model was implemented to classify 27 different actions.     
[https://github.com/quanyu2015/mtech/blob/master/04_fusion.ipynb](https://github.com/quanyu2015/mtech/blob/master/04_fusion.ipynb)
    
References:   
[Skeleton based action recognition with convolutional neural network](https://ieeexplore.ieee.org/document/7486569)  
[Human Action Recognition based on 3D Convolution Neural Networks from RGBD Videos](http://wscg.zcu.cz/WSCG2018/Poster/P31-full.PDF)  
[Deep Convolutional and LSTM Recurrent Neural Networks for Multimodal Wearable Activity Recognition](https://www.mdpi.com/1424-8220/16/1/115/htm)    
[Predicting physical activity based on smartphone sensor data using CNN + LSTM](https://blog.goodaudience.com/predicting-physical-activity-based-on-smartphone-sensor-data-using-cnn-lstm-9182dd13b6bc)



## 3. Nuclei segmentation using U-Net
Multi-organ nuclei segmentation challenge: [MoNuSeg](https://monuseg.grand-challenge.org/).
### Image training data preprocssing
[https://github.com/quanyu2015/mtech/blob/master/mask_2class.ipynb](https://github.com/quanyu2015/mtech/blob/master/mask_2class.ipynb)

### Segmentation model   
[https://github.com/quanyu2015/mtech/blob/master/cnn_4.ipynb](https://github.com/quanyu2015/mtech/blob/master/cnn_4.ipynb)

---  
# 2017   
## 1. Boost hotel rating using web data mining  
**Skills highlighted:** python, web crawling, MongoDB
### Introduction  
Our business goal is to help identify customers that are willing to provide good ratings of our target hotel, so that we can train our front desk receptionist to boost hotel's ratings. To accomplish this, we scraped user and review data from TripAdvisor and build a random forest model for predicting user ratings. From this model, we found that the percentage of good ratings of a customer in his/her previous ratings, the number of cities visited, and the number of photos shared are the most important features.  
  
Our target hotel is the [Hard Rock Hotel](https://www.tripadvisor.com.sg/Hotel_Review-g294264-d1447339-Reviews-Hard_Rock_Hotel_Singapore-Sentosa_Island.html) located on Sentosa. And this analytics procedure can be easily adapted to any hotel.

### Web scraping
Architecture of scraping:  
<img src="/docs/trip.png" width = "300">  
  
Source code:  
[https://github.com/quanyu2015/mtech/blob/master/trip2.2.py](https://github.com/quanyu2015/mtech/blob/master/trip2.2.py)

### Data analysis and modeling
1. Load data from MongoDB to python
2. Exploratory data analysis
3. Predictive model     
[https://github.com/quanyu2015/mtech/blob/master/trip_analytics_2.1.ipynb](https://github.com/quanyu2015/mtech/blob/master/trip_analytics_2.1.ipynb)

## 2. Clinical image classification   
**Skills highlighted:** Python, OpenCV, image processing, deep learning   

Kaggle competition: [Intel & MobileODT Cervical Cancer Screening](https://www.kaggle.com/c/intel-mobileodt-cervical-cancer-screening)  
Research manuscript:     
[https://github.com/quanyu2015/mtech/blob/master/docs/segmentation.pdf](https://github.com/quanyu2015/mtech/blob/master/docs/segmentation.pdf)   

## 3. Web log analysis
**Skills highlighted:** R, R Markdown, data vasualization, association rules mining   

[https://github.com/quanyu2015/mtech/blob/master/web_log.html](https://rawgit.com/quanyu2015/mtech/master/web_log.html)


