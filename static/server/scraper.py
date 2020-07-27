import webbrowser
import bs4
import requests
import pprint #for testing purposes only, cleaner list printing

#  get string from searchbar
user_input = 'dynasty warrior 5 empires'
# if spaces, replace with '+'
search_item = user_input.replace(' ', '+')
# listing type: Buy it now, auction only etc.
listing_type = 'LH_BIN=1'

#  get html/css/js from site
res = requests.get(f'https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xiphone+x.TRS0&_nkw={user_input}&_sacat=0&{listing_type}')
print(res.status_code)

# if len = 0, show no results


# if len > 0, scape data
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# get item titles, quality and price
element_titles = soup.select('.s-item__title')
element_prices = soup.select('.s-item__price')
element_quality = soup.select('.SECONDARY_INFO')
# test print data

# build data tuples
results = []
for i in range(len(element_titles)):
  results.append((element_titles[i].text, element_prices[i].text, element_quality[i].text))
  
pprint.pprint(results)