import telebot
from config import API_TOKEN
import os
import random
images = (os.listdir('images'))

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я экобот вот, что я умею: \n"
    "/reminder - памятка \n"
    "/mem - мемы \n"
    "/links - каналы \n") 

@bot.message_handler(commands=['links'])
def links(message):
    bot.send_message(message.chat.id, "Выберите:"
    "/channels - каналы, которые вам помогут \n"
    "/groups - группы, которые помогут вам \n")

@bot.message_handler(commands=['channels'])
def channels(message):
    bot.send_message(message.chat.id, "Вот всё, что удалось нам найти:"
    "https://t.me/ecomisli \n"
    "https://t.me/ecodays \n"
    "https://t.me/ekologiya_rf \n"
    "https://t.me/earthtouches_me \n"
    "https://t.me/control_klimat \n")

@bot.message_handler(commands=['groups'])
def groups(message):
    bot.send_message(message.chat.id, "Вот всё, что удалось нам найти:"
    "cvcvcv \n")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    random_images = random.choice(images)
    with open(f'images/{random_images}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['reminder'])
def reminder(message):
    bot.send_message(message.chat.id, "/reglobal_warming - Глобальное потепление \n" 
    "/Reduction_of_forest_area - Уменьшение площади лесов \n"
    "/Environmental_pollution - Загрязнение окружающей среды \n")

@bot.message_handler(commands=['reglobal_warming'])
def global_warming(message):
    bot.send_message(message.chat.id, "Глобальное потепление \n" 
    "\n"
    "В попытке сдерживать глобальное потепление многие государства ставят перед собой цели по сокращению выбросов углекислого газа. Текущие обязательства стран, в попытке сдерживать глобальное потепление, предусматривают сокращение цифры выбросов до 55 миллиардов тонн. Чтобы потепление оставалось в пределах 1,5 градуса, выбросы должны быть снижены до 33 миллиардов тонн к 2030 году. Чтобы двигаться в сторону этой цифры, нужны фундаментальные изменения в укладе общества: придется сокращать использование ископаемого топлива и переходить на чистые источники энергии, нужно сокращать вырубку лесов и использовать экологичные методы выращивания сельхозкультур. \n")

@bot.message_handler(commands=['Reduction_of_forest_area'])
def Reduction_of_forest_area(message):
    bot.send_message(message.chat.id, "Уменьшение площади лесов \n" 
    "\n"
    "Эксперты полагают, что сократить темпы уменьшения площади лесов на Земле можно, используя методы устойчивого ведения сельского хозяйства и новые технологии, которые не требуют больших площадей для выращивания культур. Также важно заниматься лесовосстановлением и давать пострадавшим от рубок или стихийных бедствий лесным экосистемам «приходить в себя». \n")

@bot.message_handler(commands=['Environmental_pollution'])
def Environmental_pollution(message):
    bot.send_message(message.chat.id, "Загрязнение окружающей среды \n" 
    "\n"
    "Остановить темпы загрязнения окружающей среды можно повсеместным внедрением переработки отходов и повторным использованием стекла, алюминия и пластика. Также страны на законодательном уровне ограничивают объемы и виды химических веществ, которые разрешено использовать в промышленности, и устанавливают штрафы за чрезмерные выбросы. \n" 
    "\n" 
    "Экологические проблемы современности требуют срочных и комплексных мер для их решения. Переход к экологически устойчивым технологиям, уменьшение потребления ресурсов и повышение экологического сознания — все это ключевые составляющие борьбы за чистую планету. Сотрудничество государств, научных сообществ, бизнеса и обычных граждан необходимо для достижения этой цели. Нам необходимо действовать сейчас, чтобы обеспечить устойчивое будущее для нашей планеты и будущих поколений. \n")

bot.infinity_polling()
