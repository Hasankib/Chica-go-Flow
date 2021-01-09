import time
from flask import Flask, jsonify, request
from main import *
import sqlite3

conn = sqlite3.connect('database.db',check_same_thread=False)
print("Opened database successfully")

app = Flask(__name__)

global startingCommunity
global destinationCommunity
global popDestinations
global targetvalue

@app.route('/find', methods=['POST'])
def find():
    global startingCommunity
    global destinationCommunity
    find_json = request.get_json()

    if not find_json:
        return jsonify({'msg': 'Missing JSON'}), 400

    startingCommunity = int(find_json.get('startingCommunity'))
    destinationCommunity = int(find_json.get('destinationCommunity'))
    print(startingCommunity)
    print(destinationCommunity)

    y = "Community" + str(startingCommunity)
    cur = conn.cursor()
    cur.execute('Update ' + y + ' SET frequency = frequency + 1 WHERE neighbour = ' + str(destinationCommunity) + ';')
    print("updated")
    conn.commit()

    return jsonify({'startingCommunity': startingCommunity}), 200


@app.route('/returnedPath')
def get_returnedPath():
    global startingCommunity
    global destinationCommunity
    return {'returnedPath': str(startingCommunity+destinationCommunity)}


@app.route('/popDestGetter', methods=['POST'])
def popDestGetter():
    global targetvalue
    popDestGetter_json = request.get_json()
    targetvalue = 0
    if not popDestGetter_json:
        return jsonify({'msg': 'Missing JSON'}), 400
    
    if popDestGetter_json.get('targetvalue') == '':
        targetvalue = 0
        return jsonify({'targetvalue': targetvalue}), 200

    targetvalue = int(popDestGetter_json.get('targetvalue'))
    
    return jsonify({'targetvalue': targetvalue}), 200


@app.route('/popDestReciever')
def popDestReciever():
    global popDestinations
    global targetvalue
    placeholder = []
    popDestinations = []
    cur = conn.cursor()
    y = "Community" + str(targetvalue)
    if(targetvalue>=1 and targetvalue<=77):
        cur.execute("SELECT neighbour FROM " + y + " ORDER BY frequency DESC LIMIT 10;")
        placeholder = cur.fetchall()
        for i in placeholder:
            popDestinations.append(i[0])
        #for i in range (10):
            #popDestinations.append(i+targetvalue)
    return {'popDestReciever': str(popDestinations)}
