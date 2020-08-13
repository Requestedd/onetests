import telebot
from telebot import types
import random
import datetime
import time
import threading 
from time import sleep
import os

token = os.environ.get('bot_token')
ids = os.environ.get('bot_ids')
bot = telebot.TeleBot(token);

###########################

yes0_list = ['Угу','Давай начнём уже','Погнали','В АТАКУ!!!1','Я преисполнен решимостью','Почему бы и нет','Да. Пора.','Уже? Океюшки',"Let's go",'Приступим','Да.']
rand_yes0 = random.choice(yes0_list)
no0_list = ['Спать хочетцо','Ещё пару минут..','Ну мааам..','Как-то не зарядился','Ещё немношко времени','Неть..','Не то не сё что-то','Не уверен я','Пожалуй что нужно досыпать..']
rand_no0 = random.choice(no0_list)

dict = {'S': 'есть'}
def my_timer(print_interval):
	data = threading.local()
	data.counter = 1
	while True:
		time.sleep(print_interval)
		if dict['S'] == 'да' :
			break
		else:
			dict['S'] = 'нет'
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			markup.row(rand_no0 , rand_yes0)
			bot.send_message(ids, "Час прошёл , готов работать?", reply_markup=markup)
			break
#t = threading.Thread(target=my_timer, name="My time thread", args=(3600, ), daemon=True)
#t.start()

###########################

#if call.data == rand and dict['S'] == 'есть':
#		dict['S'] = 'да'

ohayou_list = ['Здавствуй , здравствуй , давай без церемоний , приступим? ', 'Чудесное утро ,чтобы начать , не правда ли? ', 'Сегодня будет ещё один великий день , ты ведь к нему готов?', 
'Вставай!!!!!!!! , работоть нужно! Проснулся? ', 'Времени очень мало , давай уже начнём , готоф? ', 'Охаё Иказаемас , выспался?', 'Мне кажется , мы проспали. Сделаем шаг вперёд?']

error_list = ['На кнопки нажемай!!','Промазал!','Давай по инструкции!','Не туда братик , не туда!','По кнопкам жмякай','Рано тебе ещё диалоги писать','Я не создан для такого','Ты меня ещё не дописал , чтобы так общаться',
'Я могу очень многое , но не всё.','Давай попробуем что-то другое.','МИМО!','У тебя есть ещё попытка.','Попробуй на кнопки понажемать..']

rand = random.choice(ohayou_list)
rand_error = random.choice(error_list)

###

yes0_list = ['Угу','Давай начнём уже','Погнали','В АТАКУ!!!1','Я преисполнен решимостью','Почему бы и нет','Да. Пора.','Уже? Океюшки',"Let's go",'Приступим','Да.']

###

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup1.row(rand_no0 , rand_yes0)
bot.send_message(ids, rand, reply_markup=markup1) # Доброе утро , готов работать? - Нет / Да.

###
# Вопрос на "Я не выспался"
rise1_list = ['Успех не знает слова "потом"! , ты уверен?','Сейчас или Никогда. Силы то в тебе должны быть?','Ну ты чего. Вспомни. О чём ты мечтаешь? Чего хочешь? К чему стремишься? Готов всё это бросить? ',
'А как же 400.000 ? Их за тебя никто не сделает.',
'Ты слабак ? Давай иди добиваться мечты.','Найди в себе силы поднять жопу. Между ней и кроватью деньги не пролетят','Люба была права , ты Нюня. Ничуть не изменился.','Ну Боже , сон или мечта? ','Пока ты спишь , другие люди добиваются своей мечты!',
'Если так и будешь спать , никогда не станешь Свободным!','Я тебя понимаю , но нужно же иногда делать то , что нужно? ','Давай , шаг за шагом. Ты в себя веришь? Встань.','Не может такого быть. И это ты ? Да я не вижу в тебе силы.',
'Всемогущим хотел стать? А даже встать пораньше не можешь..','Встанешь ты наконец или нет? Мечта не ждёт.','Ты ведь хочешь стать Свободным?.. Так Вставай же! Поднимись!']

# Ответы на "хочу спать" и "теперь не хочу"
sleep_yes_list = ['Спать очень хочется..','Я совсем не в фазе...','Я понимаю. НО лучше выспаться..','Прости , нужно выспаться','Я не могу собраться , прости','Да , знаю.. я всё знаю.. но сон тоже важен','Прости.','Очень уж спать хочется..',
'Я дико извиняюсь!','Один разочек..','Ещё пару минут..','Я не забыл о своей мечте. Но часть мечты - это правильный отдых','Да , я почти.. почти готов','Ещё немного времени.. ещё чуть-чуть','Знаю  , знаю , знаю.. но.. не готов','Не могу..']

sleep_no_list = ['Да черт побери , я хочу стать Свободным!','ЛАДНО , УБЕДИЛ , ВСТАЮ!','Хорошо хорошо , встаю','Ты прав. Нужно работать','Каждый день двигает меня к цели. Да , нужно работать','Миллион сегодня - утро завтра.',
'Да. Я ещё молод , можно и не досыпать','ОКЕЙ Я ВСТАЮ','Да я понял тебя , не нужно . Встаю','Подъем подъем.','Я почти как огурчик.','Вскакиваю с кровати.','Понял и осознал , лечу к мечтам.','Хорошо , ты умеешь убеждать.',
'Да , мечта ждёт. Я пойду к ней','Меня запомнят , да?..']

# Час Сна
hour_list = ['Я надеюсь ты одумаешься , даю тебе часик другой','Дам тебе немношко времени!!1','Ну поспи ещё чуть-чуть.','Сегодня тебя пощажу. Давай чуть позже.','Мы ещё встретимся!','У тебя будет ещё немного времени',
'Ну поспи ещё чуток.','Ладно , соберись с силами.','Будет тебе час.','Напиши , если будешь готов','Нюня ты. Досыпай.','Окей окей , назад в койку.','Час значит.. окей.']

one_day = ['С чистки зубов , конечно же.','Зубки чистить начнём.','Стартуем с головы , первым делом - зубы.']
two_day = ['Думаю ,  пора её щетину.','Побреемся же.','Знаешь , усы тебе совсем не идут.','Иди и возьми бритву , сделай хорошее дело.','Бриться , нужно бриться.']

rand_one_day = random.choice(one_day)
rand_two_day = random.choice(two_day)

rand_rise1 = random.choice(rise1_list)
rand_sleep_yes = random.choice(sleep_yes_list)
rand_sleep_no = random.choice(sleep_no_list)
rand_hour = random.choice(hour_list)

###

@bot.message_handler(func=lambda message: rand_yes0 , content_types=['text'])
def process_step(message):
	if message.text == rand_yes0 :                                      # Если Да.
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add('С чего начнём?')
		bot.send_message(ids, "Замечательно , приступим же", reply_markup=markup)
	
	elif message.text == rand_no0:                                      # Если Нет.
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.row(rand_sleep_yes , rand_sleep_no)
		bot.send_message(ids, rand_rise1 , reply_markup=markup)   # Что значит нет? Ты уверен , что хочешь спать? Уверен / Встаю.
		# Кнопки sleep

	elif message.text == rand_sleep_yes :             # Всё равно спать	     
		#t = threading.Thread(target=my_timer, name="My time thread", args=(3600, ), daemon=True)
		#t.start()
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
		markup.add('Я выспался')
		bot.send_message(ids, 'Скажи , если захочешь встать.' , reply_markup=markup) # Поспи Часок

	elif message.text == rand_sleep_no:               # ТЫ прав , встаю
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add(rand_yes0)
		bot.send_message(ids, 'Начнём же?' , reply_markup=markup)       # Так и нужно.

	elif message.text == 'Я выспался' and dict['S'] == 'есть':
		dict['S'] = 'да'
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add(rand_yes0)
		bot.send_message(ids, 'Уверен?' , reply_markup=markup)

	elif message.text == 'С чего начнём?': 
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add('Дело сделано!')
		bot.send_message(ids, rand_one_day + 'Я тебя не отпущу , пока не сделаешь это. Послушай заодно музыку.' , reply_markup=markup)
	
	elif message.text == 'Дело сделано!':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.row('Ну .. есть щетина' , 'Вроде всё хорошо.')
		bot.send_message(ids, 'Дальше потрогай лицо. Скажи честно , бриться нужно?'  , reply_markup=markup)

	elif message.text == 'Ну .. есть щетина': 
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add('Я закончил бриться.')
		bot.send_message(ids, rand_two_day + 'Иди и побрейся. И да , музыку то никто не отменял. Пожалуйста , мы ведь не продолжим , если ты этого не сделаешь.'  , reply_markup=markup)

	elif message.text == 'Вроде всё хорошо.': 
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add('Ну .. есть щетина' , 'Да , я не вру!')
		bot.send_message(ids, ' Ты блин точно в этом уверен? Точно? ТЫ ведь не хочешь просрать день?', reply_markup=markup)

	elif message.text == 'Да , я не вру!':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add('Вперёд к звёздам!')
		bot.send_message(ids, ' Всё всё , верю :) Идём наконец совершать великое?', reply_markup=markup)

	elif message.text == 'Я закончил бриться.':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add('Вперёд к звёздам!')
		bot.send_message(ids, ' Умница! :) Идём наконец совершать великое?', reply_markup=markup)

	elif message.text == 'Вперёд к звёздам!':
		markup.add('Вперёд')
		bot.send_message(ids, ' Идём', reply_markup=markup)

	#else:
		#bot.send_message(ids, random.choice(error_list)  )        # Не те кнопки.

bot.polling(none_stop=True, interval=0)


#listt = ['','','','','','','','','','','','','','','','']
