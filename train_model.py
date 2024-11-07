import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load datasets
true_news = pd.read_csv('data/True.csv')
fake_news = pd.read_csv('data/Fake.csv')

# Add labels: 1 = Real, 0 = Fake
true_news['label'] = 1
fake_news['label'] = 0

# Combine datasets
data = pd.concat([true_news, fake_news], axis=0).reset_index(drop=True)
data = data[['text', 'label']]

# Split into training and testing sets
X = data['text']
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize text data
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train the model
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

# Save the model and vectorizer
with open('fake_news_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('vectorizer.pkl', 'wb') as vec_file:
    pickle.dump(vectorizer, vec_file)

print("Model and vectorizer saved successfully!")
