import telebot
import cfg


def start():
    bot = telebot.TeleBot(cfg.TOKEN, parse_mode=None)
    photo = open('./image/cam.png', 'rb')
    bot.send_photo(chat_id=cfg.ID, photo=photo)


