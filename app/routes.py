from app import app, db
from app.models import Restaurant
from flask import jsonify

@app.route('/')
def index():
    return "Welcome to Restaurant Reviews!"

@app.route('/restaurants')
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name, 'review': r.review} for r in restaurants])

