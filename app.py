from flask import Flask, render_template, request, jsonify 
from openai import OpenAI
import os
from dbconnection import show_all_data,connectionn




app = Flask(__name__) 

# OpenAI API Key 
# openai.api_key = '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'
os.environ['API_KEY'] = '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'

client = OpenAI(api_key=os.environ.get("API_KEY"),)
def get_completion(prompt): 
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": ''' User Details:
        - Name: "Nived"
        - Age: "30"
        - Monthly Income: "150,000 rupees"
        - Location: "banglore"
        - Debt: "300,000 rupees"
        -interest : "12%" 
        
        Please provide a JSON-formatted response with expense allocations based on the user's details. Ensure that the monthly total expenses match the monthly income of 150,000 rupees. Consider the user's age, location, income, and debt for accurate allocations. The user prefers to have insurance. The allocation should be in rupees.
        
        {
          "Name": "",
          "Age": "",
          "Monthly Income": "",
          "Debt": "",
          "Location": "",
          "Expense Allocation": {
            "Debt Repayment": {
              "Monthly Allocation": ""
            },
            "Emergency Fund": {
              "Monthly Allocation": ""
            },
            "Savings and Investments": {
              "Monthly Allocation": ""
            },
            "Living Expenses": {
              "Monthly Allocation : ""
            },
            "Healthcare and Insurance": {
              "Monthly Allocation": ""
            }
          }
        }
	 The result must be in JSON format only '''
        }
  ]
)

    #print(completion.choices[0].message)

    response = completion.choices[0].message
    
    return response


def get_completion1(prompt): 
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "You are a assistant"},
      {"role": "user", "content":'''The standard deviation and sortino value of certain mutual funds are provided........
      small cap:
      Kotak small cap Fund - standard deviation = 15.54 , sortino = 3.59
      Quant small  cap Fund - Standard deviation = 19.27, sortino = 2.82
      SBI small  cap Fund - Standard deviation = 13.96, sortino = 3.52
      NIppon India small  cap Fund - Standard deviation = 16.5, sortino = 3.6
      Axis small  cap Fund - Standard deviation = 12.83, sortino = 3.57
      Large Cap :
      ICICI prudential Bluechip Fund - standard deviation = 13.24 , sortino = 2.9
      Canara Robeco Bluechip Equity Fund - standard deviation = 13 , sortino = 2.33
      Kotak  Bluechip Fund - standard deviation = 12.96 , sortino = 2.73
      Edelwelss Large cap Fund - standard deviation = 13.27 , sortino = 2.72
      Axis Bluechip Fund - standard deviation = 14.75 , sortino = 1.59

      Mid Cap:
      Quant Mid cap Fund - standard deviation = 17.23 , sortino = 3.21
      PGIM India Midcap - standard deviation = 15.72 , sortino = 3.27
      SBI Magnum Midcap Fund  - standard deviation = 14.76 , sortino = 3.33
      Kotak Emerging Equity Fund - standard deviation = 14.39 , sortino = 3.17
      sort the mutual funds in best to worst for an investor of risk tolerance 0.34 in the scale of 0 to 1 where 0 is less risk and 1 is high risk
      return the reult in json format
      return Large cap Midcap and smallcap separately
      eg: {
          "Investor_Risk_Tolerance": 0.8,
          "Mutual_Funds_Ranking": [
            {
              "Fund_Name": "Kotak Small Cap Fund",
              "Rank": 1
            },
            {
              "Fund_Name": "Axis Small Cap Fund",
              "Rank": 2
            },
            {
              "Fund_Name": "SBI Small Cap Fund",
              "Rank": 3
            },
            {
              "Fund_Name": "Nippon India Small Cap Fund",
              "Rank": 4
            },
            {
              "Fund_Name": "Quant Small Cap Fund",
              "Rank": 5
            }
          ]
        }
        '''}
      
  ]
  )

    #print(completion.choices[0].message)

  response = completion.choices[0].message
    
  return response

@app.route("/", methods=['POST', 'GET'])    
def query_view(): 
  if request.method == 'GET': 
    print('step1') 
    prompt = request.args.get('prompt')
    #collect = connectionn()
    response = get_completion(prompt) 
    print(response) 
  return render_template('hi.html',data = response)

@app.route("/new", methods=['POST', 'GET'])    
def query2_view(): 
  if request.method == 'GET': 
    print('step2') 
    prompt = request.args.get('prompt')
    #collect = connectionn()
    response = get_completion1(prompt) 
    print(response) 
  return render_template('hi.html',data = response)

		
  return render_template('index.html') 

@app.route("/data", methods = ["GET"])
def show_data():
  val = connectionn()
  return render_template("show_data.html",data = val)


if __name__ == "__main__": 
	app.run(debug=True) 
