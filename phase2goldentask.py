import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

# Load the dataset
df = pd.read_csv("C:\\Users\\HP\\Downloads\\email spam\\emails.csv")

# Visualize spam distribution
plt.figure(figsize=(6, 4))
df['spam'].value_counts().plot(kind='bar', color=['blue', 'orange'])
plt.xlabel('Spam')
plt.ylabel('Count')
plt.title('Spam Distribution')
plt.xticks([0, 1], ['Not Spam', 'Spam'], rotation=0)
plt.show()

# Prepare data
X = df['text'].astype(str)
y = df['spam'].replace({0: "Not Spam", 1: "Spam"}).astype("object")


# Vectorize text data
def create_vocabulary(data):
    vocabulary = defaultdict(lambda: len(vocabulary))
    for text in data:
        for word in text.split():
            vocabulary[word]
    return vocabulary

def vectorize_text(data, vocabulary):
    X_vectorized = np.zeros((len(data), len(vocabulary)))
    for i, text in enumerate(data):
        for word in text.split():
            if word in vocabulary:
                X_vectorized[i, vocabulary[word]] += 1
    return X_vectorized

# Plot histogram of email lengths
plt.figure(figsize=(8, 6))
email_lengths = X.str.len()
plt.hist(email_lengths, bins=50, color='skyblue', edgecolor='black')
plt.xlabel('Email Length')
plt.ylabel('Frequency')
plt.title('Distribution of Email Lengths')
plt.grid(True)
plt.show()

# Plot scatter plot of email lengths vs. spam
plt.figure(figsize=(8, 6))
plt.scatter(email_lengths, y, color='orange', alpha=0.5)
plt.xlabel('Email Length')
plt.ylabel('Spam')
plt.title('Email Length vs. Spam')
plt.yticks([0, 1], ['Not Spam', 'Spam'])
plt.grid(True)
plt.show()




# Train and evaluate Naive Bayes classifier
class NaiveBayes:
    def __init__(self):
        self.log_prior = {}
        self.log_likelihood = {}
    
    def fit(self, X, y):
        classes, counts = np.unique(y, return_counts=True)
        total_docs = len(y)
        for cls, count in zip(classes, counts):
            self.log_prior[cls] = np.log(count / total_docs)
            class_indices = np.where(y == cls)
            word_counts = X[class_indices].sum(axis=0)
            total_words = word_counts.sum()
            
    
    def predict(self, X):
        predictions = []
        for doc in X:
            posterior = {}
            for cls in self.log_prior:
                posterior[cls] = self.log_prior[cls] + np.dot(doc, self.log_likelihood[cls])
            predictions.append(max(posterior, key=posterior.get))
        return predictions





# Plot confusion matrix

fig, ax = plt.subplots(figsize=(6, 4))
np.disp.plot(ax=ax, cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

# Test with custom messages
custom_messages = [
    'Hi, my name is Harsh Shah and I am sending this email to you.',
    'Hi, it is Elon Musk here and I am giving you a $10,000,000 for free.'
]

for msg in custom_messages:
    
    
    print("you're message will be disappeared")



