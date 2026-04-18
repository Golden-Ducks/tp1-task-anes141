import contractions  
import spacy
nlp = spacy.load("en_core_web_sm")


text1 = "Dates are hiding from you today :'))"
text2 = " I won't attend this Sunday evening."
text3 = " Cats are watching angels outside :)"

text1_n=contractions.fix( text1 )
text2_n=contractions.fix( text2 )
text3_n=contractions.fix( text3 )

text_sp1 = nlp(text1_n)
text_sp2 = nlp(text2_n)
text_sp3 = nlp(text3_n)

print(
    [  (t, t.is_stop) for t in text_sp1 ],"\n",
    [t for t in text_sp1 if not t.is_stop ]
)
print("\n")
print(
    [  (t, t.is_stop) for t in text_sp2 ],"\n",
    [t for t in text_sp2 if not t.is_stop ]
)
print("\n")
print(
    [  (t, t.is_stop) for t in text_sp3 ],"\n",
[   t for t in text_sp3 if not t.is_stop ]
)
print("\n")
p1= [t for t in text_sp1 if not t.is_punct ]
p2= [t for t in text_sp2 if not t.is_punct ]
p3= [t for t in text_sp3 if not t.is_punct ]

print(p1)
print(p2)
print(p3)
print("\n")
print([i for i in p1 if not i.is_stop])
print([i for i in p2 if not i.is_stop])
print([i for i in p3 if not i.is_stop])
print("\n")

print("========================================================")

from sklearn.cluster import KMeans
from num2words import num2words
import numpy as np
import string
punctuations = list(string.punctuation)
texts = [
    "Muslims are praying and giving charity today",
    "People are fasting and praying during Ramadan",
    "The community gathers to pray and help the needy",
    "Customers are buying and giving feedback today",
    "People are shopping and giving reviews online",
    "The community gathers to buy and help new clients",
]

def num2words(text: str):
    num = "".join(c for c in text if c.isdigit())
    if num:
        text = text.replace(num, num2words(int(num)))
    return text

def drop_sw(text: list):
    return [t for t in text if not t.is_stop]

def drop_p(text: list):
    return [t for t in text if t.text not in punctuations]

def Lemmatization(text: list):
    return [t.lemma_.lower() for t in text]

for i, text in enumerate(texts):
    texts[i] = contractions.fix(text)

texts = [nlp(text)       for text in texts]
texts = [drop_p(text)    for text in texts]
texts = [drop_sw(text)   for text in texts]
texts = [Lemmatization(text) for text in texts]


vocab = list(set([w for text in texts for w in text]))
Vectors = list()
for text in texts:
    Vectors.append(
        [1 if v in text else 0 for v in vocab]
    )
X_vectors = np.array(Vectors)



kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
kmeans.fit(X_vectors)

print("Clusters:", kmeans.labels_)

#the bow only check the presence of the word , without the meaning#