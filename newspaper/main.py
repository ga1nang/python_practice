from newspaper import Article
import sys
import io
import nltk
from nltk.tokenize import word_tokenize

# Set UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Download necessary NLTK resources
nltk.download('punkt')  
nltk.download('averaged_perceptron_tagger') 

article = Article("https://vnexpress.net/ky-su-phan-mem-ai-dau-tien-tren-the-gioi-4722040.html")

article.download()
article.parse()

print(article.text)

data = article.text

tokenization = word_tokenize(data)
res = nltk.pos_tag(tokenization)
print(res)
