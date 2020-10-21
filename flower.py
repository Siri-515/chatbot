import random
from datetime import datetime
"""
1. Details regarding the shop like contact numbers and address.
2. Types of services offered by this site.
3. Online/offline orders and tracking details
4. Details about different types of available products.
5. offer and dicounts available on products
"""
contact_number =  "79547352873" 
website = "www.laurestine-bhimavaram.com"

#this method is used to display the menu of flower boquet bot
def bot_options():
    print("**********************************************")
    print("1. About the Shop")
    print("2. Services Provided")
    print("3. Discount Offers")
    print("4. Order Details")
    print("0. For Exit")
    print("**********************************************")
    try:
        return int(input("enter your choice: "))
    except:
        print("only given choice 1 to 4")
    return 0

#about the shop address
def about_shop():
    address = "Laurestine is a Flower Shop located in J.P.Road,Opposite to Zoom Color Lab, Bhimavaram - 534202"
    contact_number =  "79547352873" 
    messsage = address + "\n" + "If you have any queries please contact this number "+ contact_number
    return messsage

#about the services provided by the flower boquet site
def services_Provided():
    messsage = '''we sell flowers and boquets along with customization
    We offer different decoration services for all types of events,
	Online bookings and Mid-night Deliveries are also available'''
    return messsage + "\n" + "For further assistance contact - " + contact_number

#about discounts and offers
def discounts():
    message = "As it is a festival season, we have special discounts on the products." + "\n" + "You can check them in our website www.laurestine-bhimavaram.com" + "\n"
    return message + "If you want to know more details contact - " + contact_number

#about different types of provided by the flowe boquet site
def order_details():
    print("Do you want to book an order or to track any order ?")
    res = input()
    if res == "book" or "booking":
	    msg = "visit " + website
	    return msg
    else:
	    print("Enter Tracking ID")


def greet_and_introduce():
    #declare some list of responses
    responses = [ "Hi There! I am Bot. I am here to help you. May I know your name please ?", 
    "Hi It is so nice to be in touch with you. Can you tell me your name ? "
    ]
    #pick a responses at random
    print(random.choice(responses))
def get_timeofday_greeting():
    current_time = datetime.today()
    timeofday_greeting = "Good Morning"
    if current_time.hour > 12 and current_time.hour < 17:
        timeofday_greeting = "Good Afternoon"
    elif current_time.hour >= 17 and current_time.hour < 22:
        timeofday_greeting = "Good Evening"
    else:
        timeofday_greeting ="Hi, Thats late"
    return timeofday_greeting
def welcome(name):
    messages = ["Nice to meet you", "Glad that you are here"]
    print("Hi "+ name +"," + " Welcome to Laurestine"+ "\n" + get_timeofday_greeting()+ ", " + random.choice(messages) )

def good_bye_message():
    print("Thank You for visiting our site")
def bot():
    greet_and_introduce()
    name = input("May I know your good name:")
    welcome(name)
    choice = bot_options()
    while choice != 0:
        if choice == 1:
            print(about_shop())
        elif choice == 2:
            print(services_Provided())
        elif choice == 3:
            print(discounts())
        elif choice == 4:
            print(order_details())
        choice = bot_options()
    good_bye_message()
        
bot()