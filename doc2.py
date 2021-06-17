# 패키지 로딩하기
import modin.pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
from afinn import Afinn
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import codecs
# 데이터 읽어오기
pos_review = "D:/movie_review/new_data_review/amsal/baseline_new/review_history_trusted_comment_sympathy_noempty.txt"
# pos_file = open(pos_review, "r")
with codecs.open(pos_review, 'r', 'utf-8') as pos_file:
    pos_lines1 = pos_file.readlines()
# pos_file.close()

neg_review = "D:/movie_review/new_data_review/amsal/baseline_new/review_history_untrusted_comment_sympathy_noempty.txt"
# pos_file = open(pos_review, "r")
with codecs.open(neg_review, 'r', 'utf-8') as neg_file:
    neg_lines1 = neg_file.readlines()
# neg_file.close()

# Afinn 감성사전 생성하기
afinn = Afinn()

# Afinn 감성사전으로 긍정 평가
afinn.score(pos_lines1)

# Afinn 감성사전으로 부정 평가
afinn.score(neg_lines1)

# EmoLex 감성사전 생성하기
ncr = pd.read_table("D:/deeplearning/textmining/NRC.txt", engine="python", header=None, sep="\t")
ncr = ncr[(ncr != 0).all(1)]
ncr = ncr.reset_index(drop=True)

# 형태소 분석기
tokenizer = RegexpTokenizer("[\w]+")
stop_words = stopwords.words("english")
p_stemmer = PorterStemmer()

# 긍정 평가
pos_raw = pos_lines1.lower()
pos_tokens = tokenizer.tokenize(pos_raw)
stopped_pos_tokens = [i for i in pos_tokens if not i in stop_words]
match_pos_words = [x for x in stopped_pos_tokens if x in list(ncr[0])]

pos_emotions = []
for i in match_pos_words:
    temp = list(ncr.iloc[np.where(ncr[0] == i)[0], 1])
    for j in temp:
        pos_emotions.append(j)

pos_sentiment_result1 = pd.Series(pos_emotions).value_counts()
pos_sentiment_result1.plot.bar()
plt.show()