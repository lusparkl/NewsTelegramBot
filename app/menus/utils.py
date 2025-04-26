from telebot.types import InputFile

def create_buttons_from_list(list_with_names):
    buttons = {}
    for name in list_with_names:
        buttons[name] =  {"callback_data": name}
    buttons["Back to main menu"] = {"callback_data": "Back to main menu"}

image_input_object = InputFile("/app/attachments/cartoon_news.jpg")