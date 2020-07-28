from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api
from flask_cors import CORS
from static.server.scraper import result_generator
from static.server.excelwriter import createSpreadsheet

app = Flask(__name__)
app.debug = True
api = Api(app)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def yo():
  return 'yo'


# #  search result api
# @app.route('/api/search/<input>')
# def scrape_results(input):
#   return result_generator(input=input)




# #  excel spreadsheet api
# @app.route('/api/send/')
# def send_spreadsheet():
#   return createSpreadsheet(ebayData)

#  search result api
# @app.route('/api/search/<input>')
# def scrape_results(input):
#   return result_generator(input=input)


class scrape_results(Resource):
    def get(self, userinput):
        results = result_generator(input=userinput)  
        return results



class send_results(Resource):
    def post(self):
        print('recieved')
        user_email = request.json['name']
        print(user_email)
        createSpreadsheet(request.json)
        print(f'{request.json["name"]} - eBayData.xlsx')
        # return  send_from_directory('./', f'{request.json["name"]} - eBayData.xlsx', as_attachment=True)
        f = open(f'{request.json["name"]} - eBayData.xlsx', 'rb')
        output = make_response(f.read())
        output.headers["Content-Disposition"] = "attachment; filename=report.xlsx"
        output.headers["Content-type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        f.close()
        return output






api.add_resource(scrape_results, '/api/search/<string:userinput>')
api.add_resource(send_results, '/api/send')


jsonData = {
  "average_price": 109.68,
  "user_email" : "john@email.com",
  "image": "https://i.ebayimg.com/thumbs/images/g/VG0AAOSwqwRdxs7E/s-l225.jpg",
  "name": "tombi 2",
  "results": [
    [
      "Name 1",
      74.99,
      "Pre-owned",
      "https://www.ebay.co.uk/itm/PlayStation-1-Tombi-2-Rental-Copy-Rare-Collectors-Item/353109158363?hash=item5236f229db%3Ag%3AY3MAAOSwUQBe6PzJ&amp;LH_BIN=1"
    ],
    
    [
      "Name 2",
      74.99,
      "Pre-owned",
      "https://www.ebay.co.uk/itm/PlayStation-1-Tombi-2-Rental-Copy-Rare-Collectors-Item/353109158363?hash=item5236f229db%3Ag%3AY3MAAOSwUQBe6PzJ&amp;LH_BIN=1"
    ],
    
    [
      "Name 3",
      74.99,
      "Pre-owned",
      "https://www.ebay.co.uk/itm/PlayStation-1-Tombi-2-Rental-Copy-Rare-Collectors-Item/353109158363?hash=item5236f229db%3Ag%3AY3MAAOSwUQBe6PzJ&amp;LH_BIN=1"
    ]
  ]
}