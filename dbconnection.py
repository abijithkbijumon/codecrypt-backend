from flask import Flask, render_template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# app = Flask(__name__)

uri = "mongodb+srv://abhijithkbijumon:bijumon1234@cluster0.hjiup31.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["code_crypt"]
collection = db["cost_of_living_index"]

#@app.route('/data')

def show_all_data():
    # Retrieve all documents from the MongoDB collection
    print("this is not error 22222222222222222")
    data = collection.find()

    # Convert the cursor to a list for easier rendering in the template
    data_list = list(data)

    # Render the template with the data
    #return render_template('show_data.html', data=data_list)
    print(data_list)
    return data_list

def connectionn():
    # Send a ping to confirm a successful connection
    try:
        print(client)
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        # Perform a MongoDB query (replace with your actual query)
        result = collection.find()
        val = []
        # Print the result
        for document in result:
            val.append(document)
        return val
    except Exception as e:
        print('HHHH')

# If you want to test the connection, call the connectionn function
# if __name__ == '__main__':
#     connectionn()
#     app.run(debug=True)
