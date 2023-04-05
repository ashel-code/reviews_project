
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


def cluster(texts):
    print("----------------------")
    # Load vectorized comments as an array
    # comments = np.load('vectorized_comments.npy')
    comments = np.array(texts)

    # Convert comments to a numerical representation using TF-IDF
    vectorizer = TfidfVectorizer(max_features=768)
    comment_vectors = vectorizer.fit_transform(comments).toarray()

    # Create a neural network model
    model = Sequential()
    model.add(Dense(256, input_dim=768, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(2, activation='softmax'))

    # Compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    # Train the model
    model.fit(comment_vectors, np.array([[1,0]]*len(comment_vectors)), epochs=500, verbose=1)

    # Get cluster labels
    labels = KMeans(n_clusters=2).fit_predict(model.predict(comment_vectors))

    # Separate comments into fake and genuine
    fake_comments = comments[labels == 0]
    genuine_comments = comments[labels == 1]
    print(">----------------------<\nRESULTS")
    print(fake_comments)
    print("----------------")
    print(genuine_comments)
    for com in genuine_comments:
        print(texts.index(com))

    return genuine_comments, fake_comments
