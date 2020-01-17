from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_restful import Api

from cassandradb import CassandraSession
from models.person import Person
from cassandra.cqlengine import connection

app = Flask(__name__)
CORS(app)
api = Api(app)
cassObj = CassandraSession()

@app.route('/')
def hello():
    connection.set_session(cassObj.session)
    return jsonify(dict(Person.objects().get())), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)