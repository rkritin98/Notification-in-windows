from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from win10toast import ToastNotifier 
import time
from datetime import date

def program():
        
    today = date.today()
    # Textual month, day and year	
    d = today.strftime("%B %d, %Y")

    header ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}
    req = Request("https://www.worldometers.info/coronavirus/country/india/",headers=header)
    html = urlopen(req)

    #print(html.status)

    soup = BeautifulSoup(html,"html.parser")

    #print(soup.prettify())

    new_cases = soup.find('li', {"class":"news_li"}).strong.text.split()[0]
    #print(new_cases)

    new_deaths = list(soup.find('li',{'class':'news_li'}).strong.next_siblings)[1].text.split()[0] #.next_siblings gives a list of subsequent next siblings of strong
    #print(new_deaths)

    notifier=ToastNotifier()

    message= f"{d}\nNew cases : {new_cases}\nDeaths : {new_deaths}"

    notifier.show_toast(title="COVID Update",msg= message, duration=5, icon_path=r"virus.ico")

while(True):
    program()
    time.sleep(86400) #24 hours in seconds