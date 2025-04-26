from telebot.util import quick_markup
from app.menus.utils import create_buttons_from_list

main_markup = quick_markup({
    "Change topics": {"callback_data": "Change topics"},
    "Change time": {"callback_data": "Change time"},
    "Show news": {"callback_data": "Show news"}
})

change_topics_markup = quick_markup({
    "Add topics": {"callback_data": "Add topics"},
    "Delete topics": {"callback_data": "Delete topics"},
    "Back to main menu": {"callback_data": "Back to main menu"}
})

add_topics_markup = quick_markup(create_buttons_from_list())

def create_delete_topics_markup(user_id):
     #get user choosed topics and pass this to crete_buttons_from_list fn
     quick_markup(create_buttons_from_list())

change_time_markup = quick_markup({
     "Set timezone": {"callback_data": "Set timezone"},
     "Set time for news": {"callback_data": "Set time for news"},
     "Back to main menu": {"callback_data": "Back to main menu"}
})

#add timezones list to create_buttons_from_list fn
set_timezone_markup = quick_markup(create_buttons_from_list())

time_for_news_markup = quick_markup({
     "Morning": {"callback_data": "Morning"},
     "Afternoon": {"callback_data": "Afternoon"},
     "After work": {"callback_data": "After work"},
     "Evening": {"callback_data": "Evening"},
})
