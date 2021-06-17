# -*- coding: utf-8 -*-


from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json 
import collections
import math

def tree():
    return collections.defaultdict(tree)

driver = webdriver.Chrome('D:\chromedriver_win32/chromedriver.exe')


def rating_list_crawler(desired_):
    page_number = 1
    while(page_number != desired_):
        
        for i in range(1, 11):
            driver.get("https://movie.naver.com//movie/bi/mi/pointWriteFormList.nhn?code=161850&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}".format(page_number))

            f = open("D:/movie_review/new_data_review/i can speak/review_history2.txt".format(((page_number-1)*10)+i), "a+t")
            
            req = requests.get(driver.current_url)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')  
            css_select = "body > div > div > div.score_result > ul > li:nth-child({}) > div.score_reple > dl > dt > em:nth-child(1) > a > span".format(i)
            user_name_list = soup.select('body > div > div > div.score_result > ul > li > div.score_reple > dl > dt > em > a > span')
            driver.find_element_by_css_selector(css_select).click()
            page=driver.current_url
            user_req = requests.get(page)
            user_html = user_req.text
            user_soup = BeautifulSoup(user_html, 'html.parser')
            
            h5 = user_soup.find('h5',attrs={'class':'sub_tlt underline'})
            div = h5.find('div', attrs={'class':'h5_right_txt'})
            number = div.find('strong')
            number0 = number.text
            number1 = number0.replace('<strong class="c_88 fs_11">','')
            number2 = number1.replace('</strong>','')
            number3 = float(number2)
            number4 = math.ceil(number3/10)
            page_num=1
            data_list = []
            while (page_num<=number4):
                page=driver.current_url
                user_req1 = requests.get(page+"&page="+str(page_num))
                user_html1 = user_req1.text
                user_soup1 = BeautifulSoup(user_html1, 'html.parser')
                table = user_soup1.find('table', attrs={'class':'list_netizen'})
                table_body = table.find('tbody')
    
                rows = table_body.find_all('tr')
                for row in rows:
                    title = row.find('td', attrs={'class':'title'})
                    score = title.find('div')
                    em = score.find_all('em')
                    i=0
                    for a in em:
                        data_list.append(a.text)
                if page_num<1000:        
                    page_num+=1
                else:
                    page_num=number4+1
            data_modi =""
            for j in data_list:
                data_modi = data_modi + j + " " 
            print((page_number-1)*10+int(i))
            f.write(str(data_modi))
            
            f.write("\n")        
        page_number += 1
       
    
if __name__ == "__main__":
    rating_list_crawler(1465)