from flair.models import TextClassifier
from flair.data import Sentence
import pandas as pd
classifier = TextClassifier.load('en-sentiment')
file = open('./Social_res.txt', encoding='utf-8')
lines = file.readlines()
res = []
for line in lines:
    sentence = Sentence(line)
    classifier.predict(sentence)
    tmp = {'text': sentence.labels[0].data_point.text, 'tag': sentence.labels[0].data_point.tag,
           'score': sentence.labels[0].score}
    print("running")
    res.append(tmp)

data = pd.DataFrame(res)
data.to_csv('data1.csv', header=True, index=True)
