MODELS_INFO = {
    "Logistic Regression + TF-IDF": {
        "file": "logistic_regression_tfidf_model.pkl",
        "accuracy": 0.8615625,
        "type": "Logistic Regression",
        "vectorizer": "TF-IDF",
        "description": "Combines TF-IDF (Term Frequency-Inverse Document Frequency) for feature extraction with a Logistic Regression classifier. TF-IDF evaluates how relevant a word is to a document in a collection. Logistic regression is a statistical model that in its basic form uses a logistic function to model a binary dependent variable.",
        "pros": ["High accuracy", "Robust to noise", "Handles sparse data effectively", "Provides interpretable probabilities"],
        "cons": ["Assumes linear relationship between features", "Requires more computational power than Naive Bayes"],
        "best_for": "Complex text classification tasks where accuracy is paramount."
    },
    "Naive Bayes + Bag of Words (BoW)": {
        "file": "naive_bayes_bow_model.pkl",
        "accuracy": 0.7678125,
        "type": "Naive Bayes",
        "vectorizer": "Bag of Words (BoW)",
        "description": "Uses the Bag of Words (BoW) method to count the frequency of words in a document, ignoring order. It pairs this with a Naive Bayes classifier, a probabilistic machine learning model based on Bayes' Theorem, which assumes independence between predictors.",
        "pros": ["Simple and fast to train", "Works well for basic text classification tasks like spam filtering", "Highly scalable"],
        "cons": ["Ignores word order and context", "Assumes all words are independent (the 'naive' assumption)"],
        "best_for": "Quick baseline models and simple categorization."
    },
    "Naive Bayes + TF-IDF": {
        "file": "naive_bayes_tfidf_model.pkl",
        "accuracy": 0.6609375,
        "type": "Naive Bayes",
        "vectorizer": "TF-IDF",
        "description": "Uses Term Frequency-Inverse Document Frequency (TF-IDF) for feature extraction to penalize highly frequent, non-informative words. Combined with the Naive Bayes probabilistic classifier.",
        "pros": ["Better than BoW at highlighting rare but important words", "Fast to predict"],
        "cons": ["Still ignores word order", "Sometimes underperforms BoW if the task relies heavily on common word patterns"],
        "best_for": "Tasks where specific rare keywords are highly indicative of the class."
    }
}

def get_model_names():
    return list(MODELS_INFO.keys())

def get_model_details(model_name):
    return MODELS_INFO.get(model_name, None)
