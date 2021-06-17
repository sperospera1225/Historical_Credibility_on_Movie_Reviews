# -*- coding: utf-8 -*-

from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json 
import collections
 
def tree():
    return collections.defaultdict(tree)


driver = webdriver.Chrome('D:\chromedriver_win32/chromedriver')
def crawling(desire_):
    with open("D:/movie_review/new_data_review/i can speak/review_data.json", "w", encoding='utf-8') as write_file:
        page_number = 1
        number = 1
        while(page_number<=desire_):
            driver.get("https://movie.naver.com//movie/bi/mi/pointWriteFormList.nhn?code=161850&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}".format(page_number))
            req = requests.get(driver.current_url)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            review_list = soup.select('body > div > div > div > ul > li > div > p')
            rating_list = soup.select('body > div > div > div.score_result > ul > li > div.star_score > em')
            date_list = soup.select('body > div > div > div.score_result > ul > li > div.score_reple > dl > dt')
            review_sympathy_list = soup.select('body > div > div > div.score_result > ul > li > div.btn_area > a._sympathyButton > strong')
            review_unsympathy_list = soup.select('body > div > div > div.score_result > ul > li > div.btn_area > a._notSympathyButton > strong')
    
            for a, b, c, d, e in zip(review_list,rating_list,date_list,review_sympathy_list,review_unsympathy_list):
                data = tree()
                id = c.text.split()[0]
                date = c.text.split()[1] + " " + c.text.split()[2]
                data['no'] = number
                data['id'] = id
                data['review'] = str(a.text)
                data['rating'] = str(b.text)
                data['sympathy'] =str(d.text)
                data['unsympathy'] = str(e.text)
                data['date'] = date
                
                data_list.append(data)
                number = number + 1
            while len(data_list) < 10 and page_number != desire_:
                data_list.append(data_list[-1])
                print(number)
                number = number+1
            page_number = page_number + 1
        json.dump(data_list, write_file, ensure_ascii=False, indent=3)

if __name__ == "__main__":
    # driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome('D:\chromedriver_win32/chromedriver')
    data_list = []
    crawling(1454)