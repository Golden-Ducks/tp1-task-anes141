import numpy as np
import spacy
import contractions
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score

nlp = spacy.load("en_core_web_sm")
print("######task1########")
# Class 1: Sports & Athletics (Context: Winning/Medals)
doc1 = "The gold medal price is high effort"
doc2 = "Winning a gold medal needs a high jump"
doc3 = "Market for a gold medal is a trade of sweat"
doc4 = "The athlete will trade all for a gold medal"

# Class 2: Finance & Economy (Context: Market/Investment)
doc5 = "The gold bars price is high today"
doc6 = "Investing in gold bars needs a high rate"
doc7 = "Market for gold bars is a trade of money"
doc8 = "The bank will trade all for gold bars"

def preprocess_text(text):
    """
    Make sure to lowercase and remove punctuation.
    """

    def to_contraction(text: str) -> str:
        text = text.lower()
        return contractions.fix(text)

    def drop_sw(doc: spacy.tokens.doc.Doc) -> list:
        return [t for t in doc if not t.is_stop]

    def drop_p(tokens: list) -> list:
        return [t for t in tokens if not t.is_punct]

    text = to_contraction(text)
    doc = nlp(text)
    tokens = drop_sw(doc)
    tokens = drop_p(tokens)
    return [t.lemma_ for t in tokens]

def vectorize(docs, n_gram_size=1):
    tokenized = [preprocess_text(doc) for doc in docs]

    all_ngrams = [
        " ".join(tokens[i:i+n_gram_size])
        for tokens in tokenized
        for i in range(len(tokens) - n_gram_size + 1)
    ]
    vocabs = sorted(set(all_ngrams))

    Vectors = list()
    for tokens in tokenized:
        doc_ngrams = [" ".join(tokens[i:i+n_gram_size]) for i in range(len(tokens) - n_gram_size + 1)]
        Vectors.append(
            [1 if v in doc_ngrams else 0 for v in vocabs]
        )
    return Vectors

# Training / Clustering
all_docs = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8]
y_true   = [0, 0, 0, 0, 1, 1, 1, 1]

# 1-gram Experiment
X1  = vectorize(all_docs, n_gram_size=1)
km1 = KMeans(n_clusters=2, random_state=42).fit(X1)

# 2-gram Experiment
X2  = vectorize(all_docs, n_gram_size=2)
km2 = KMeans(n_clusters=2, random_state=42).fit(X2)

print(f"1-gram clusters: {km1.labels_}")
print(f"2-gram clusters: {km2.labels_}")

# compare accuracy and precision
for name, km in [("1-gram", km1), ("2-gram", km2)]:
    labels = km.labels_
    print(f"\n{name}")
    print(f"  Accuracy : {accuracy_score(y_true, labels):.2f}")
    print(f"  Precision: {precision_score(y_true, labels, zero_division=0):.2f}")

#######################Task2####################################
print("#########task2#########")
# Documents
D1 = "I love cats"
D2 = "Cats are chill"
D3 = "I am late"

def add_padding(tokens):
    # wrap tokens with start and end flags
    return ["<s>"] + tokens + ["</s>"]

def extract_windows(tokens, window_size=1):
    # slide window and collect all (2*window_size+1)-token windows
    width = 2 * window_size + 1
    return [" ".join(tokens[i:i+width]) for i in range(len(tokens) - width + 1)]

def build_vocab(all_windows):
    # collect unique windows, sort alphabetically, assign index
    vocabs = sorted(set(w for windows in all_windows for w in windows))
    return {w: i for i, w in enumerate(vocabs)}

def vectorize_doc(doc_windows, vocab):
    # return a binary vector: 1 if window in doc, 0 otherwise
    return [1 if v in doc_windows else 0 for v in vocab]

# Run
all_docs = [D1, D2, D3]

all_windows = []
for doc in all_docs:
    tokens  = add_padding(preprocess_text(doc))
    windows = extract_windows(tokens, window_size=1)
    all_windows.append(windows)

vocab = build_vocab(all_windows)

print("\nSorted vocab:")
for w, i in vocab.items():
    print(f"  {i}: \"{w}\"")

print()
for doc, windows in zip(all_docs, all_windows):
    vec = vectorize_doc(windows, vocab)
    print(f"{doc!r:20s} → {vec}")