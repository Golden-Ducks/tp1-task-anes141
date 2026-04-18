#Djelili Anes Abdessamad
print("##################Task1###########################")
vocab = ['feel', 'good', 'better', 'thank', 'happened']

def vect(words, vocab):
    vec = []
    for v in vocab:
        if v in words:
            vec.append(1)
        else:
            vec.append(0)
    return vec

D2 = ['feel', 'better', 'thank']
D3 = ['good', 'happened']

print("Vector(D2):", vect(D2, vocab))
print("\n")
print("Vector(D3):", vect(D3, vocab))

print("\n")
######################################################
print("##################Task2###########################")
######################################################

def clean(text):

    text = text.lower()

    for p in ['.', ',', '!', '?']:
        text = text.replace(p, '')

    words = text.split()
    return words

D1 = "I feel good."
D2 = "I do feel even better now, thank you!"
D3 = "What's happened to you? you all good?"

D1_tokens = clean(D1)
D2_tokens = clean(D2)
D3_tokens = clean(D3)

print("D1 tokens:", D1_tokens)
print("\n")
print("D2 tokens:", D2_tokens)
print("\n")
print("D3 tokens:", D3_tokens)

print("\n")





##########################################
print("##################Task3(dataset)###########################")
#########################################

def load_dataset(path, label_value):
    docs = []
    labels = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            parts = line.strip().split(",")
            if len(parts) >= 2:
                text = parts[1]
                docs.append(text)
                labels.append(label_value)
    return docs, labels

fake_docs, fake_labels = load_dataset(
    r"TP2\archive (5)\News _dataset\Fake.csv", 0
)
true_docs, true_labels = load_dataset(
    r"TP2\archive (5)\News _dataset\True.csv", 1
)

docs_raw = fake_docs[:5] + true_docs[:5]
labels = fake_labels[:5] + true_labels[:5]

def clean(text):
    text = text.lower()
    for p in ['.', ',', '!', '?', ';', ':', '"', "'"]:
        text = text.replace(p, '')
    return text

num2word = {
    "0":"zero","1":"one","2":"two","3":"three","4":"four",
    "5":"five","6":"six","7":"seven","8":"eight","9":"nine","10":"ten"
}

def tokenize(text):
    return text.split()

def normalize(tokens):
    normalized = []
    for t in tokens:
        if t.isdigit() and t in num2word:
            normalized.append(num2word[t])
        else:
            normalized.append(t)
    return normalized

def build_vocab(docs):
    vocab = []
    for doc in docs:
        for word in doc:
            if word not in vocab:
                vocab.append(word)
    return vocab

def vectorize(doc, vocab):
    vec = []
    for v in vocab:
        if v in doc:
            vec.append(1)
        else:
            vec.append(0)
    return vec

docs_processed = []
for d in docs_raw:
    cleaned = clean(d)
    tokens = tokenize(cleaned)
    normalized = normalize(tokens)
    docs_processed.append(normalized)

vocab = build_vocab(docs_processed)

vectors = []
for doc in docs_processed:
    vectors.append(vectorize(doc, vocab))

print("Vocabulary size:", len(vocab))
print("\n")
print("First 20 vocab words:", vocab[:20])
print("\n")
print("Vectors sample:", vectors[:3])
print("\n")
print("Labels sample:", labels[:3])
