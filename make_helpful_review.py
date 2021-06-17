import json
from pprint import pprint

with open('D:/movie_review/new_data_review/A taxi driver/review_data.json', "r", encoding='utf-8') as f12:
    review_data = json.load(f12)
pprint(review_data[0])
count = 1
overlap = 0
f3 = open("D:/movie_review/new_data_review/A taxi driver/baseline_old/review_history_undecided.txt", "w", encoding='utf-8')
f4 = open("D:/movie_review/new_data_review/A taxi driver/baseline_old/review_history_helpful.txt", "w", encoding='utf-8')
f5 = open("D:/movie_review/new_data_review/A taxi driver/baseline_old/review_history_unhelpful.txt", "w", encoding='utf-8')
number1 = 0
number2 = 0
number3 = 0
number4 = 0
while (count <= 48915):  # review_data.json 갯수
    labeled1 = True
    labeled2 = True
    labeled3 = True

    # f3.write(str(review_data[count-1]["no"]))
    # f3.write("\t")
    # f3.write(review_data[count-1]["id"])
    # f3.write("\t")
    # f3.write(review_data[count-1]["rating"])
    # f3.write("\t")
    # f3.write(review_data[count-1]["sympathy"])
    # f3.write("\t")
    # f3.write(review_data[count-1]["unsympathy"])
    # f3.write("\t")
    sympathy=review_data[count-1]["sympathy"]
    unsympathy = review_data[count-1]["unsympathy"]
    sympathy_int = int(sympathy)
    unsympathy_int = int (unsympathy)

    if sympathy_int + unsympathy_int >= 5:
        if sympathy_int > unsympathy_int:
            labeled2 = False

    # if sympathy_int >= unsympathy_int:
    #     labeled2 = True
    elif sympathy_int == 0 and unsympathy_int == 1:
        labeled2 = False
        labeled3 = False
    elif sympathy_int == 1 and unsympathy_int == 2:
        labeled2 = False
        labeled3 = False
    else:
        labeled2 = True

    d=review_data[count-1]["review"]
    e=d.replace("\n관람객\n","")
    g=e.strip()

    if labeled2 == False:
        if labeled3 == True:
            # f3.write("unlabeled")
            # f3.write(g)
            f4.write(g)
            f4.write("\n")
            number3=number3+1
        elif labeled3 == False:
            f3.write(g)
            f3.write("\n")
            number1 = number1 + 1
    else:
        # f3.write("labeled")
        # f3.write(g)
        f5.writelines(g)
        f5.write("\n")
        number4=number4+1

    # f3.write("\n")

    if labeled1 == True and labeled2 == True:
        overlap = overlap + 1
    count = count + 1
print(overlap)
print(number1)
print(number2)
print(number3)
print(number4)
# f.close()
# f1.close()
# f2.close()
# f3.close()
f4.close()
f5.close()
