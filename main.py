import PyPDF2
import nltk
from nltk.corpus import stopwords

nltk.download('punkt_tab')
nltk.download("stopwords")
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

pdf_caminho = r"#"
with open(pdf_caminho, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + " "

tokens = nltk.word_tokenize(text)
words = [word.lower() for word in tokens if word.isalpha()]

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(words))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

stop_words = set(stopwords.words("portuguese"))
words = [word for word in words if word not in stop_words]

word_counts = Counter(words)

most_common_word, most_common_count = word_counts.most_common(1)[0]

print(f"A palavra que mais aparece é '{most_common_word}', e ela aparece {most_common_count} vezes!")
