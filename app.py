from flask import Flask
from static.server.scraper import result_generator
app = Flask(__name__)

@app.route('/')
def yo():
  return 'yo'


#  search result api
@app.route('/search/<input>')
def scrape_results(input):
  return result_generator(input=input)


#  excel spreadsheet api
