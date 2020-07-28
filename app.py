from flask import Flask
from flask_cors import CORS
from static.server.scraper import result_generator


app = Flask(__name__)
CORS(app)


@app.route('/')
def yo():
  return 'yo'


#  search result api
@app.route('/api/search/<input>')
def scrape_results(input):
  return result_generator(input=input)


#  excel spreadsheet api
