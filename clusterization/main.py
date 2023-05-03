
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


def cluster(texts):
    # Load vectorized comments as an array
    # comments = np.load('vectorized_comments.npy')


    # Convert comments to a numerical representation using TF-IDF

    # Модель нейронной сети
    model = Sequential()
    model.add(Dense(64, input_dim=768, activation='relu'))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(768, activation='relu'))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(2, activation='softmax'))

    # Compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    # Train the model
    model.fit(texts, np.array([[1,0]]*len(texts)), epochs=100, verbose=1)

    # Get cluster labels
    labels = KMeans(n_clusters=2).fit_predict(model.predict(texts))

    # Separate comments into fake and genuine
    fake_comments = texts[labels == 0]
    genuine_comments = texts[labels == 1]

    for com in genuine_comments:
        print(texts.index(com))

    return genuine_comments, fake_comments
