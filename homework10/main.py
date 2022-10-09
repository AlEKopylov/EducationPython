import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

reply_keyboard = [['/play', '/rules'],
                  ['/exit']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5461645927:AAHEK7YaRm8ws6qp1pbarSRSLYr8DzcCm80'

candy = 0


def start(update, context):
    update.message.reply_text(
        "Привет давай поиграем!\n play - начать игру\n rules - правила игры\n exit - выход",
        reply_markup=markup
    )


def play(update, context):
    update.message.reply_text('Введите количество конфет: ')
    return 1


def stop(update, context):
    update.message.reply_text("")
    return ConversationHandler.END


def get_candy(update, context):
    global candy
    try:
        candy = int(update.message.text)
        update.message.reply_text(
            f"В игре {candy} конфет. Вы ходите первым, сколько конфет Вы возьмете?"
        )
    except ValueError:
        logging.warning('Ошибка: неверный тип данных')
        update.message.reply_text("Введите число больше 28")
        return 1
    return 2


def user_hod(update, context):
    global candy
    val = 1
    print(candy)
    if candy > 0:
        new_candy = int(update.message.text)
        if new_candy >= 1 and new_candy <= 28:
            candy -= new_candy
            if candy <= 0:
                update.message.reply_text("Выиграл Игрок!\nmade by AEKopy", reply_markup=markup)
                return ConversationHandler.END
            bot_candy = candy%29
            if bot_candy == 0: bot_candy = 1
            candy -= bot_candy
            update.message.reply_text(f"Бот взял {bot_candy}")
            if candy <= 0:
                update.message.reply_text("Выиграл БОТ!\nmade by AEKopy", reply_markup=markup)
                return ConversationHandler.END
            update.message.reply_text(f"Конфет осталось {candy}\nВведите число от 1 до 28 - {val}")
        else:
            update.message.reply_text("Неверный ввод!\nВведите число от 1 до 28")
    return 2


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def rules(update, context):
    update.message.reply_text(
        "Вы играете против непобедимого БОТа.\nПервый ход будет за Вами.\nВыберите количество конфет в игре.\nКаждый ход Вы сможете забрать не более чем 28 конфет.\nПобедит тот, кто заберет последнюю конфету. \n\n Удачи!")


def exit(update, context):
    update.message.reply_text(
        "Удачи!")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    play_handler = ConversationHandler(

        entry_points=[CommandHandler('play', play)],

        states={
            1: [MessageHandler(Filters.text & ~Filters.command, get_candy)],

            2: [MessageHandler(Filters.text & ~Filters.command, user_hod)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("exit", exit))
    
    dp.add_handler(play_handler)
    
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()