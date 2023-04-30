# libraries
pip install telebot
import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
import requests
import json
from geopy.geocoders import Nominatim

# Set up geolocator
geolocator = Nominatim(user_agent="my-app")

# give your bot TOKEN API ID
TOKEN = str("Give your Bot Token ID")



# CODE
## fucntion to fetch the address based on the latitude and longitude
def get_address(lat, long):
    url = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={long}"
    response = requests.get(url).json()
    if 'address' in response:
        address = response['address']
        return f"{address.get('road', '')}"
    else:
        return "Address not found"
        
        
## Bot code
bot = telebot.TeleBot(TOKEN)
details = {}

@bot.message_handler(commands=['start'])
def start_message(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_location = KeyboardButton(text="Share Location", request_location=True)
    keyboard.add(button_location)
    bot.send_message(chat_id=message.chat.id, text="Please the destination location:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Swap Location🔁")
def swap_locations(message: Message):
    details['user_latitude'], details['destination_latitude'] = details['destination_latitude'], details['user_latitude']
    details['user_longitude'], details['destination_longitude'] = details['destination_longitude'], details['user_longitude']

    user_road = get_address(details['user_latitude'], details['user_longitude'])
    destination_road = get_address(details['destination_latitude'], details['destination_longitude'])
    bot.reply_to(message, f"User Location: {user_road}\nDestination Location: {destination_road}")

@bot.message_handler(func=lambda message: message.text == "Book")
def book_ride(message: Message):
    bot.reply_to(message,"Booking confirmed! \n\nDriver name : \ncontact number : \nAuto number : \nFare: \nEstimated arrival time :")
    print(details)

@bot.message_handler(func=lambda message: message.text == "Clear")
def clear_details(message: Message):
    global details
    details = {}
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_location = KeyboardButton(text="Share Location", request_location=True)
    button_swap = KeyboardButton(text="Swap Location")
    keyboard.add(button_location)
    bot.reply_to(message, f"Details cleared. Please share the destination location again.", reply_markup=keyboard)

@bot.message_handler(content_types=['location'])
def handle_location(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    if 'destination_latitude' not in details:
        details['destination_latitude'] = latitude
        details['destination_longitude'] = longitude
        bot.reply_to(message, f"Please share your location:")
    else:
        details['user_latitude'] = latitude
        details['user_longitude'] = longitude
        user_road = get_address(details['user_latitude'], details['user_longitude'])
        destination_road = get_address(details['destination_latitude'], details['destination_longitude'])
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button_book = KeyboardButton(text="Book")
        button_swap = KeyboardButton(text="Swap Location🔁")
        button_clear = KeyboardButton(text="Clear")
        keyboard.add(button_swap)
        keyboard.add(button_book, button_clear)
        bot.reply_to(message, f"User Location: {user_road}\nDestination Location: {destination_road}", reply_markup=keyboard)

    if 'destination_latitude' in details and 'user_latitude' in details:
      user_road = get_address(details['user_latitude'], details['user_longitude'])
      destination_road = get_address(details['destination_latitude'], details['destination_longitude'])

bot.polling()
     
        
