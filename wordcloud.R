# Annie Sauer
# October 24, 2018

library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")

# Load text
text <- readLines("~/Stat Programming/STAT_5014_Homework/11_Python/constitution.txt")
text <- Corpus(VectorSource(text))
# Clean up text 
text <- tm_map(text, content_transformer(tolower))
text <- tm_map(text, removeNumbers)
text <- tm_map(text, removeWords, stopwords("english"))
text <- tm_map(text, removePunctuation)
text <- tm_map(text, stripWhitespace)

# Create matrix of word frequencies
t_matrix <- TermDocumentMatrix(text)
t_matrix <- as.matrix(dtm)
vec <- sort(rowSums(t_matrix),decreasing=TRUE)
df <- data.frame(word = names(vec),freq=vec)

wordcloud(words = df$word, freq = df$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(6, "Dark2"))
