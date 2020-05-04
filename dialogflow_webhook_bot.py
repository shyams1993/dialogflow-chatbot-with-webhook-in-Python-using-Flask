import dialogflow_v2beta1
import dialogflow_v2
from flask import Flask, request, make_response, jsonify
import pandas as pd
app = Flask(__name__)
df = pd.read_csv(r) #please copy the downloaded csv file as path and paste inside the brackets after r (shift + right click on the file; select copy as path)
@app.route('/')
def index():
  return 'Hello World!'


def results():
    req = request.get_json(force=True)
    action = req.get('queryResult').get('action')
    if action == 'getAge':
        res = getAge(req)
    else:
        res = getdob(req)
    
    return {'fulfillmentText': res}

def getAge(req):	
    element = req.get('queryResult').get('parameters').get('given-name')
    age = list(df['age'][df['name']==element].values)
    name = list(df['name'][df['name']==element].values)
    updated_name = str(name)[1:-1].replace("'","")
    result = str(age)[1:-1]
    result_new = updated_name+"'s age is "+result
    return(result_new)

def getdob(req):	
    element = req.get('queryResult').get('parameters').get('given-name')
    dob = list(df['dob'][df['name']==element].values)
    name = list(df['name'][df['name']==element].values)
    updated_name = str(name)[1:-1].replace("'","")
    result = str(dob)[1:-1].replace("'","")
    result_new = updated_name+"'s DOB is "+result
    return(result_new)

@app.route('/webhook', methods=['GET','POST'])
def webhook():
  # return response
  return make_response(jsonify(results()))
#run the app
if __name__ == '__main__':
  app.run(port=8080,debug=True)