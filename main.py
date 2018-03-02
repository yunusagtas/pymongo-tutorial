from flask import Flask, request

from database import Database
from bson.json_util import dumps
import json
import re

app = Flask(__name__)

@app.route('/', methods=['GET'])
def on_get():
    if "_id" in request.args and len(request.args) == 1:
        if request.args["_id"].isdigit():
            adress_database.add_query_parameter("_id", int(request.args["_id"]))
            query_result = list(adress_database.find())
            web_response = dumps(query_result)
            return web_response
        else:
            return "_id is not number"

    return "Github Page: <a target='_blank' href='https://github.com/yunusagtas/pymongo-tutorial'>https://github.com/yunusagtas/pymongo-tutorial</a>"

@app.route('/', methods=['POST'])
def on_post():

    required_insert_parameters = ("name", "surname", "mail", "phone")
    query_parameters = ("_id", "name", "surname", "mail", "phone")

    if "insert" in request.form:

        json_data = request.form['insert']
        try:
            data = json.loads(json_data)
        except Exception as e:
            return e.message

        if set(required_insert_parameters) <= set(data):
            for insert_parameter in data:
                if not (insert_parameter in required_insert_parameters):
                    return "Invalid insert parameter:%s" % insert_parameter
                if data[insert_parameter] == "":
                    return "Empty parameter:%s" % insert_parameter
                if insert_parameter == "mail" and not re.match(r"[^@]+@[^@]+\.[^@]+", data["mail"]):
                    return "Email is not valid"
                if insert_parameter == "phone" and not data["phone"].isdigit():
                    return "Phone is must be only numbers"

            inserted_id = adress_database.insert(data["name"], data["surname"], data["mail"], data["phone"])
            return str(inserted_id)
        else:
            return "Missing insert parameters"
    else:
        for posted_parameter in request.form:
            value = request.form[posted_parameter]

            if not (posted_parameter in query_parameters):
                return "Invalid parameter:%s" % posted_parameter
            if value == "":
                return "Empty parameter:%s" % posted_parameter
            if posted_parameter == "phone" and not value.isdigit():
                return "Phone is must be only numbers"

            if posted_parameter == "_id":
                value = int(value)

            adress_database.add_query_parameter(posted_parameter, value)

    query_result = list(adress_database.find())
    web_response = dumps(query_result)
    return web_response

if __name__ == '__main__':
    adress_database = Database()
    app.run()
