from datetime import datetime
from enum import unique
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import uuid
from sqlalchemy import create_engine



base = declarative_base()

#TSHIRTS TABLE
class Clothes(base):
    __tablename__ = 'clothes'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100))
    anime = Column(String(100))
    
    
    
    def __init__(self, name, anime):
        self.name = name
        self.anime = anime
        
    
        
class Colors(base):
    __tablename__ = 'colors'
    id = Column(Integer(), primary_key=True)
    color = Column(String(50), unique = True)  
    
    def __init__(self, color): 
        self.color = color
   
                 
class ClothesToColor(base):
    __tablename__ = 'clothestocolors'
    id = Column(Integer(), primary_key=True)
    color_id = Column(Integer())
    clothing_id = Column(Integer())
    stock = Column(Integer())
    image = Column(String(100), unique = True)
    type = Column(String(100))
    
    
        
    def __init__(self, color_id, clothing_id, stock, image, type):
            self.stock = stock
            self.color_id = color_id
            self.clothing_id = clothing_id
            self.image = image
            self.type = type
            
           
#USER SHOPPING CART TABLES 

#USER ACCOUNT TABLES 