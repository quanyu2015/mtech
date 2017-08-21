# author: QUAN YU
# reference:
# https://github.com/AndyMeng/TripAdvisorRatingBoosting/blob/master/iss_selenium.py

import re
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

TRAVELLER_TYPES={
    "Families":"taplc_location_review_filter_controls_hotels_0_filterSegment_Families",
    "Couples":"taplc_location_review_filter_controls_hotels_0_filterSegment_Couples",
    "Solo":"taplc_location_review_filter_controls_hotels_0_filterSegment_Solo",
    "Business":"taplc_location_review_filter_controls_hotels_0_filterSegment_Business",
    "Friends":"taplc_location_review_filter_controls_hotels_0_filterSegment_Friends"
}

def wait_for_element(option,  delay=5):
        option.click()
        WebDriverWait(driver, delay).until(EC.staleness_of(option))

ta_url = 'https://www.tripadvisor.com.sg/Hotel_Review-g294264-d1447339-Reviews-Hard_Rock_Hotel_Singapore-Sentosa_Island.html'

# driver = webdriver.Chrome()
driver = webdriver.Firefox()

def wait_js(option, delay = 5):
        driver.execute_script('arguments[0].click()', option)
        WebDriverWait(driver, delay).until(EC.staleness_of(option))

def main():
    data = []
  
    try:
        driver.get(ta_url)
        keys = list(TRAVELLER_TYPES)
        
        for key in keys[2:]:
            print("key: '"+key+"'\n")
            tv_type = driver.find_element_by_id(TRAVELLER_TYPES[key])
            wait_js(tv_type)

            # find pages to crawl
            page = driver.find_elements(By.CSS_SELECTOR, 'span.pageNum.last.taLnk')[0].get_attribute("data-page-number")
            print("Pages: "+page+"\n")
   
            for p in range(int(page)):
            # for p in range(3):
                print("p"+str(p+1)+"\n")

                review_containers = driver.find_elements(By.CSS_SELECTOR, 'div.review-container')
                
                # crawling info from each review
                for container in review_containers:
                    html = container.get_attribute('innerHTML')
                    rev = BeautifulSoup(html, 'html.parser')

                    # info from the main page
                    user = rev.find("span", class_="expand_inline scrname")
                    user = user.text
                    # print(user)

                    member = rev.find("div",{'class':"memberOverlayLink"})
                    if(member is None):
                        continue
                    empty, uid, src = re.split('UID_|-|-SRC_', member['id'])

                    # user rating
                    rate = rev.find("span", class_=re.compile("ui_bubble_rating"))
                    rate = rate['class'][1].strip("bubble_")
                    
                    date = rev.find("span", class_="ratingDate relativeDate")['title']
                    
                    # review title and content
                    quote = rev.find("span", class_="noQuotes").text
                    part = rev.find("p", class_ = "partial_entry").text
                    part = re.sub('More$', '', part).strip(".").replace("\n"," ")
                
                    mobile = rev.find("a", class_="viaMobile")
                    if mobile:
                            tool = "mobile"
                    else: 
                            tool = "pc"
    	
        #
                    # info from mouse hover page
                    hover = requests.get("https://www.tripadvisor.com.sg/MemberOverlay", params = {"uid": uid})
                    overlay = BeautifulSoup(hover.content, "html.parser")
                
                    # user level
                    level_ = overlay.find('div', {'class':'badgeinfo'})
                    level = level_.span.text if level_ else "none"
               
                    # membership year
                    desc = overlay.find("ul", class_="memberdescriptionReviewEnhancements")
                    user_year = desc.li.text.strip()[-4:]

                    # other info
                    info = {
                        'age': "none",
                        'gender': "none",
                        'country': "none"
                    }
                    info_all = desc.text.strip().split("\n")
                    if(len(info_all) == 2):
                        infos = info_all[1].split()
                        if("From" in info_all[1]):
                            info['country'] = " ".join(infos[1:])
                        if("Man" in info_all[1] or " man" in info_all[1]):
                            info['gender'] = "man"
                        if("Woman" in info_all[1] or "woman" in info_all[1]):
                            info['gender'] = "woman"
                        if re.match("\d+", info_all[1]):
                            info['age'] = infos[0]
                        if("from" in info_all[1]):
                            idx = infos.index('from') + 1
                            info['country'] = " ".join(infos[idx:])

		    #  
                    cnts = overlay.find_all("li",{"class":'countsReviewEnhancementsItem'})
                    out = {
                        'contribution': '0', 
                        'vote': '0', 
                        'city': '0',
                        'photo': '0'
                      }
                    for cnt in cnts:
                        item = cnt.text.strip()
                        if("Contribution" in item):
                            out["contribution"] = item.split()[0]
                        elif("visited" in item):
                            out["city"] = item.split()[0]
                        elif("vote" in item):
                            out["vote"] = item.split()[0]
                        elif("Photo" in item):
                            out["photo"] = item.split()[0]

                    # rating distribution
                    distr = {
                    "Excellent":'0',
                    "Very good":'0',
                    "Average":'0',
                    "Poor": '0',
                    "Terrible":'0'
                            }
                    temp = overlay.find_all("span", class_="rowCountReviewEnhancements rowCellReviewEnhancements")
                    if len(temp) == 5:
                            distr["Excellent"] = temp[0].text.strip()
                            distr["Very good"] = temp[1].text.strip()
                            distr["Average"] = temp[2].text.strip()
                            distr["Poor"] = temp[3].text.strip()
                            distr["Terrible"] = temp[4].text.strip()
 
                    # output    
                    item = {
                    "user": user,
                    "traveler_type": key,
                    "country": info['country'], 
                    "age": info['age'],
                    "gender": info['gender'],
                    "user_year": user_year,
                    "uid": uid,
                    "review": {
                        "date": date,
                        "tool": tool,
                        "title": quote,
                        "cnt": part
                              },
                    "distribution": distr,
                    "rate": rate,
                    "level": level,
                    "count": out,
                    }
                    data.append(item)
                    
                print(len(data))
                print("---")
                # next page    
                if p < int(page) - 1:
                    wait_for_element(driver.find_elements(By.CSS_SELECTOR, 'span.nav.next.taLnk')[0])
            
            print(key, " finished\n")
            # Deselect the traveller type
            tv_type = driver.find_element_by_id(TRAVELLER_TYPES[key])
            wait_js(tv_type)

    except Exception as error:
        print("Web Driver exits unexpectedly with message: {0}".format(str(error)))
    
    finally:
        driver.quit()
        with open('tripadv2_2.json','w') as f:
            json.dump(data,f,indent = 4)

            
if __name__== "__main__":
    main()
