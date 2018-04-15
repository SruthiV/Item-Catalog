from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="vinukonda.sruthi@gmail.com")
session.add(User1)
session.commit()

# Menu for Rajula's Kitchen
restaurant1 = Restaurant(name = "Rajula's Kitchen", user_id = "1")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name = "Masala Dosa", description = "South Indian, fermented crepe made from rice batter and black lentils.", price = "$2.99", restaurant = restaurant1, user_id = 1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Sambar Idly", description = " Rice cake with lentil-based vegetable stew.", price = "$7.50",  restaurant = restaurant1, user_id = 1)

session.add(menuItem2)
session.commit()


menuItem3 = MenuItem(name = "Pongal", description = "South indian porridge made with rice and yellow moong lentils. ", price = "$5.50", restaurant = restaurant1, user_id = 1)

session.add(menuItem3)
session.commit()


#Menu for Super Stir Fry
restaurant2 = Restaurant(name = "Biryani Pot", user_id = "1")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name = "Veg Biryani", description = "Rice dish layered with vegetables.", price = "$7.99", restaurant = restaurant2, user_id = 1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Avakai Biryani", description = "Rice dish layered with vegetables and mango pickle.", price = "$25",  restaurant = restaurant2, user_id = 1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Gongura Biryani", description = "Rice dish layered with vegetables and chutney made with Sorrel leaves. ", price = "$15", restaurant = restaurant2, user_id = 1)

session.add(menuItem3)
session.commit()


print "Added menu items!"
