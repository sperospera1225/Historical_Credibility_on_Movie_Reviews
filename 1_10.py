# import json
# from pprint import pprint
#
# with open('/new_data_review/the_outlaws/review_data.json', "r", encoding='utf-8') as f12:
#     review_data = json.load(f12)
# pprint(review_data[0])
# count = 1
# overlap = 0
# f1 = open("/new_data_review/the_outlaws/baseline_old/review_0_10_trusted_comment.txt", "w", encoding='utf-8')
# f2 = open("/new_data_review/the_outlaws/baseline_old/review_0_10_untrusted_comment.txt", "w", encoding='utf-8')
# reading_file = open("/new_data_review/the_outlaws/review_history.txt", "r", encoding='utf-8')
# number1 = 0
# number2 = 0
# number3 = 0
# number4 = 0
# while (count <= 21267):  # review_data.json 갯수
#
#     labeled1 = True
#     labeled2 = True
#     labeled3 = True
#     line = reading_file.readline()
#     asdf = line.split()
#     # f.write(str(review_data[count-1]["no"]))
#     # f.write("\t")
#     # f.write(review_data[count-1]["id"])
#     # f.write("\t")
#     # f.write(review_data[count-1]["rating"])
#     # f.write("\t")
#     asdf = list(map(int, asdf))
#     asdf = list(asdf)
#     #print(asdf)
#     if 0 in asdf:
#         asdf.remove(0)
#     if (review_data[count - 1]["rating"] == '1' or review_data[count - 1]["rating"] == '10'):
#         labeled2 = False
#         #print(sum(asdf, 0.0)/len(asdf))
#         #print(len(asdf)/1)
#         if len(asdf) >= 2.0:
#             #print(len(asdf))
#             a = sum(asdf, 0.0) / len(asdf)
#             #print(a)
#             if  a == 10:
#                 labeled1 = False
#                 #print(asdf)
#             elif a == 1:
#                 labeled1 = False
#                 #print(asdf)
#             elif len(asdf) == 0:
#                 labeled1 = False
#             #print(asdf)
#     # if len(asdf) <= 2:
#     #     if len(asdf) == 1 and 1 in asdf:
#     #         labeled1 = False
#     #     elif len(asdf) == 1 and 10 in asdf:
#     #         labeled1 = False
#     #     elif len(asdf) == 2 and 1 in asdf and 10 in asdf:
#     #         labeled1 = False
#     #     elif len(asdf) == 0:
#     #         labeled1 = False
#
#     a = review_data[count - 1]["review"]
#     b = a.replace("\n관람객\n", "")
#     c = b.strip()
#
#     if labeled1 == False:
#         print(asdf)
#         f2.write(c)
#         f2.write("\n")
#         number1 = number1 + 1
#     elif labeled2 == False and labeled1 == True:
#         f1.writelines(c)
#         f1.write("\n")
#         number2 = number2 + 1
#
#     count = count + 1
#
# print(number1)
# print(number2)
#
# f1.close()
# f2.close()
