#!/usr/bin/python
#coding=utf-8
from konlpy.tag import Okt
import json
import codecs
import os
from pprint import pprint
import nltk
import numpy as np
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
# nsmc 데이터 불러오기

min1 = True
min3 = " "

def read_data(filename):
        with open(filename, 'r', encoding='utf8') as f:
                data = [line.split('\t') for line in f.read().splitlines()]
                # txt 파일의 헤더(id document label)는 제외하기
                data = data[1:]
        return data
train_data = read_data('ratings_train.txt')
test_data  = read_data('ratings_test.txt')
#print(len(train_data))
#print(len(train_data[0]))
#print(len(test_data))
#print(len(test_data[0]))
# 데이터 전처리
# KoNLPy 라이브러리를 이용해 형태소 분석 및 품사 태깅
# imdb 리뷰 분석 예제처럼 주어진 빈도만을 사용해서 처리해도 되지만 한국어는 영어와는 달리 띄어쓰기로 의미를 구분짓기에는 한계가 있고
# 네이버 영화 데이터에는 맞춤법이나 띄어쓰기가 제대로 되어있지 않은 경우가 있기 때문에 정확한 분류를 위해서 KoNLPy를 이용
# KoNLPy는 띄어쓰기 알고리즘과 정규화를 이용해서 맞춤법이 틀린 문장도 어느 정도 고쳐주면서 형태소 분석과 품사를 태깅해주는 여러 클래스를 제공
# 그 중에서 Okt(Open Korean Text) 클래스를 이용
# 먼저 Okt를 이용해서 간단한 문장을 분석
okt = Okt()
#print(okt.pos('이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요'))
# 이제 아까 불러온 데이터에 형태소 분석을 통해서 품사를 태깅해주는 작업
# 데이터의 양이 큰 만큼 시간이 오래 걸리기 때문에 이 작업을 반복하지 않도록 한 번 태깅을 마친 후에는 json 파일로 저장하는 것을 추천
# 여기에서는 이미 태깅이 완료된 train_docs.json 파일이 존재하면 반복하지 않도록 만듦
def tokenize(doc):
        # norm은 정규화, stem은 근어로 표시하기를 나타냄
        return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]
if os.path.isfile('train_docs.json'):
        with open('train_docs.json', 'r', encoding="utf-8") as f:
                train_docs = json.load(f)
        with open('test_docs.json', 'r', encoding="utf-8") as f:
                test_docs = json.load(f)
else:
        train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
        test_docs = [(tokenize(row[1]), row[2]) for row in test_data]
        # JSON 파일로 저장
        with open('train_docs.json', 'w', encoding="utf-8") as make_file:
                json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
        with open('test_docs.json', 'w', encoding="utf-8") as make_file:
                json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")
# 예쁘게(?) 출력하기 위해서 pprint 라이브러리 사용
#pprint(train_docs[0])
# 분석한 데이터의 토큰(문자열을 분석을 위한 작은 단위)의 갯수를 확인
tokens = [t for d in train_docs for t in d[0]]
#print(len(tokens))
# 이제 이 데이터를 nltk 라이브러리를 통해서 전처리
# Text 클래스는 문서를 편리하게 탐색할 수 있는 다양한 기능을 제공
# 여기에서는 vocab().most_common 메서드를 이용해서 데이터에서 가장 자주 사용되는 단어를 가져올 때 사용
text = nltk.Text(tokens, name='NMSC')
# 전체 토큰의 개수
#print('전체 토근 개수: {}'.format(len(text.tokens)))
# 중복을 제외한 토큰의 개수
#print('중복 제외 토근 수: {}'.format(len(set(text.tokens))))
# 출현 빈도가 높은 상위 토큰 10개
#pprint('출현 빈도가 높은 상위 10개 토큰: {}'.format(text.vocab().most_common(10)))
# 자주 사용되는 토큰 10000개를 사용해서 데이터를 벡터화
# 여기서는 원 핫 인코딩 대신에 CountVectorization을 사용
# 이는 문서 집합에서 단어 토큰을 생성하고 각 단어의 수를 세어 BOW(Bag of Words) 인코딩한 벡터를 만드는 역할을 함
# 시간이 꽤 걸립니다! 시간을 절약하고 싶으면 most_common의 매개변수를 줄여보세요.
selected_words = [f[0] for f in text.vocab().most_common(200)]
def term_frequency(doc):
        return [doc.count(word) for word in selected_words]
train_x = [term_frequency(d) for d, _ in train_docs]
test_x  = [term_frequency(d) for d, _ in test_docs]
train_y = [c for _, c in train_docs]
test_y  = [c for _, c in test_docs]
# 이제 데이터를 float로 형 변환 시켜주면 데이터 전처리 과정은 끝남
x_train = np.asarray(train_x).astype('float32')
x_test  = np.asarray(test_x).astype('float32')
y_train = np.asarray(train_y).astype('float32')
y_test  = np.asarray(test_y).astype('float32')
# 두 개의 Dense 층은 64개의 유닛을 가지고 활성화 함수로는 relu를 사용했으며, 마지막 층은 sigmoid 활성화 함수를 사용해서 긍정의 리뷰일 확률을 출력
# 손실 함수로는 binary_crossentropy를 사용했고 RMSProp 옵티마이저를 통해서 경사하강법을 진행
# 또한 배치 사이즈를 512로, 에포크를 10번으로 학습
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(200,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer=optimizers.RMSprop(lr=0.001),
        loss=losses.binary_crossentropy,
        metrics=[metrics.binary_accuracy])
model.fit(x_train, y_train, epochs=10, batch_size=512)
#results = model.evaluate(x_test, y_test)
# 테스트 데이터로 확인해본 결과를 출력해보면 80%의 성능을 보여주는 것을 알 수 있음
#print(results)

f1 = open("D:/movie_review/new_data_review/confidential assignment/baseline_old/t.txt",  "w", encoding='utf-8')
f2 = open("D:/movie_review/new_data_review/confidential assignment/baseline_old/ut.txt",  "w", encoding='utf-8')
# f3 = open("D:/movie_review/new_data_review/confidential assignment/baseline_old/.txt",  "w", encoding='utf-8')
# 이제 문자열 형태의 새로운 데이터를 받아와서 바로 결과를 예측하는 함수
# 데이터의 형태를 맞춰주기 위해서 np.expand_dims 메서드를 이용해 array의 축을 확장
# 최종 확률이 0.5 보다 크면 긍정이고, 그렇지 않으면 부정이라고 예측

a = 0
b = 0

def predict_pos_neg(review):
        token = tokenize(review)
        tf    = term_frequency(token)
        data  = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
        score = float(model.predict(data))
        # f3.writelines(str(score*100))
        # f3.write("\n")
        if min1 == False:
                f1.write(str(score * 100))
                f1.write(",")
                f1.write(min3)
                f1.write('\n')
        elif min1 == True:
                f2.write(str(score * 100))
                f2.write(",")
                f2.write(min3)
                f2.write('\n')

filename1 = open("D:/movie_review/new_data_review/confidential assignment/baseline_old/333.csv", 'r', encoding='utf-8')

# 여기에 CSV파일을 불러와서 2번째 리뷰만 포함한 열을 INPUT으로 넣고 돌린다. 또한 코드를 작성할시에 3번째 열에
# 있는 평점을 추가로 작성해주고, 4번째 열의 결과에 따라서 UNL인지 L인지에 따라서 파일을 달리 저장한다.

# with codecs.open(filename1, 'r', 'utf-8') as f7:
lines1 = filename1.readlines()

# lines1 = lines1.split(",")[1]
# print(lines1)

for line in lines1:
    line2 = line.split(",")[1]
    # print(line2)
    # print(line.split(",")[3])
    if line.split(",")[3].replace('\n','') == 'l':
        min1 = False
        print(min1)
        print("1")
        a = a + 1
        # print(line.split(",")[3].replace('\n',''))
    elif line.split(",")[3].replace('\n','') == "unl":
        min1 = True
        print(min1)
        print("2")
        b = b + 1
        # print(line.split(",")[3].replace('\n',''))
    min3 = line.split(",")[2]
    predict_pos_neg(line2)
    #print(line.strip())

print(str(a))
print(str(b))
f1.close()
f2.close()