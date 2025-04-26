from app.bot import bot
from app.menus.utils import image_input_object
from app.menus.markup import main_markup, change_topics_markup

class Menu:
    def __init__(self, *, user_id, chat_id):
        self.user_id = user_id
        self.chat_id = chat_id
    
    def show_main(self):
        bot.send_photo(chat_id=self.chat_id, photo=image_input_object, reply_markup=main_markup)
    
    def show_change_topics(self):
        bot.send_message(chat_id=self.chat_id, text="Choose what you wanna do with topics:", reply_markup=change_topics_markup)
    
    