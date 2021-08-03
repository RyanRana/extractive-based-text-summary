
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
x = input("Enter Text: ")
stop_words = stopwords.words('english')
summarize_text = []
file = open(file_name, "r")
filedata = file.readlines()
article = filedata[0].split(". ")
sentences = []
for sentence in article:
    print(sentence)
    sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
sentences.pop() 
similarity_matrix = np.zeros((len(sentences), len(sentences)))
for idx1 in range(len(sentences)):
    for idx2 in range(len(sentences)):
        if idx1 == idx2: #ignore if both are same sentences
            continue 
        sent1 = sentences[idx1]
        sent2 = sentences[idx2]
        if stopwords is None:
            stopwords = []
        sent1 = [w.lower() for w in sent1]
        sent2 = [w.lower() for w in sent2]
        all_words = list(set(sent1 + sent2))
        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)
        for w in sent1:
            if w in stopwords:
                continue
            vector1[all_words.index(w)] += 1
        for w in sent2:
            if w in stopwords:
                continue
            vector2[all_words.index(w)] += 1
    similarity_matrix[idx1][idx2] = 1 - cosine_distance(vector1, vector2)
sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
scores = nx.pagerank(sentence_similarity_graph)
ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
print("Indexes of top ranked_sentence order are ", ranked_sentence)    
for i in range(5):
    summarize_text.append(" ".join(ranked_sentence[i][1]))
print("Summarize Text: \n", ". ".join(summarize_text))
