from flask import Flask, request

from database import Database
from bson.json_util import dumps
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():

    if request.method == 'POST':

        #insert json data ("name", "surname", "mail", "phone")
        if "insert" in request.form:

            json_data = request.form['insert']
            try:
                data = json.loads(json_data)
            except Exception as e:
                print (e)
                return e.message

            if set(("name", "surname", "mail", "phone")) <= set(data):
                inserted_id = adress_database.insert(data["name"], data["surname"], data["mail"], data["phone"])
                return str(inserted_id) #returns inserted id
            else:
                return "Missing parameters"
        else: #query the parameters
            if "id" in request.form:
                adress_database.add_id_query(int(request.form['id']))
            if "name" in request.form:
                adress_database.add_name_query(request.form['name'])
            if "surname" in request.form:
                adress_database.add_surname_query(request.form['surname'])
            if "mail" in request.form:
                adress_database.add_mail_query(request.form['mail'])
            if "phone" in request.form:
                adress_database.add_phone_query(request.form['phone'])

    query_result = list(adress_database.find())
    web_response = dumps(query_result)
    return web_response

if __name__ == '__main__':
    adress_database = Database()
    app.run()
