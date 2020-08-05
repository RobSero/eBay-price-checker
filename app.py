from flask import Flask, request, send_from_directory, send_file, render_template
from flask_restful import Resource, Api
# from flask_cors import CORS
from static.server.scraper import result_generator
from static.server.excelwriter import createSpreadsheet

app = Flask(__name__)
# app.run(debug=True)
api = Api(app)
# CORS(app)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def homeView():
    return render_template('index.html', flask_token='Hello')


class scrape_results(Resource):
    def get(self, userinput):
        results = result_generator(input=userinput)  
        return results



class create_results(Resource):
  # create spreadsheet
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



api.add_resource(scrape_results, '/api/search/<string:userinput>')
api.add_resource(create_results, '/api/send')
api.add_resource(send_results, '/api/send/<string:filename>')
