# author: QUAN YU
import requests
import re
import json
from bs4 import BeautifulSoup

# P: pages of a hotel to crawl: [1,353] as 16 Aug, 2017
# P = 3
P = 353

data = []

for pg in range(P):
    url = "https://www.tripadvisor.com.sg/Hotel_Review-g294264-d1447339-Reviews-or{}-Hard_Rock_Hotel_Singapore-Sentosa_Island.html".format(pg * 5)
    print("page: ", pg + 1)

    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
      
    review = soup.find_all('div', {'class':'review-container'})
    
    # crawling info from each review
    for rev in review:
        #
        # info from the main page
        user = rev.find("span", class_="expand_inline scrname")
        user = user.text
    
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
        # part = rev.find("p", class_ = "partial_entry").text.replace('More', '').strip(".").replace("\n","")
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

with open('trip_users.json','w') as f:
    json.dump(data,f,indent = 4)
