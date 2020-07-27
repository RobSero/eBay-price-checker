import webbrowser
import bs4
import requests

#  get string from searchbar
user_input = 'yvuybiub'
#  LOOP THROUGH A NUMBER OF PRODUCTS (SAY 15?)

#  get html/css/js from site
res = requests.get(f'https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xiphone+x.TRS0&_nkw={user_input}&_sacat=0')
print(res.status_code)

# if len = 0, show no results


# if len > 0, scape data
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# get item titles, quality and price
element_titles = soup.select('.s-item__title')
element_prices = soup.select('.s-item__price')
element_quality = soup.select('.SECONDARY_INFO')
# test print data
for i in range(len(element_titles)):
  print(element_titles[i].text)
  print(element_prices[i].text)
  print(element_quality[i].text)