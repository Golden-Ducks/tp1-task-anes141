vocab = ["feel", "good", "better", "thank", "happened"]

docs = {
    "D1": (["feel", "good"], "Positive"),
    "D2": (["feel", "better", "thank"], "Positive"),
    "D3": (["happened", "good"], "Negative")
}


def words(docs, vocab):
    counts = {"Positive": {w:0 for w in vocab}, "Negative": {w:0 for w in vocab}}
    totals = {"Positive":0, "Negative":0}
    for words, label in docs.values():
        for w in words:
            counts[label][w] += 1
            totals[label] += 1
    return counts, totals

counts, totals = words(docs, vocab)


def Posterior_prob(word, label, counts, totals, vocab_size):
    return (counts[label][word] + 1) / (totals[label] + vocab_size)


priors = {"Positive": 2/3, "Negative": 1/3}

def naive_bayes(doc_words):
    scores = {}
    for label in ["Positive", "Negative"]:
        prob = priors[label]
        for w in doc_words:
            prob *= Posterior_prob(w, label, counts, totals, len(vocab))
        scores[label] = prob
    return max(scores, key=scores.get), scores

label, scores = naive_bayes(["feel", "good"])
print("Predicted:", label)
print("Scores:", scores)


label, scores = naive_bayes(["feel", "better", "thank"])
print("Predicted:", label)
print("Scores:", scores)


label, scores = naive_bayes(["happened", "good"])
print("Predicted:", label)
print("Scores:", scores)

