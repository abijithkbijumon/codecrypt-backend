from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dbconnection import connectionn

app = Flask(__name__)
CORS(app)

# OpenAI API Key
os.environ['API_KEY'] = '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'

client = OpenAI(api_key=os.environ.get("API_KEY"),)


def get_completion(prompt,datadb):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "finance assistant"},
            {"role": "user", "content": f''' User Details:
            - Name: {prompt["User Information"]["Name"]}
            - Age: "{prompt["User Information"]["Age"]}"
            - Monthly Income: {prompt["User Information"]["Annual Income"]}
            - Location: {prompt["User Information"]["Location"]}
            - Debt: "{prompt["User Information"]["Debt"]["Amount"]}"
            -interest : "{prompt["User Information"]["Debt"]["Interest Rate"]}" 
            -debt duration in years: "{prompt["User Information"]["Debt"]["Duration"]}" 
            The data related to the cost of living, rent cost, purchasing power, etc of the city is provided below
'''f'''
            "city": "{datadb["City"]}",
            "cost_of_living_index": "{datadb["Cost_of_Living_Index"]}",
            "rent_index": "{datadb["Rent_Index"]}",
            "cost_of_living_plus_rent_index":"{datadb["Cost_of_Living_Plus_Rent_Index"]}",
            "groceries_index": "{datadb["Groceries_Index"]}",
            "restaurant_price_index":"{datadb["Restaurant_Price_Index"]}",
            "local_purchasing_power_index":"{datadb["Local_Purchasing_Power_Index"]}"

            Please provide a JSON-formatted response with expense allocations based on the user's details, and the data about the city. Ensure that the monthly total expenses exactly matches the provided monthly income. Consider the user's age, location, income, and debt for accurate allocations. The location must be given utmost importance. The user prefers to have insurance. The allocation should be in rupees.
        ''''''
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
            The result must be in JSON format only as given above'''
            }
        ]
    )

    print(prompt)
    print(prompt["User Information"]["Name"])

    response = completion.choices[0].message.content
    # print("hi")
    # print(response)
    # print("hi2")
    # print(type(response))
    # print(response["Name"])

    return response


def get_completion1():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are an assistant"},
            {"role": "user", "content": '''The standard deviation and sortino value of certain mutual funds are provided........
            small cap:
            Kotak small cap Fund - standard deviation = 15.54 , sortino = 3.59
            Quant small cap Fund - Standard deviation = 19.27, sortino = 2.82
            SBI small cap Fund - Standard deviation = 13.96, sortino = 3.52
            NIppon India small cap Fund - Standard deviation = 16.5, sortino = 3.6
            Axis small cap Fund - Standard deviation = 12.83, sortino = 3.57
            Large Cap:
            ICICI prudential Bluechip Fund - standard deviation = 13.24 , sortino = 2.9
            Canara Robeco Bluechip Equity Fund - standard deviation = 13 , sortino = 2.33
            Kotak Bluechip Fund - standard deviation = 12.96 , sortino = 2.73
            Edelwelss Large cap Fund - standard deviation = 13.27 , sortino = 2.72
            Axis Bluechip Fund - standard deviation = 14.75 , sortino = 1.59

            Mid Cap:
            Quant Mid cap Fund - standard deviation = 17.23 , sortino = 3.21
            PGIM India Midcap - standard deviation = 15.72 , sortino = 3.27
            SBI Magnum Midcap Fund  - standard deviation = 14.76 , sortino = 3.33
            Kotak Emerging Equity Fund - standard deviation = 14.39 , sortino = 3.17
            sort the mutual funds in best to worst for an investor of risk tolerance 0.34 in the scale of 0 to 1 where 0 is less risk and 1 is high risk
            return the result in json format
            return Large cap Midcap and smallcap separately
             all the results must be strictly in json format no other results must be shown
             if there is any other extra characters added otherthan json remove them
             the three types of investments must be in same json manner
             please donot give unneccesory intro or endings in natural lanmguage
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

    # response = completion.choices[0].message
    # response = completion['choices'][0]['message']['content']
    response = completion.choices[0].message.content

    # print(response)
    # print(jsonify({"response" : response}))

    # return jsonify({"response" : response})
    return response

def get_completion2(prompt):
    print(prompt)
    risk = prompt["Survey Information"]["risk"]
    options = prompt["Survey Information"]["options"]
    dependency = prompt["Survey Information"]["dependency"]
    loseMoney = prompt["Survey Information"]["loseMoney"]
    riskOptions = prompt["Survey Information"]["riskOptions"]
    volatility = prompt["Survey Information"]["volatility"]

    riskTol = (risk + options + dependency + loseMoney + riskOptions + volatility) / 6
    print(riskTol)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are an json object provider that sends data to websites"},
            {"role": "user", "content": f'''if i give my risk tolerance is {riskTol} in investing on a firm of scale of 0 to 1,where 0 represents low risk taking mentality and 1 represent high risk taking mentality. Predict what percentage of my investment should go to FD, Digital Gold,Debt Mutual fund,Mutual Fund  Give the result in json format only
      for an eg: ''''''
      {
        "Fixed Deposit ": "",
        "Digital Gold": "",
        "Debt Mutual Fund": "",
        "Equity Mutual Fund": ""
      } 
      give only the json data.Dont give any useless comments.Just pure json data.I specifically say pure json data.Also dont give any introductory sentences. Just pure json data.Remember that
'''}

        ]
    )

    # response = completion.choices[0].message
    # response = completion['choices'][0]['message']['content']
    response = completion.choices[0].message.content

    # print(response)
    # print(jsonify({"response" : response}))

    # return jsonify({"response" : response})
    return response

@app.route("/", methods=['POST', 'GET'])
def query_view():
    if request.method == 'POST':
        print('step1')
        prompt = request.get_json()
        datadb =  connectionn(prompt["User Information"]["Location"])
        # print(datadb["City"])

        response = get_completion(prompt,datadb)
        # print("\n\nThis is response\n\n")
        # print(response)
        # print(response['choices'][0]['message']['content'])
        # res = response.choices[0].message.content
        # res2 = jsonify({"res2": res})
        # print(res2)
        # response_content = response.content
        # print(response_content)
        # return jsonify({"response": response})
        return response

   
    # return jsonify({"error": "Invalid method"})
    return response


@app.route("/new", methods=['POST', 'GET'])
def query2_view():
    if request.method == 'POST':
        print('step2')
        prompt = request.get_json()
        # response = get_completion1()
        response2 = get_completion2(prompt)
        # print(response2)
        # return render_template('hi.html', data=str(response))
        # return {response,response2}
        # return {"response": response, "response2": response2}
        return response2


    # return render_template('index.html')
    # return {response,response2}
    # return {"response": response, "response2": response2}
    return response2


# @app.route("/data", methods=["GET"])
# def show_data():
#     val = connectionn()
#     print(val)
#     return render_template("show_data.html", data=val)



    # return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)
