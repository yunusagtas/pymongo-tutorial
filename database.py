import pymongo

from pymongo import MongoClient


class Database:

    def __init__(self):
        print("database init")
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['adres-db']
        self.collection = self.db['adresler']
        self.query_parameters = {}

    #returns new _id for db
    def get_next_sequence(self, collection, name):
        return collection.find_and_modify(
            query={'_id': name},
            update={'$inc': {'seq': 1}},
            upsert=True,
            new=True
        ).get('seq')

    #insert new data
    def insert(self, name, surname, mail, phone):
        post_data = {
            '_id': self.get_next_sequence(self.db["idCounter"], "userid"),
            'name': name,
            'surname': surname,
            'mail': mail,
            'phone': str(phone)
        }
        return self.collection.insert_one(post_data).inserted_id

    # adds parameters to query_parameters
    def add_id_query(self, id):
        self.query_parameters["_id"] = id

    def add_name_query(self, name):
        self.query_parameters["name"] = name

    def add_surname_query(self, surname):
        self.query_parameters["surname"] = surname

    def add_mail_query(self, mail):
        self.query_parameters["mail"] = mail

    def add_phone_query(self, phone):
        self.query_parameters["phone"] = phone

    #mongodb query
    def find(self):
        query_parameters = self.query_parameters
        self.query_parameters = {}
        return self.collection.find(query_parameters)

