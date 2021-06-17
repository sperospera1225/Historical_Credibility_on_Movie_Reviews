import nltk
from konlpy.tag import Twitter
import codecs
pos_tagger = Twitter()

train = list()
# positive 리뷰랑 negative 리뷰랑 나누어서 각기다른 파일에 저장
filename1 = "C:/Users/admin/PycharmProjects/pjt/movie_review/pos/pos.txt"
filename2 = "C:/Users/admin/PycharmProjects/pjt/movie_review/neg/neg.txt"
with codecs.open(filename1, 'r', 'utf-8') as f:
    lines1 = f.readlines()

with codecs.open(filename2, 'r', 'utf-8') as f2:
    lines2 = f2.readlines()

for line in lines1:
    sub_train = list()
    sub_train.append(line.strip())
    sub_train.append('pos')
    train.append(sub_train)
for line in lines2:
    sub_train = list()
    sub_train.append(line.strip())
    sub_train.append('neg')
    train.append(sub_train)

def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

def term_exists(doc):
    # return {'exists({})'.format(word): (word in set(doc)) for word in tokens}
    return {'{}'.format(word): (word in set(doc)) for word in tokens}




train_docs = [(tokenize(row[0]),row[1]) for row in train]
tokens = [t for d in train_docs for t in d[0]]
train_xy = [(term_exists(d), c) for d, c in train_docs]
classifier = nltk.NaiveBayesClassifier.train(train_xy)
print(classifier.show_most_informative_features())
filename1 = "D:/movie_review/new_data_review/the_outlaws/baseline_old/review_history_trusted_comment_noempty.txt"
filename2 = "D:/movie_review/new_data_review/the_outlaws/baseline_old/review_history_untrusted_comment_noempty.txt"

test_sentence = []

with codecs.open(filename1, 'r', 'utf-8') as f:
    lines1 = f.readlines()

with codecs.open(filename2, 'r', 'utf-8') as f:
    lines2 = f.readlines()

for line in lines1:
    test_sentence.append(line.strip())

for line in lines2:
    test_sentence.append(line.strip())
positive = 0
negative = 0

f1 = open("D:/movie_review/new_data_review/The Spy Gone North/baseline_old/trusted_positive_sympathy_2.txt",  "w",encoding='utf-8')
f2 = open("D:/movie_review/new_data_review/The Spy Gone North/baseline_old/trusted_negative_sympathy_2.txt",  "w",encoding='utf-8')

for i in range(len(test_sentence)):
    test_docs = tokenize(test_sentence[i])
    print(test_sentence[i])
    # print(classifier.show_most_informative_features())
    test_sent_features = {word: (word in tokens) for word in test_docs}
    print(classifier.classify(test_sent_features))

    if classifier.classify((test_sent_features)) == 'pos':
        positive += 1
        f1.write(test_sentence[i])
        f1.write("\t")
        f1.write('1')
        f1.write("\n")

    elif classifier.classify((test_sent_features)) == 'neg':
        negative += 1
        f2.write(test_sentence[i])
        f2.write("\t")
        f2.write('0')
        f2.write("\n")
print(positive, negative)