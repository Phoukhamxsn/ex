import matplotlib.pyplot as plt
from wordcloud import wordcloud

script = open('/downloads/gender.txt','r').read()

wordcloud = wordcloud().genderate(script)
wordcloud.words_
{'women':1.0,
 }