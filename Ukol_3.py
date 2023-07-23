from urllib.request import urlopen
from scrapy.selector import Selector

#function for scraping all home and away teams, and dates of matches
def get_matches(url):
    html = urlopen(url).read()
    xpath_date = '//div[@class="datetime-container"]'
    xpath_home = '//div[@class="team-container team-home"]/descendant::div[1]'
    xpath_away = '//div[@class="team-container team-away"]/descendant::div[1]'
    data = {}
    sel = Selector(text=html)
    data["date"] = sel.xpath(xpath_date).extract()
    data["home"] = sel.xpath(xpath_home).extract()
    data["away"] = sel.xpath(xpath_away).extract()
    return data

#filter all loosers with Brno together with dates
def get_LooserWithBrno(data):
    won_home = [i for i in range(len(data["home"])) if "team-looser" not in data["home"][i] and "Brno" in data["home"][i]] #indexes of matches which Brno won at home
    won_away = [i for i in range(len(data["away"])) if "team-looser" not in data["away"][i] and "Brno" in data["away"][i]] #indexes of matches which Brno won away
    loosers_away_name = [data["away"][i] for i in won_home] #get names of teams that lost with Brno when Brno was home team
    loosers_home_name = [data["home"][i] for i in won_away] #get names of teams that lost with Brno when Brno was away team
    date_won_home = [data["date"][i] for i in won_home] #get dates when Brno won at home
    date_won_away = [data["date"][i] for i in won_away] #get dates when Brno won away
    loosers_all = loosers_away_name + loosers_home_name
    dates_all = date_won_home + date_won_away
    return_data = {"loosers":loosers_all,"date":dates_all}
    return return_data

#clean loosers names and dates from garbage
def customize(LoosersData):
    loosers_customized = [i.split("<")[1].split(">")[1] for i in LoosersData["loosers"]]
    date_customized = [i.split("<")[1].split(">")[1].split("•")[0] for i in LoosersData["date"]]
    customized_data = {"loosers":loosers_customized,"date":date_customized}
    return customized_data

matches = get_matches("https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089")
loosers = get_LooserWithBrno(matches)
final = customize(loosers)

for i in range(len(final["loosers"])):
    print(final["date"][i]," ","sme porazili"," ",final["loosers"][i])
