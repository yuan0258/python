#coding = utf-8
#
from yahoo_finance import Share
import datetime
#
import urllib2
from bs4 import BeautifulSoup
#https://github.com/toomore/grs
from grs import Stock

def getgrsdata():
    stock = Stock('2618')                         
    print stock.moving_average(5)                 
    #print stock.moving_average_value(5)           
    #print stock.moving_average_bias_ratio(5, 10)  

def getopendata(id):
    url = 'http://mops.twse.com.tw/mops/web/ajax_t164sb04?'\
        'encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&TYPEK=all&isnew=false&co_id=2330&year=102&season=01'
    #url = 'http://www.google.com.tw'
    #response = urllib.request.urlopen(url)
    response = urllib2.urlopen(url)
    html = response.read().args
    sp = BeautifulSoup(html.decode('utf8'))  #cp950
    print(sp)

def getStock(id):
    stock = Share(str(id)+'.TW')
    today = datetime.date.today() #todays date
    data = stock.get_historical('2016-09-20', str(today))
    return data

def main():
    print ("I'm main function")
    #print getStock(2317)
    #getopendata(2317)
    getgrsdata()
if __name__ == "__main__":
    main()
