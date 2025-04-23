from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from data import documents
from ignord_words import mots_ignore

documents = [doc.lower() for doc in documents]


# Convertir les documents en une matrice TF-IDF
vectorizer = TfidfVectorizer(stop_words=mots_ignore)
X_fit = vectorizer.fit(documents)

X = vectorizer.transform(documents)
print ( "TF-IDF Matrix Shape:" , X)   # Afficher la forme de la matrice

vocabulaire = vectorizer.get_feature_names_out()
print("vocabulaire: ",vocabulaire)