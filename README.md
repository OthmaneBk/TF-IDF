### TF-IDF
- TF-IDF (Term Frequency-Inverse Document Frequency) est une méthode statistique utilisée en traitement du langage naturel et en recherche d'information pour évaluer l'importance d'un mot dans un document par rapport à une collection de documents.

### wrokflow de TF-IDF
- Suppression des mots qui n'auront aucun impact sur l'analyse en traitement du langage naturel, tels que : {le, a, des,...}
- TF(Term Frequency): Mesure la fréquence d'apparition d'un terme dans un document. Elle reflète l'importance du terme dans ce document spécifique.
- IDF (Inverse Document Frequency): Mesure l'importance du terme dans l'ensemble de la collection.

### Exemple d'application de TF-IDF
1- "Le chat mange une souris"
2- "Le chien court après le chat"
3- "Une souris se cache du chat et du chien"

## Étape 1: Elimincation des mots_vides: {le, une, après, se, du, et}

## Étape 2: Calculer TF (Term Frequency) pour chaque mot dans la phrase 1

Total de mots dans la phrase 1: 3 (apres suppression des mots_vides)
"chat": 1/3 = 0.333
"mange": 1/3 = 0.333
"souris": 1/3 = 0.333

## Étape 3: Calculer IDF (Inverse Document Frequency) pour chaque mot

# Documents totaux: 3
"chat": apparaît dans 3 documents → IDF = log(3/3) = 0
"mange": apparaît dans 1 document → IDF = log(3/1) ≈ 1.099
"souris": apparaît dans 2 documents → IDF = log(3/2) ≈ 0.405

### Le résultat
Dans cet exemple, le mot "mange" a le score TF-IDF le plus élevé (0.366) car il n'apparaît que dans cette phrase, ce qui confirme qu'il est le terme le plus distinctif de cette phrase par rapport au corpus.
