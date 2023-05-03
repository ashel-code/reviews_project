
# import numpy as np
# from keras.models import Sequential
# from keras.layers import Dense
# from sklearn.cluster import KMeans
# from sklearn.feature_extraction.text import TfidfVectorizer

# from structure.preclustering import Precluster

# def cluster():
#     pass

# def learn():
#     # TODO: data = database.get_all()
#     # 
#     data = [Precluster(1, 'some_vector_stuff'),
#             Precluster(4, 'some_vector_stuff2'),
#             Precluster(23, 'some_vector_stuff3'),]
#     learn(data)

# def learn(data):

#     vectors = [d.text for d in data]

#     # Load vectorized comments as an array
#     # comments = np.load('vectorized_comments.npy')

#     # Модель нейронной сети
#     model = Sequential()
#     model.add(Dense(64, input_dim=768, activation='relu'))
#     model.add(Dense(256, activation='relu'))
#     model.add(Dense(768, activation='relu'))
#     model.add(Dense(256, activation='relu'))
#     model.add(Dense(2, activation='softmax'))

#     # Compile the model
#     model.compile(loss='categorical_crossentropy', optimizer='adam')

#     # Train the model
#     model.fit(vectors, np.array([[1,0]]*len(vectors)), epochs=3, verbose=1)

#     # Get cluster labels
#     labels = KMeans(n_clusters=2).fit_predict(model.predict(vectors))


#     for com in genuine_comments:
#         print(texts.index(com))

#     return genuine_comments, fake_comments


