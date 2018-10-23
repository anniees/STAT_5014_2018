# Annie Sauer
# October 24, 2018

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load text 
file = open("11_Python/constitution.txt", 'r')
text = file.read()
wordcloud = WordCloud(background_color="white").generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()