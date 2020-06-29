#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
stopwords = set(STOPWORDS)


# In[2]:


df = pd.read_csv(r"C:\Users\pxj190011\Desktop\Projects\Coursera dataset\reviews_by_course.csv")


# In[3]:


df.head()


# In[4]:


def plot_wordcloud(text, mask=None, max_words=400, max_font_size=120, figure_size=(24.0,16.0), 
                   title = None, title_size=40, image_color=False):
    stopwords = set(STOPWORDS)
    more_stopwords = {'one', 'br', 'Po', 'th', 'sayi', 'fo', 'Unknown'}
    stopwords = stopwords.union(more_stopwords)

    wordcloud = WordCloud(background_color='white',
                    stopwords = stopwords,
                    max_words = max_words,
                    max_font_size = max_font_size, 
                    random_state = 42,
                    mask = mask)
    wordcloud.generate(text)
    
    plt.figure(figsize=figure_size)
    if image_color:
        image_colors = ImageColorGenerator(mask);
        plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear");
        plt.title(title, fontdict={'size': title_size,  
                                  'verticalalignment': 'bottom'})
    else:
        plt.imshow(wordcloud);
        plt.title(title, fontdict={'size': title_size, 'color': 'green', 
                                  'verticalalignment': 'bottom'})
    plt.axis('off');
    plt.tight_layout()  
    
    C= '../Projects/Coursera dataset/'
    
  


# In[5]:


data =df[df['CourseId'] == 'data-management']
wordcloud = WordCloud(
                          background_color='black',
                          stopwords=stopwords,
                          max_words=100,
                          max_font_size=50, 
                          random_state=42
                         ).generate(str(data['Review']))

print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("word1.png", dpi=500)


# In[6]:


data1 =df[df['CourseId'] == 'analytics-tableau']
wordcloud = WordCloud(
                          background_color='black',
                          stopwords=stopwords,
                          max_words=100,
                          max_font_size=50, 
                          random_state=42
                         ).generate(str(data1['Review']))

print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("word1.png", dpi=500)


# In[7]:


data2 =df[df['CourseId'] == 'data-science-course']
wordcloud = WordCloud(
                          background_color='black',
                          stopwords=stopwords,
                          max_words=100,
                          max_font_size=50, 
                          random_state=42
                         ).generate(str(data2['Review']))

print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("word1.png", dpi=500)


# In[8]:


data2 =df[df['CourseId'] == 'data-science-course']
plt.rcParams['figure.figsize'] = (18, 10)

plt.subplot(1, 2, 1)
label1 = ' '.join([text for text in data['Review'][data['Label'] == 5]])

wordcloud = WordCloud(background_color = 'yellow', width = 2000, height = 2000, max_words = 70).generate(label1)
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Good reviews for data management course', fontsize = 20, fontweight = 30)

plt.subplot(1, 2, 2)

label1 = ' '.join([text for text in data2['Review'][data2['Label'] == 5]])
wordcloud = WordCloud(background_color = 'yellow', width = 2000, height = 2000, max_words = 70).generate(label1)
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Good reviews for data science course', fontsize = 20, fontweight = 30)
plt.show()

