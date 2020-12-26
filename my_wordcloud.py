#!/usr/bin/env python
# coding: utf-8

# In[5]:


from textblob import TextBlob
import nltk
import pandas as pd
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt


# In[4]:


#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('stopwords')


# In[44]:


def word_cloud_generate(column_of_df, get_adj = True): 
    
    
    string = column_of_df if isinstance(column_of_df, str) else str(column_of_df)
    
    def get_adjectives(text):
        blob = TextBlob(text)
        return [ word for (word,tag) in blob.tags if tag.startswith("JJ")] 
    
    string_to_cloud = string
    if get_adj:
        string_adj = get_adjectives(string)
        string_to_cloud = str(string_adj).replace("'","").replace(",", " ").replace("[", "").replace("]", "")

    stopwords=set(STOPWORDS)
    def Mywordcloud(data, title=None):
        wordcloud=WordCloud(
            background_color='white',
            stopwords=stopwords,
            max_words=60,
            max_font_size=50,
            scale=3,
            random_state=1
        ).generate(data)
        fig=plt.figure(1,figsize=(10,10))
        plt.axis('off')
        if title:
            fig.suptitle(title,fontsize=20)
            fig.subplots_adjust(top=2.3)
        plt.imshow(wordcloud)
        plt.show()
    Mywordcloud(string_to_cloud)


# In[46]:


#df=pd.read_csv('productdata.csv')
#word_cloud_generate(df.loc[df['brand'] == 'Microsoft', 'reviews_text'])

