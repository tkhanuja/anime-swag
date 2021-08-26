from flask import Flask, request, jsonify

from sqlalchemy.orm import sessionmaker
from models import base, Clothes, Colors, ClothesToColor
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from flask_cors import CORS
from sqlalchemy import create_engine

app = Flask(__name__)
CORS(app)
engine = create_engine("sqlite:///storage.db")
Session = sessionmaker(bind=engine)
session = Session()

# base.metadata.drop_all(engine)
base.metadata.create_all(engine)



@app.route('/')
def index():
    data = {}
    clothes = session.query(Clothes).all()
    for c in clothes:
        if c.anime not in data:
            data[c.anime] = []
            data[c.anime].append({c.name: {'details': []} } )
        else: 
            data[c.anime].append({c.name: { 'details': []} } )
        ownership = session.query(ClothesToColor).filter_by(clothing_id= c.id).all()
        for o in ownership:
            color = session.query(Colors).filter_by(id = o.color_id).first().color
            data[c.anime][len(data[c.anime])-1][c.name]['details'].append({'color': color,'image':o.image, 'stock': o.stock, 'type': o.type})
      
    return jsonify(data)

    
