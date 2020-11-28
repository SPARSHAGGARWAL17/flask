from flask import Flask, jsonify,render_template,request

# This line is used to give flask app an unique name
app = Flask(__name__)

stores = [
    {
        'name' : 'My Wonderful Store',
        'items' : [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

# Route for pages
@app.route('/')
def home():
    return render_template('index.html')

# Default route is a get
@app.route('/store',methods = ['POST'])
def create_store():
    request_data = request.get_json()
    print(request_data)
    new_store = {
        'name': request_data["name"],
        'items' : [],
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    print(name)
    for i in stores:
        if name == i['name']:
            return jsonify({'data':i})
    return jsonify({'data':'Not found'})

@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    print(name)
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({'data':'Added Successfully'})
    return jsonify({'data':'Not found'})

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'data':'Not found'})

app.run(port=5000)