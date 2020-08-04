from flask import Flask, request, send_from_directory, send_file
from flask_restful import Resource, Api
from flask_cors import CORS
from static.server.scraper import result_generator
from static.server.excelwriter import createSpreadsheet

app = Flask(__name__)
app.run(debug=True)
api = Api(app)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


class home(Resource):
    def get(self):
        return '<h1>Hello</h1>'



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



class create_results(Resource):
  # createspreadsheet
    def post(self):
        print('recieved')
        user_email = request.json['name']
        print(user_email)
        createSpreadsheet(request.json)
        print(f'{request.json["name"]}_eBayData.xlsx')
        return {'message' : f'{request.json["name"]}'}
     
        #  send spreadsheet
    
        
class send_results(Resource):
  def get(self, filename):
        print('recieved')
        return send_file(f'./sheets/{filename}_eBayData.xlsx', as_attachment=True)



# api.add_resource(scrape_results, '/')
api.add_resource(scrape_results, '/api/search/<string:userinput>')
api.add_resource(create_results, '/api/send')
api.add_resource(send_results, '/api/send/<string:filename>')

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