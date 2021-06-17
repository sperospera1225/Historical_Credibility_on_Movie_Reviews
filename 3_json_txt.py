import json
from pprint import pprint

with open('D:/movie_review/new_data_review/Intimates strangers/review_data.json', "r", encoding='utf-8') as f12:
    review_data = json.load(f12)
pprint(review_data[0])
count = 1
overlap = 0
# f = open("D:/movie_review/new_data_review/Intimates strangers/baseline_old/labeled2.txt", "w", encoding='utf-8')
f1 = open("D:/movie_review/new_data_review/Intimates strangers/baseline_old/trusted_rating.txt", "w", encoding='utf-8')
f2 = open("D:/movie_review/new_data_review/Intimates strangers/baseline_old/untrusted_rating.txt", "w", encoding='utf-8')
reading_file = open("D:/movie_review/new_data_review/Intimates strangers/review_history.txt", "r", encoding='utf-8')
number1 = 0
number2 = 0
number3 = 0
number4 = 0
while (count <= 23310):  # review_data.json 갯수

    labeled1 = True
    labeled2 = True
    labeled3 = True
    line = reading_file.readline()
    asdf = line.split()

    # f.write(str(review_data[count-1]["no"]))
    # f.write("\t")
    # f.write(review_data[count-1]["id"])
    # f.write("\t")
    # f.write(review_data[count-1]["rating"])
    # f.write("\t")
    asdf = list(map(int, asdf))
    asdf = list(asdf)
    #print(asdf)
    if 0 in asdf:
        asdf.remove(0)
    if (review_data[count - 1]["rating"] == '1' or review_data[count - 1]["rating"] == '10'):
        #print(sum(asdf, 0.0)/len(asdf))
        #print(len(asdf)/1)
        if len(asdf) >= 2.0:
            #print(len(asdf))
            a = sum(asdf, 0.0) / len(asdf)
            #print(a)
            if  a == 10:
                labeled1 = False
                #print(asdf)
            elif a == 1:
                labeled1 = False
                #print(asdf)
            elif len(asdf) == 0:
                labeled1 = False
            else:
                labeled1 = True
        else:
            labeled1 = True
    else: labeled1 = True

    # if len(asdf) <= 2:
    #     if len(asdf) == 1 and 1 in asdf:
    #         labeled1 = False
    #     elif len(asdf) == 1 and 10 in asdf:
    #         labeled1 = False
    #     elif len(asdf) == 2 and 1 in asdf and 10 in asdf:
    #         labeled1 = False
    #     elif len(asdf) == 0:
    #         labeled1 = False

    # f.write("\t")
    a = review_data[count - 1]["rating"]
    c = a.strip()

    if labeled1 == False:
        print(asdf)
        # f.write("unlabeled")
        # f.write(c)
        f2.write(c)
        f2.write("\n")
        number1 = number1 + 1
    elif labeled1 == True:
        # f.write("labeled")
        # f.write(c)
        f1.writelines(c)
        f1.write("\n")
        number2 = number2 + 1
    #
    # f.write("\n")

    count = count + 1

print(number1)
print(number2)

# f.close()
f1.close()
f2.close()
