from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

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



#Menu for UrbanBurger
restaurant1 = Restaurant(name = "Rajula's Kitchen")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(name = "Sambar Idly", description = "Juicy grilled veggie patty with tomato mayo and lettuce", price = "$7.50",  restaurant = restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(name = "Masala Dosa", description = "with garlic and parmesan", price = "$2.99", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Pongal", description = "Juicy grilled chicken patty with tomato mayo and lettuce", price = "$5.50", restaurant = restaurant1)

session.add(menuItem2)
session.commit()


#Menu for Super Stir Fry
restaurant2 = Restaurant(name = "Biryani Pot")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name = "Veg Biryani", description = "With your choice of noodles vegetables and sauces", price = "$7.99", restaurant = restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Avakai Biryani", description = " A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price = "$25",  restaurant = restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Gongura Biryani", description = "Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ", price = "15", restaurant = restaurant2)

session.add(menuItem3)
session.commit()


print "added menu items!"
