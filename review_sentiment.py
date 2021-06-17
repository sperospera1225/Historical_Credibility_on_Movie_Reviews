import nltk
from konlpy.tag import Twitter
import codecs

# filename1 = "C:/Users/admin/PycharmProjects/pjt/movie_review/pos/pos.txt"
filename2 = "C:/Users/admin/PycharmProjects/pjt/movie_review/neg/neg.txt"

test_sentence = []

# with codecs.open(filename1, 'r', 'utf-8') as f:
#     lines1 = f.readlines()

with codecs.open(filename2, 'r', 'utf-8') as f:
    lines2 = f.readlines()

# for line in lines1:
#     test_sentence.append(line.strip())

for line in lines2:
    test_sentence.append(line.strip())


f1 = open("C:/Users/admin/PycharmProjects/pjt/movie_review/test_data.txt",  "w", encoding='utf-8')

for i in range(len(test_sentence)):
    f1.write(test_sentence[i])
    f1.write('\t')
    f1.write('0')
    f1.write('\n')
    print(test_sentence[i])