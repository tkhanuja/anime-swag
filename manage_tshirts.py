from sqlalchemy.orm import sessionmaker
from models import base, Clothes, Colors, ClothesToColor
from app import session


#def __init__(self, name, anime, path, type):
#def __init__(self, color_id, clothing_id, stock):
# all = session.query(Tshirts).all()
#tshirts

def add_clothing(name, anime) :
    if not session.query(Clothes).filter_by(name = name).first():
        clothing = Clothes(name, anime )
        session.add(clothing)
        session.commit()
    
def add_colors(color):
    if not session.query(Colors).filter_by(color = color).first():
        color = Colors(color)
        session.add(color)
        session.commit()

def ownership(name, color, stock, path, type):
    clothing_id = (session.query(Clothes).filter_by(name = name).first()).id
    color_id = (session.query(Colors).filter_by(color = color).first()).id
    ownership = ClothesToColor(color_id, clothing_id, stock, path, type)
    session.add(ownership)
    session.commit()
    
def populate_tables(name, anime, stock, color, path, type):
    # add_clothing(name, anime)
    # add_colors(color)
    ownership(name, color, stock, path, type)
    
# animes  
naruto = 'Naruto'
dbz = 'Dragon Ball Z'
mha = 'My Hero Academia'
op = 'One Piece'

# types
tshirt = 'T-shirt'
sweatshirt = 'Sweatshirt'
tank = 'Tank Top'

#colors
black = 'Black'
red = 'Red'
orange = 'Orange'
blue = 'Navy Blue'
green = 'Green'
white = 'White'


populate_tables('sharingan', naruto, 3, black, 'images.sharingan_black.jpg', tshirt)
# populate_tables('Akatsuki T-shirt', naruto, 0, red, 'images.akatsuki_cloud_red.jpg',  tshirt)


