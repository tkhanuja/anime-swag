from flask import Flask, request, jsonify
import json

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
    ret = []
    data = {}
   
    clothes = session.query(Clothes).all()
    # for c in clothes:
    #     if str(c.anime) not in ret:
            
    #         ret.append({str(c.anime): [{'name': str(c.name), 'details': []}]})
    #         index = ret.index(str(c.anime))
    #     else:
    #         index = ret.index(str(c.anime))
    #         ret[index][str(c.anime)].append({'name': str(c.name), 'details': []})
    #     ownership = session.query(ClothesToColor).filter_by(clothing_id= c.id).all()
    #     for o in ownership:
    #             color = session.query(Colors).filter_by(id = o.color_id).first().color
            
    #             ret[index][str(c.anime)][len(ret[index][str(c.anime)])-1]['details'].append({'color': str(color),'image':str(o.image), 'stock': int(o.stock), 'type': str(o.type)})
                
       
    # print(ret)    
    for c in clothes:
        if c.anime not in data:
            data[str(c.anime)] = []
            data[str(c.anime)].append({str(c.name): {'details': []} } )
        else: 
            data[str(c.anime)].append({str(c.name): { 'details': []} } )
        ownership = session.query(ClothesToColor).filter_by(clothing_id= c.id).all()
        for o in ownership:
            color = session.query(Colors).filter_by(id = o.color_id).first().color
            data[str(c.anime)][len(data[str(c.anime)])-1][str(c.name)]['details'].append({'color': str(color),'image':str(o.image), 'stock': int(o.stock), 'type': str(o.type)})
    print(data)
    return jsonify(data)

   
