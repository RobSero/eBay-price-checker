import webbrowser
import bs4
import re
import requests
import pprint #for testing purposes only, cleaner list printing


def result_generator(input=input):
  #  get string from searchbar
  user_input = input
  # if spaces, replace with '+'
  search_item = user_input.replace(' ', '+')
  # listing type: Buy it now, auction only etc.
  listing_type = 'LH_BIN=1'

  #  get html/css/js from site
  res = requests.get(f'https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw={user_input}&_sacat=0&rt=nc&{listing_type}')
  
  print(res.status_code)

#srp-river-results > ul > li:nth-child(7) > div > div.s-item__info.clearfix > a


  # if len > 0, scape data
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
 
  # get item titles, quality,link
  element_titles = soup.select('.s-item__title')
  element_link = soup.select('.s-item__image')
    # if len = 0, show no results
  if len(element_titles) == 0:
    return 'Could not find any results for this product, try checking your spelling'
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


# get item link through regex of tag
  link_regex = re.compile(r'href=\"(.*)BIN=1\"')
  element_link_list = []
  for atag in element_link:
    link_match = link_regex.search(str(atag))
    link_string = link_match.group().replace('href=','').replace('"','')
  # push to results
    element_link_list.append(link_string)
    
    
  # build data tuples in results
  results = []
  for i in range(len(element_titles)):
    results.append((element_titles[i].text, element_prices[i], element_quality[i].text, element_link_list[i]))
    
  # find average price
  average_price = round(sum(element_prices) / len(element_prices), 2)


  
  





  #  get first item image src
  item_image = soup.select('#srp-river-results > ul > li:nth-child(6) > div > div.s-item__image-section > div > a > div > img')
  # print(str(item_image[0]))
  # use regex to extract the src
  image_regex = re.compile(r'src=\"(.*)\"')
  src_match = image_regex.search(str(item_image[0]))
  image_source = src_match.group().replace('src=','').replace('"','')
  # print(image_source)


  product_data = {
    'name': user_input,
    'results': results,
    'image': image_source,
    'average_price': average_price
  }
  
  return product_data
