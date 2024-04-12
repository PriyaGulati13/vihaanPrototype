# -*- coding: utf-8 -*-
"""textSimilarity.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15Pw2ztF3QatZ0PcfbBD9Bc0ZAwyN7G3D
"""

!pip install -q sentence_transformers

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from pprint import pprint

# paraphrase: This indicates that the model is trained to understand paraphrases, which are sentences or phrases that convey the same meaning but may be expressed differently. The model is trained to capture the semantic similarity between sentences and identify if they are paraphrases of each other.
# MiniLM: This refers to the architecture used for the model. In this case, it's a smaller version of the popular transformer architecture called "MiniLM." MiniLM is designed to be computationally efficient while still maintaining strong performance on various NLP tasks.
# L6: This indicates the number of transformer layers in the model. In this case, it has 6 transformer layers.

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

Sentences=\
  ['I love cats', 'I love dogs',
   'Cats are amazing pets', 'my name is Kavisha']

sentence_embeddings = model.encode(Sentences)

for sentence, embedding in zip(Sentences, sentence_embeddings):
  print("sentence:", sentence)
  print("embedding:", embedding)

len(sentence_embeddings)

len(sentence_embeddings[0])

pprint('Similarity between {} and {} is {}'.format(Sentences[0], Sentences[2], cosine_similarity(sentence_embeddings[0].reshape(1, -1), sentence_embeddings[2].reshape(1,-1))[0][0]))

similarities = []
for i in range(len(Sentences)):
    for j in range(i + 1, len(Sentences)):
        similarity_score = cosine_similarity(sentence_embeddings[i].reshape(1, -1), sentence_embeddings[j].reshape(1, -1))[0][0]
        similarities.append((Sentences[i], Sentences[j], similarity_score))

# ALGORITHM FOR TEXT SIMILARITY

# Assuming you have a function 'classify_genre' that takes an input string and returns its genre label
# And a function 'get_complaints_by_genre' that takes a genre label and returns all complaints belonging to that genre from your dataset


# input_string = "Your input string here"
# input_genre = classify_genre(input_string)

# similar_complaints = get_complaints_by_genre(input_genre)

# similarities = []
# input_embedding = embed(input_string)

# for complaint in similar_complaints:
#     complaint_embedding = embed(complaint)
#     similarity_score = cosine_similarity(input_embedding.reshape(1, -1), complaint_embedding.reshape(1, -1))[0][0]
#     similarities.append((input_string, complaint, similarity_score))

pprint(similarities)

