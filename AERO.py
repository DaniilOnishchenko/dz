# Кейс: Разработка чат бота для навигации пассажира в аэропорту «Краснодар»
 
# 1) Приветствие пассажира, информация о боте. Кнопки для выбора нужного объекта

# -Регистрация
# -Регистрация на стойке самообслуживания
# -Аптека
# -Кафе
# -Бизнес-зал
# -Проход на досмотр
# -Выход из аэропорта

# 2)
# -При выборе коммерческих строк предоставляется лист вариантов (кафе, аптеки и т.д)
# -При выборе бизнес-зала предоставляется возможность построить маршрут 
# -При выборе прочих вариантов предлагается построить маршрут

# 3)
# -При выборе кафе/аптек предоставляется информация о среднем чеке и типе кухни


# 4)
# При окончательном выборе кафе предлагает забронировать столик для этого просит ввести номер телефона и время прихода

import telebot
from telebot import types

TOKEN = '1811415738:AAERwHlquzMu5syFJQKdWzHVhcjzcIKSOGw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def help_def(message):
    bot.send_message(message.from_user.id, "Напиши 'Старт'")

@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 
    if message.text == "Старт": 
        bot.send_message(message.chat.id, "Привет, я бот Аэропорта 'Краснодар'")
        main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        button1 = types.KeyboardButton('Кафе')
        button2 = types.KeyboardButton('Бизнес зал') 
        button3 = types.KeyboardButton('Магазины')
        button4 = types.KeyboardButton('Регистрация')
        button5 = types.KeyboardButton('Саморегистрация')

        main_markup.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, "Выбери нужную кнопку и я помогу тебе.", reply_markup = main_markup)
        bot.register_next_step_handler(message, name)
    elif message.text == "Назад": 
        main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        button1 = types.KeyboardButton('Кафе')
        button2 = types.KeyboardButton('Бизнес зал') 
        button3 = types.KeyboardButton('Магазины')
        button4 = types.KeyboardButton('Регистрация')
        button5 = types.KeyboardButton('Саморегистрация')

        main_markup.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, "Выбери нужную кнопку и я помогу тебе.", reply_markup = main_markup)
        bot.register_next_step_handler(message, name)
    else: 
        bot.send_message(message.chat.id, "Напиши Старт")

def name(message):
    if message.text == 'Кафе':
        main_markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cafe1 = types.KeyboardButton('Борт 17/93')
        cafe2 = types.KeyboardButton('Babooshka') 
        cafe3 = types.KeyboardButton('Шоколадница')
        cafe4 = types.KeyboardButton('Кубань')
        cafe5 = types.KeyboardButton('Craft Store')
        cafe6 = types.KeyboardButton('Назад')

        main_markup1.add(cafe1, cafe2, cafe3, cafe4, cafe5, cafe6)
        bot.send_message(message.chat.id, "Выбери интересующее кафе", reply_markup = main_markup1)
        bot.register_next_step_handler(message, cafe)

    elif message.text == 'Бизнес зал':
        main_markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bz1 = types.KeyboardButton('Услуги')
        bz2 = types.KeyboardButton('Прайс')
        bz3 = types.KeyboardButton('Маршрут')
        bz4 = types.KeyboardButton('Назад')

        main_markup2.add(bz1, bz2, bz3, bz4)
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup = main_markup2)
        bot.register_next_step_handler(message, bz)

    elif message.text == 'Магазины':
        main_markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mk1 = types.KeyboardButton('Моя станица')
        mk2 = types.KeyboardButton('Дары Каспия')
        mk3 = types.KeyboardButton('Аптека')
        mk4 = types.KeyboardButton('TOY')
        mk5 = types.KeyboardButton('Цветы "Клумба')
        mk6 = types.KeyboardButton('Назад')

        main_markup3.add(mk1, mk2, mk3, mk4, mk5, mk6)
        bot.send_message(message.chat.id, "Выбери интересующий магазин?", reply_markup = main_markup3)
        bot.register_next_step_handler(message, mk)

    elif message.text == 'Регистрация':
        main_markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        reg1 = types.KeyboardButton('Aeroflot')
        reg2 = types.KeyboardButton('S7')
        reg3 = types.KeyboardButton('Utair')
        reg4 = types.KeyboardButton('Pobeda')
        reg5 = types.KeyboardButton('Azimut')
        reg6 = types.KeyboardButton('Turkish Airlines')
        reg7 = types.KeyboardButton('Другая')
        reg8 = types.KeyboardButton('Назад')

        main_markup4.add(reg1, reg2, reg3, reg4, reg5, reg6, reg7, reg8)
        bot.send_message(message.chat.id, "Выберите вашу авиакомпанию", reply_markup = main_markup4)
        bot.register_next_step_handler(message, reg)


    elif message.text == 'Саморегистрация':
        main_markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        so1 = types.KeyboardButton('Aeroflot')
        so2 = types.KeyboardButton('S7')
        so3 = types.KeyboardButton('Другая')
        so4 = types.KeyboardButton('Назад')

        main_markup5.add(so1, so2, so3, so4)
        bot.send_message(message.chat.id, "Выберите вашу авиакомпанию", reply_markup = main_markup5)
        bot.register_next_step_handler(message, so)
    else: 
        bot.send_message(message.chat.id, "Напиши Привет")   



#Второй уровень меню

def cafe(message):
    if message.text == 'Борт 17/93':
        bot.send_message(message.chat.id, "Кафе «Борт 17/93» предлагает посетителям легкие закуски, сэндвичи, бургеры, круглосуточные завтраки, десерты, а также большой выбор напитков: кофе, чай, лимонады, смузи. Мы собрали коллекцию пива высшего качества зарубежных сортов, большой ассортимент вина Кубанских виноделен. \nЗал ожидания вылета внутренних линий, 1 этаж. \nСредний чек: 540 руб. \nТелефон +7 (989) 198-32-54")
    elif message.text == 'Babooshka':
        bot.send_message(message.chat.id, "Домашние завтраки и обеды по приятным ценам. Всегда в меню супы, салаты, холодные и горячие закуски, мороженное, десерты и свежая выпечка, а также напитки: морсы, соки, чай, кофе, вино и шампанское. \nЗал прилета внутренних линий, 1 этаж. \nСредний чек: 320 руб. \nТелефон +7 (918) 918-77-88")
    elif message.text == 'Шоколадница':
        bot.send_message(message.chat.id, "Кофейня «Шоколадница» предлагает широкий ассортимент напитков, закусок, горячих блюд, которые не только радуют глаз своим внешним видом, но и изобилием вкусов. Здесь вы сможете приятно провести время за чашкой ароматного кофе и попробовать наши фирменные десерты, взять полноценный горячий обед или быстро перекусить по пути на самолет. Быстрое и качественное обслуживание, уютная атмосфера, самые качественные продукты — наш приоритет. \nТерминал1 (внутренние линии), Общая зона, 1 этаж. \nСредний чек: 750 руб. \nТелефон +7 (988) 369-76-29")
    elif message.text == 'Кубань':
        bot.send_message(message.chat.id, "Кафе Кубань предлагает своим гостям лучшие блюда кубанской кухни по классическим рецептам. Попробуйте традиционные супы, салаты и закуски, свежую выпечку, компоты и лимонады собственного производства, чай, кофе и сэндвичи. \nТерминал1 (внутренние линии), Общая зона, 1 этаж. \nСредний чек: 450 руб. \nТелефон +7 (989) 276-60-09")
    elif message.text == 'Craft Store':
        bot.send_message(message.chat.id, "Craft Store|Wine bar — это совершенно новая концепция, новое слово в сегменте «эко, био, фрэш» продукции. Попробуйте эксклюзивные сорта крафтового пива из лучших пивоварен России, мясные деликатесы, широкий ассортимент местных сыров, произведенных на частных эко-фермах. Также в ассортименте Craft представлены орехи, сухофрукты, специи, чай, масла, а также мед и джем — яркий вкус природы. \nТерминал 1 (внутренние линии), Cтерильная зона \nСредний чек: 780  руб. \nТелефон +7 (952) 814-88-94")
    elif message.text == 'Babooshka':
        bot.send_message(message.chat.id, "Зал прилета внутренних линий, 1 этаж. \nСредний чек: 320 руб. \nТелефон +7 (918) 918-77-88")
    elif message.text == 'Назад':
    	get_text_messages(message)
    else: 
        bot.send_message(message.chat.id, "Напиши Привет")
def bz(message):
    if message.text == 'Услуги':
        bot.send_message(message.chat.id, "пользование баром; \nвизуальная информация о вылетающих рейсах; \nиндивидуальное приглашение пассажиров к выходу на посадку; доставка на борт ВС отдельным транспортом; \nвозможность просмотра каналов спутникового телевидения; \nдоступ к Wi-Fi; \nпериодические печатные издания различной тематики; \nдетская игровая зона;")
    elif message.text == 'Прайс':
        bot.send_message(message.chat.id, "Обслуживание одного пассажира – 4 000 рублей. \nДети от 2-х до 12 лет – 50% от тарифа. \nДети от 2-х до 12 лет – 50% от тарифа.")
    elif message.text == 'Маршрут':
        bot.send_message(message.chat.id, "2 этаж, правое крыло, \nТелефон: +7 (861) 219-19-88")
    else: 
        bot.send_message(message.chat.id, "Напиши Привет")
def mk(message):
    if message.text == 'Моя станица':
        bot.send_message(message.chat.id, "Фирменный магазин «Моя Станица» предлагает покупателям 100 % натуральные продукты родной Кубани. Под брендом «Моя Станица» выпускаются охлажденные мясные изделия, свежие колбасы и молочная продукция с уникальной формулой А2 — легко усваивается и усиливает защитные функции организма. Порадуйте натуральными деликатесами «Моя Станица» себя и близких! \nЗал ожидания вылета внутренних линий, 1 этаж. \nТелефон +7 (918) 971-73-42")
    elif message.text == 'Дары Каспия':
        bot.send_message(message.chat.id, "Астраханские деликатесы, икра черная, красная, щучья, а также балык горячего и холодного копчения. Рыба вяленая, консервы и пресервы из рыбы. Всегда свежая и вкусная продукция. \nОбщая зона терминала внутренних линий, 1 этаж. \nТелефон +7 (937) 128-66-21")
    elif message.text == 'Аптека':
        bot.send_message(message.chat.id, "В аптеке Лаки Фарма Вы найдете необходимые медикаменты и средства гигиены, чтобы Ваше путешествие всегда было комфортным. \nОбщая зона терминала внутренних линий, 1 этаж. \nТелефон +7 (918) 201-22-22")
    elif message.text == 'TOY':
        bot.send_message(message.chat.id, "В детском магазине Toy вы с легкостью найдете то, чем порадовать ребенка, ведь здесь представлены развивающие игры и игрушки для разных возрастных групп. \nЗал ожидания вылета внутренних линий, 1 этаж. \nТелефон +7 (918) 918-77-88")
    elif message.text == 'Цветы "Клумба':
        bot.send_message(message.chat.id, "Цветы и букеты на любой вкус, а также опытный флорист соберёт букет по Вашему желанию быстро и качественно, проконсультирует как сохранить красоту и свежесть букета или цветка как можно дольше. Каждому покупателю внимательное отношение и хорошее настроение обеспечено! \nПривокзальная площадь. \nТелефон +7 (918) 696-07-76")
    elif message.text == 'Назад':
    	get_text_messages(message)
    else: 
        bot.send_message(message.chat.id, "Напиши Привет")
def reg(message):
    if message.text == 'Aeroflot':
        bot.send_message(message.chat.id, "Пожалуйста, наденьте маску, перчатки и подготовьте паспорт. \nПодходите на стойки регистриции 1-3")
    elif message.text == 'S7':
        bot.send_message(message.chat.id, "Пожалуйста, наденьте маску, перчатки и подготовьте паспорт. \nПодходите на стойки регистриции 4-6")
    elif message.text == 'Utair':
        bot.send_message(message.chat.id, "Пожалуйста, наденьте маску, перчатки и подготовьте паспорт. \nПодходите на стойки регистриции 7-9")
    elif message.text == 'Pobeda':
        bot.send_message(message.chat.id, "Пожалуйста, наденьте маску, перчатки и подготовьте паспорт. \nПодходите на стойки регистриции 10-12")
    if message.text == 'Azimut':
        bot.send_message(message.chat.id, "Пожалуйста, наденьте маску, перчатки и подготовьте паспорт. \nПодходите на стойки регистриции 13-15")
    elif message.text == 'Turkish Airlines':
        bot.send_message(message.chat.id, "Пожалуйста, наденьте маску, перчатки и подготовьте паспорт. \nПодходите на стойки регистриции 16-18")
    elif message.text == 'Другая':
        bot.send_message(message.chat.id, "Пожалуйста, наденьте маску, перчатки и подготовьте паспорт. \nПодходите на стойки регистриции 19-21")
    elif message.text == 'Назад':
    	get_text_messages(message)
    else: 
        bot.send_message(message.chat.id, "Напиши Привет")
def so(message):
    if message.text == 'Aeroflot':
        bot.send_message(message.chat.id, "Стойка для печати посадочного билета компании 'Aeroflot' находится возле стойки №1")
    elif message.text == 'S7':
        bot.send_message(message.chat.id, "Стойка для печати посадочного билета компании 'S7' находится возле стойки №5")
    elif message.text == 'Другая':
        bot.send_message(message.chat.id, "Стойка для печати посадочного билета находится возле стойки №21")   
    elif message.text == 'Назад':
    	get_text_messages(message)
    else: 
        bot.send_message(message.chat.id, "Напиши Привет")

bot.polling()












