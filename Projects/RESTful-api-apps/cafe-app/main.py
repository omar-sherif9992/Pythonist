import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

MY_API_DOCUMENTATION="https://documenter.getpostman.com/view/17286684/U16bvU74"
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        """Converts SQl object into dictionary """
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        #return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/all",methods=['GET'])
def get_all_cafe():
    # cafes = db.session.query(Cafe).all()
    cafes=Cafe.query.all()
    all_cafes=[cafe.to_dict()for cafe in cafes]
    return jsonify(cafes=all_cafes)
@app.route("/search/")
def get_cafe():
    # cafes = db.session.query(Cafe).all()
    loc=request.args.get("loc")# http://127.0.0.1:5000/search/?loc=London
    cafes=Cafe.query.all()
    all_cafes=[cafe.to_dict()for cafe in cafes if loc in cafe.location]
    # cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if all_cafes==[]:
        return jsonify(error={
            "Not Found":"Sorry , we dont have a cafe at that location"
        })

    return jsonify(cafes=all_cafes)


@app.route("/random",methods=['GET'])
def get_random_cafe():
    # cafes = db.session.query(Cafe).all()
    cafes=Cafe.query.all()
    rand_cafe=random.choice(cafes)
    cafe = jsonify(
        # jsonify the dictionary
        cafe=jsonify(
            # jsonify the cafe data
            id=rand_cafe.id,
            name=rand_cafe.name,
            map_url=rand_cafe.map_url,
            img_url=rand_cafe.img_url,
            location=rand_cafe.location,
            seats=rand_cafe.seats,
            amenities=jsonify( has_toilet=rand_cafe.has_toilet,
            has_wifi=rand_cafe.has_wifi,
            has_sockets=rand_cafe.has_sockets,
            can_take_calls=rand_cafe.can_take_calls).json,
            coffee_price=rand_cafe.coffee_price,
        ).json  # convert the Response object to a dictionary
    )
    #return cafe
    #or
    return jsonify(cafe=rand_cafe.to_dict())

    # or
    # return jsonify(cafe={
    #     # Omit the id from the response
    #     # "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #
    #     # Put some properties in a sub-category
    #     "amenities": {
    #         "seats": random_cafe.seats,
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "has_sockets": random_cafe.has_sockets,
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "coffee_price": random_cafe.coffee_price,
    #     }
    # })



## HTTP GET - Read Record


def check(para:str)->bool:
    return para=="1" or para==1 or para=="True"
## HTTP POST - Create Record

@app.route("/add",methods=["POST"])
def add_cafe():
    try:
        new_cafe=Cafe(
        # id = request.form['id'],
        name = request.form['name'],
        map_url = request.form['map_url'],
        img_url = request.form['img_url'],
        location = request.form['location'],
        seats = request.form['seats'],
        has_toilet=check(str(request.form['toilet'])),
        has_wifi=check(str(request.form['wifi'])),
        has_sockets=check(str(request.form['sockets'])),
        can_take_calls=check(str(request.form['calls'])),
        coffee_price = request.form['price'])
        db.session.add(new_cafe)
        db.session.commit()
    except :

        return jsonify(response={"Fail": "Invalid Data"})

    return jsonify(response={"Success":"Successfully added a new cafe"})




## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>",methods=["PATCH"])
def update_price(cafe_id):
    new_price=request.args.get("new_price")# http://127.0.0.1:5000/search/?loc=London
    cafes=Cafe.query.all()
    cafe_update = None
    for cafe in cafes:
        if cafe.id==cafe_id:
            cafe_update=cafe
    if cafe_update==None:
        return jsonify(response={"Fail": "Invalid Data"})
    cafe_update.coffee_price=new_price
    db.session.commit()
    return jsonify(response={"Success":f"Successfully updated the price of {cafe_update.name}"})

@app.route("/report-closed/<cafe_id>",methods=["DELETE"])
def report_closed(cafe_id):
    api_key=request.args.get("api_key")
    if api_key!="iamthebest":
        return jsonify(response={"Not Authorized": "Invalid api ey"})
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe==None:
        return jsonify(response={"Not Found": "Invalid Id"})
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"Success":f"Successfully deleted {cafe.name}"})




## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
