from django.db import models

from keras.models import load_model
# from gensim import models as lda
# from gensim.corpora.dictionary import Dictionary
# import spacy

import os
import numpy as np
import pickle

email_authors = pickle.load(open('ml/pickle/tc_'))

topics = (

)

explanation = ()

class EmailBody(models.Model):
    body_text = models.TextField()
    
    def __str__(self):
        return self.body_text[:10]


class PredictModel(models.Model):
    body_text = models.TextField(null=True, blank=True)
    who_wrote_it = models.CharField(max_length=250, choices=email_authors, null=True)
    relation = models.CharField(max_length=250, choices=topics, null=True)
    relation_elaboration = models.TextField(null=True)

    # def preprocess(text):
    #     return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

    def save(self, *args, **kwargs):
        current_path = os.path.dirname(__file__)
        model_folder = os.path.join(current_path, 'models')

        # text classification
        model_path = os.path.join(model_folder, 'tm_model.h5')
        model = load_model(model_path)
        predict = model.predict([self.body_text])
        self.who_wrote_it = email_authors[np.argmax(predict)]
        
    #     # topic modeling
    #     en_model = spacy.load('en_core_web_sm')
    #     tags_rm = ['ADV','PRON','CCONJ','PUNCT','PART','DET','ADP','SPACE','NUM','SYM']

    #     email_token = [token.lemma_.lower() for token in self.body_text if token.pos_ not in tags_rm and not token.is_stop and token.is_alpha]

    #     model_path = os.path.join(model_folder, 'tm_model')

    #     # load model
    #     model2 = lda.ldamodel.LdaModel.load(model_path)

    #     # load dictionary
    #     dictionary = pickle.load(open('pickle/tm_dictionary.pkl', 'wb'))
    #     bow_vector = dictionary.doc2bow()
        
    #     self.relation = np.argmax([for index, score in sorted(model2[bow_vector], key=lambda tup: -1*tup[1])])

    #     self.relation_elaboration = explanation[self.relation]
        return super(PredictModel, self).save(*args, **kwargs)
