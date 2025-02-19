import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load the dataset
sports_df = pd.read_excel('queries_dataset.xlsx')

# Load the saved model
with open('field_of_interest.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the vectorizer used for training the model
vectorizer = TfidfVectorizer()
vectorizer.fit_transform(sports_df['Query'])  # Fit the vectorizer to the queries

# Read user queries from the file
def read_user_queries(filename):
    with open(filename, 'r') as file:
        user_queries = file.readlines()
    return [query.strip() for query in user_queries]

# Predict the fields of interest
def predict_fields(user_queries, model, vectorizer):
    query_vectorized = vectorizer.transform(user_queries)
    return model.predict(query_vectorized)

# Get top fields of interest based on occurrence count
def get_top_fields(fields, top_n=4, min_occurrences=4):
    field_counts = pd.Series(fields).value_counts()
    top_fields = field_counts[field_counts >= min_occurrences][:top_n].index.tolist()
    return top_fields

# Read user queries
user_queries = read_user_queries('user_queries.txt')

# Predict fields of interest
predicted_fields = predict_fields(user_queries, model, vectorizer)

# Get top fields of interest
top_fields = get_top_fields(predicted_fields)

print("Top Fields of Interest:")
for i, field in enumerate(top_fields, 1):
    print(f"{i}. {field}")
