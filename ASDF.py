import codecs

train = list()

filename1 = "D:/movie_review/new_data_review/amsal/baseline_new/review_history_trusted_comment_sympathy_noempty.txt"
filename2 = "D:/movie_review/new_data_review/amsal/baseline_new/review_history_untrusted_comment_sympathy_noempty.txt"
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
print(len(train))

# train = [('하정우진짜멋있다....ㅜㅜ', 'pos'),
# ('완전 잼있어요 이런 영화 강추 전지현 존예', 'pos'),
# ('내가 왜 자네 앞에서 눈을 감나', 'neg'),
# ('최고입니다 끝나고도 여운이 남는 영화', 'pos'),
# ('배우들의 연기 매우 굿 암울했던 시절의 이야기를 너무 우울하지 않게 밀도 있게 표현함 하정우짱', 'pos'),
# ('시사회로 봤는데 재미와 의미를 모두 잡은 영화입니다!! 한두번 더 봐도 좋겠단 생각이 들었습니다^^', 'pos'),
# ('시사회 보고 왔는데.. 진짜 꼭 봐야할 영화, 보고 나니 가슴이 찡한 영화', 'pos'),
# ('긴장감과 이야기의 흐름이 잘이어진거같고 여운이많이남네요', 'pos'),
# ('시간가는줄 모르고 봤어요  연기잘하는 배우들도 많이 나오고 영화자체가 볼거리가 많아요', 'pos'),
# ('긴시간 시간가는줄 모르고 집중해서 보게됨 올만에 완성도있는 영화봐서 매우만족합니다~~', 'pos'),
# ('별점9점만 남기고 갑니다.. 제가 평가할수 있는 영화가 아니네요..', 'pos'),
# ('긴시간이지만 지루하지 않게 재밌게 봤습니다. 전지현.하정우.이정재 연기 멋지게 잘 봤습니다. ~^^', 'pos'),
# ('최고!! 최고!!! 진짜 한국영화중에 제일 재밌었음', 'pos'),
# ('너무 잔인하지않아서 좋아요 잔잔함 감동도 있고 ~~', 'pos'),
# ('모든 배우가 연기를 다잘하는 영화... 두번연속으로 봤는데도 안질리네요 ㅎㅎㅎㅎ하와이피스톨 진짜 너뮤 매력적인캐릭터에요!!!!', 'pos'),
# ('배우는 연기력도 그렇고 기대 이하에요ㅜㅜㅜ', 'neg'),
# ('그저그럼 포인트준다고 해서 씀', 'neg'),
# ('흠 뭐라할까 약간 부족한느낌...', 'neg'),
# ('시간내서 꼭 보세요.  절대 돈아까운 영화 아닙니다.', 'pos')]