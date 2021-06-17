filename1 = open("D:/333.csv",'r',encoding='utf-8')

# 여기에 CSV파일을 불러와서 2번째 리뷰만 포함한 열을 INPUT으로 넣고 돌린다. 또한 코드를 작성할시에 3번째 열에
# 있는 평점을 추가로 작성해주고, 4번째 열의 결과에 따라서 UNL인지 L인지에 따라서 파일을 달리 저장한다.

# with codecs.open(filename1, 'r', 'utf-8') as f7:
lines1 = filename1.readlines()

# lines1 = lines1.split(",")[1]
# print(lines1)

for line in lines1:
    line2 = line.split(",")[1]
    # print(line2)
    print(line.split(",")[3].replace('\n',''))
    if line.split(",")[3].replace('\n','') == 'l':
        print('1111111111111111111111111111111')