from flask import Flask , jsonify, request
import csv, ast


app = Flask(__name__)
count = 0

@app.route('/processjson', methods = ['POST'])
def processjson():

    data = request.get_json() #get the json payload

    data_file = open('data_file.csv', 'w')
    csv_writer = csv.writer(data_file)

    #if count == 0:
    #    # Writing headers of CSV file
    #    header = data.keys()
    #    csv_writer.writerow(header)
    #    count += 1

    # Writing data of CSV file
    csv_writer.writerow(data.values())

    data_file.close()

    #send back the result
    data['result'] = 'success'
    return jsonify(data)
