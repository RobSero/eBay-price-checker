import webbrowser
import bs4
import re
import requests
import pprint #for testing purposes only, cleaner list printing

#  get string from searchbar
user_input = 'face mask'
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
# get item titles, quality
element_titles = soup.select('.s-item__title')
element_quality = soup.select('.SECONDARY_INFO')

# Get item prices & format
prices_list_strings = soup.select('.s-item__price')
subRegex = re.compile(r'£')
element_prices = []
for price in prices_list_strings:
  if 'to' in price.text: # ex. £3.99 to £ 4.99
    # split string into list with two values, remove '£', convert to floats and find average
    split_prices = price.text.split(' to ')
    average_price = sum([float(subRegex.sub('', split_prices[0])), float(subRegex.sub('', split_prices[1]))]) / 2
    element_prices.append(average_price)
  else:
    element_prices.append(float(subRegex.sub('', price.text)))



# element_prices =  [float(subRegex.sub('', price.text)) for price in prices_list_strings]


# # build data tuples
# results = []
# for i in range(len(element_titles)):
#   results.append((element_titles[i].text, element_prices[i], element_quality[i].text))
  
  
  
# average_price = round(sum(element_prices) / len(element_prices), 2)
# print(average_price)
# # pprint.pprint(results)
