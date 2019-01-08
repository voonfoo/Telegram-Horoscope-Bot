from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def initialization():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    horoscopes = ["Aries ♈", "Taurus ♉", "Gemini ♊", "Cancer ♋", "Leo ♌", "Virgo ♍"]
    horoscopes_1 = ["Libra ♎", "Scorpio ♏", "Sagittarius ♐", "Capricorn ♑", "Aquarius ♒", "Pisces ♓"]
    for horoscope, horoscope_1 in zip(horoscopes, horoscopes_1):
        markup.add(InlineKeyboardButton(text=horoscope, callback_data="horoscope_{}".format(horoscope)),
                    InlineKeyboardButton(text=horoscope_1, callback_data="horoscope_{}".format(horoscope_1)))
    return markup

def settings_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(text="Change Horoscope", callback_data=f"change_horoscope"))
    return markup

def change_horoscope():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    horoscopes = ["Aries ♈", "Taurus ♉", "Gemini ♊", "Cancer ♋", "Leo ♌", "Virgo ♍"]
    horoscopes_1 = ["Libra ♎", "Scorpio ♏", "Sagittarius ♐", "Capricorn ♑", "Aquarius ♒", "Pisces ♓"]
    for horoscope, horoscope_1 in zip(horoscopes, horoscopes_1):
        markup.add(InlineKeyboardButton(text=horoscope, callback_data="change_{}".format(horoscope)),
                    InlineKeyboardButton(text=horoscope_1, callback_data="change_{}".format(horoscope_1)))
    return markup

def horoscope_done_troll(horoscope):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(text="You are a " + horoscope + " now!", callback_data="hehe"))
    return markup