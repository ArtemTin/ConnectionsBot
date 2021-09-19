from typing import List

metro_lines = {
    "1": ("Сокольническая линия", "Красная"),
    "2": ("Замоскворецкая линия", "Тёмно-зелёная"),
    "3": ("Арбатско-Покровская линия", "Синяя"),
    "4": ("Филёвская линия", "Голубая"),
    "4A": ("Филёвская линия(м)", "Голубая"),
    "5": ("Кольцевая линия", "Коричневая"),
    "6": ("Калужско-Рижская линия", "Оранжевая"),
    "7": ("Таганско-Краснопресненская линия", "Фиолетовая"),
    "8": ("Калининская линия", "Жёлтая"),
    "9": ("Серпуховско-Тимирязевская линия", "Серая"),
    "10": ("Люблинско-Дмитровская линия", "Салатовая"),
    "11": ("Большая кольцевая линия", "Бирюзовая"),
    "12": ("Бутовская линия", "Серо-голубая"),
    "14": ("Московское центральное кольцо", "Бежевая"),
    "15": ("Некрасовская линия", "Розовая"),
    "D1": ("Первый диаметр", "Светло-розовая"),
    "D2": ("Второй диаметр", "Светло-жёлтая"),
    "8A": ("Солнцевская линия", "Жёлтая")}

# Нету Народного ополчения мневники тпк
lines_stations = {
    "1": ("Коммунарка", "Ольховая", "Прокшино", "Филатов Луг", "Саларьево", "Румянцево", "Тропарёво", "Юго-Западная",
          "Проспект Вернадского", "Университет", "Воробьёвы горы", "Спортивная", "Фрунзенская", "Парк культуры",
          "Кропоткинская", "Библиотека имени Ленина", "Охотный ряд", "Лубянка", "Чистые пруды", "Красные Ворота",
          "Комсомольская", "Красносельская", "Сокольники", "Преображенская площадь", "Черкизовская",
          "Бульвар Рокоссовского"),
    "2": ("Алма-Атинская", "Красногвардейская", "Домодедовская", "Орехово", "Царицыно", "Кантемировская", "Каширская",
          "Коломенская", "Технопарк", "Автозаводская", "Павелецкая", "Новокузнецкая", "Театральная", "Тверская",
          "Маяковская", "Белорусская", "Динамо", "Аэропорт", "Сокол", "Войковская", "Водный стадион", "Речной вокзал",
          "Беломорская", "Ховрино"),
    "3": ("Щёлковская", "Первомайская", "Измайловская", "Партизанская", "Семёновская", "Электрозаводская", "Бауманская",
          "Курская", "Площадь Революции", "Арбатская", "Смоленская", "Киевская", "Парк Победы", "Славянский бульвар",
          "Кунцевская", "Молодёжная", "Крылатское", "Строгино", "Мякинино", "Волоколамская", "Митино",
          "Пятницкое шоссе"),
    "4": ("Александровский сад", "Арбатская", "Смоленская", "Киевская", "Студенческая", "Кутузовская", "Фили",
          "Багратионовская", "Филёвский парк", "Пионерская", "Кунцевская"),
    "4A": ("Александровский сад", "Арбатская", "Смоленская","Киевская", "Выставочная", "Международная"),
    "5": ("Курская", "Комсомольская", "Проспект Мира", "Новослободская", "Белорусская", "Краснопресненская", "Киевская",
          "Парк культуры", "Октябрьская", "Добрынинская", "Павелецкая", "Таганская"),
    "6": (
        "Новоясеневская", "Ясенево", "Тёплый Стан", "Коньково", "Беляево", "Калужская", "Новые Черёмушки",
        "Профсоюзная",
        "Академическая", "Ленинский проспект", "Шаболовская", "Октябрьская", "Третьяковская", "Китай-город",
        "Тургеневская",
        "Сухаревская", "Проспект Мира", "Рижская", "Алексеевская", "ВДНХ", "Ботанический сад", "Свиблово",
        "Бабушкинская",
        "Медведково"),
    "7": ("Котельники", "Жулебино", "Косино", "Лермонтовский проспект", "Выхино", "Рязанский проспект", "Кузьминки",
          "Текстильщики", "Волгоградский проспект", "Таганская", "Китай-город", "Лубянка", "Кузнецкий Мост",
          "Пушкинская", "Баррикадная", "Улица 1905 года", "Полежаевская", "Октябрьское Поле", "Щукинская", "Спартак",
          "Тушинская", "Сходненская", "Планерная"),
    "8": ("Новокосино", "Новогиреево", "Перово", "Шоссе Энтузиастов", "Авиамоторная", "Площадь Ильича", "Марксистская",
          "Третьяковская"),
    "9": ("Бульвар Дмитрия Донского", "Аннино", "Улица Академика Янгеля", "Пражская", "Южная", "Чертановская",
          "Севастопольская", "Нахимовский проспект", "Нагорная", "Нагатинская", "Тульская", "Серпуховская", "Полянка",
          "Боровицкая", "Чеховская", "Цветной бульвар", "Менделеевская", "Савёловская", "Дмитровская", "Тимирязевская",
          "Петровско-Разумовская", "Владыкино", "Отрадное", "Бибирево", "Алтуфьево"),
    "10": ("Зябликово", "Шипиловская", "Борисово", "Марьино", "Братиславская", "Люблино", "Волжская", "Печатники",
           "Кожуховская", "Дубровка", "Крестьянская Застава", "Римская", "Чкаловская", "Сретенский бульвар", "Трубная",
           "Достоевская", "Марьина Роща", "Бутырская", "Фонвизинская", "Петровско-Разумовская", "Окружная",
           "Верхние Лихоборы", "Селигерская"),
    "11": ("Савёловская", "Петровский парк", "ЦСКА", "Хорошёвская", "Шелепиха", "Деловой центр"),
    "12": (
        "Бунинская Аллея", "Улица Горчакова", "Бульвар Адмирала Ушакова", "Улица Скобелевская",
        "Улица Старокачаловская",
        "Лесопарковая", "Битцевский парк"),
    "14": ("Андроновка", "Шоссе Энтузиастов", "Соколиная Гора", "Измайлово", "Локомотив", "Бульвар Рокоссовского",
           "Белокаменная", "Ростокино", "Ботанический сад", "Владыкино", "Окружная", "Лихоборы", "Коптево",
           "Балтийская", "Стрешнево", "Панфиловская", "Зорге", "Хорошёво", "Шелепиха", "Деловой центр", "Кутузовская",
           "Лужники", "Площадь Гагарина", "Крымская", "Верхние Котлы", "ЗИЛ", "Автозаводская", "Дубровка", "Угрешская",
           "Новохохловская", "Нижегородская"),
    "15": ("Некрасовкая", "Лухмановская", "Улица Дмитриевского", "Косино", "Юго-Восточная", "Окская", "Стахановская",
           "Нижегородская", "Авиамоторная", "Лефортово", "Электрозаводская"),
    "D1": (
        "Одинцово", "Баковка", "Сколково", "Немчиновка", "Сетунь", "Рабочий Посёлок", "Кунцевская",
        "Славянский бульвар",
        "Фили", "Тестовская", "Беговая", "Белорусская", "Савёловская", "Тимирязевская", "Окружная", "Дегунино",
        "Бескудниково", "Лианозово", "Марк", "Новодачная", "Долгопрудная", "Водники", "Хлебниково", "Шереметьевская",
        "Лобня"),
    "D2": (
        "Подольск", "Силикатная", "Остафьево", "Щербинка", "Бутово", "Битца", "Красный Строитель", "Покровское",
        "Царицыно",
        "Москворечье", "Курьяново", "Перерва", "Депо", "Люблино", "Текстильщики", "Новохохловская", "Калитники",
        "Москва-Товарная", "Курская", "Каланчёвская", "Рижская", "Дмитровская", "Гражданская", "Красный Балтиец",
        "Стрешнево", "Щукинская", "Спартак", "Трикотажная", "Волоколамская", "Пенягино", "Павшино", "Красногорская",
        "Опалиха", "Аникеевка", "Нахабино"),
    "8A": (
        "Рассказовка", "Новопеределкино", "Боровское шоссе", "Солнцево", "Говорово", "Озёрная", "Мичуринский проспект",
        "Раменки", "Ломоносовский проспект", "Минская", "Парк Победы", "Деловой центр")
}

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    PicklePersistence,
    ConversationHandler,
    CallbackContext,
)
import tinydb

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

CHOOSING_DAY, CHOOSING_STATIONS_START, CHOOSING_STATIONS_MIDDLE, CHOOSING_LINE, CHOOSING_TIME, CONFIRMING, DELETING, DELETING_CONFIRMED, STARTINGSEARCH, SHOWING_OFF, SELECTINGOP1, SELECTINGOP2, SELECTINGOP3, SELECTINGOP4, DELETING_DAY, SETTINGS_MENU, LEVEL_SELECTING, DELETING_PREF, USER_LEVEL_SELECT, USER_OP_SELECT = range(
    20)
# клавиатура выбора пары
reply_keyboard_time = [
    ["Первая (9:30)", "Вторая (11:10)"],
    ["Третья (13:00)", "Четвёртая (14:40)"],
    ["Пятая (16:20)", "Шестая (18:10)"],
]
markup_picking_time = ReplyKeyboardMarkup(reply_keyboard_time, one_time_keyboard=True)
# клавиатура выбора дня

# клавиатура при выборе станции (уже есть станции)
reply_keyboard_picking = [
    ['Отменить ввод', 'Завершить ввод']
]
markup_picking = ReplyKeyboardMarkup(reply_keyboard_picking, one_time_keyboard=True)

reply_keyboard_startpicking = [
    ['Отменить ввод']
]
markup_startpicking = ReplyKeyboardMarkup(reply_keyboard_startpicking, one_time_keyboard=True)


def choosing_day(update: Update, context: CallbackContext) -> int:
    """Начало общения, приглашение к вводу дня/кнопки управления"""
    context.user_data['day'] = ""
    context.user_data['tmp_station'] = ""

    reply_keyboard_main: list[list[str]] = [
        ['Понедельник', 'Вторник', 'Среда'],
        ['Четверг', 'Пятница', 'Суббота'],
        ['Показать расписание и начать поиск людей', 'Удалить расписание, прекратить поиск', "Настроить предпочтения"],
    ]
    markup_main = ReplyKeyboardMarkup(reply_keyboard_main, one_time_keyboard=True)
    update.message.reply_text(
        f"Привет! Я бот от Таси и я помогу тебе найти попутчиков в метро!\n"
        f"Для этого ты должен(-а) рассказать мне свое расписание и маршрут\n"
        f"Выбери день, который заполнишь",

        reply_markup=markup_main,
    )

    return CHOOSING_DAY


def settings_main(update: Update, context: CallbackContext) -> int:
    """Меню настроек предпочтений"""
    update.message.reply_text(
        f'Тут ты можешь настроить, каких людей мы будем тебе предлагать\n Ты можешь выбрать курс и образовательную программу. Выбрать можно несколько пунктов.\nЕсли ничего не выбрано, мы показываем всех людей, подходящих по маршруту',
        reply_markup=ReplyKeyboardMarkup(
            [["В главное меню", "Предпочитаемые курсы", "Предпочитаемые ОП", "Удалить предпочтения"]],
            one_time_keyboard=True)
    )

    return SETTINGS_MENU

def user_level_select(update: Update, context: CallbackContext) -> int:
    """Меню выбора курса пользователя"""

def user_op_select(update: Update, context: CallbackContext) -> int:
    """Меню выбора ОП пользователя"""

def choosing_stations_start(update: Update, context: CallbackContext) -> int:
    """Узнали день и спрашиваем первую станцию"""
    choosen_day = update.message.text
    context.user_data['day'] = choosen_day
    context.user_data[choosen_day] = []
    context.user_data[choosen_day + "_time"] = ""

    update.message.reply_text(
        f'Введи первую станцию\n'
        f'Заполняем маршрут на {choosen_day.lower()}',
        reply_markup=markup_startpicking,
    )

    return CHOOSING_STATIONS_START


def choosing_stations_middle(update: Update, context: CallbackContext) -> int:
    """Спрашиваем конечную станцию на этой линии (может быть конечной в целом)"""
    choosen_line = update.message.text
    now_day = context.user_data['day']
    if len(context.user_data[now_day]) > 0:
        last_station = context.user_data[now_day][len(context.user_data[now_day]) - 1]

        last_st_tmp = last_station.split()

        last_st_line = last_st_tmp[len(last_st_tmp) - 1]
        last_st_name = ""
        for i in range(len(last_st_tmp) - 1):
            if i == 0:
                last_st_name = last_st_tmp[0]
            else:
                last_st_name = last_st_name + " " + last_st_tmp[i]
        # context.user_data[now_day].append(context.user_data["tmp_station"] + " " + choosen_line)
        if choosen_line == last_st_line:
            line_list = lines_stations[last_st_line]
            last_st_index = line_list.index(last_st_name)
            next_st_index = line_list.index(context.user_data["tmp_station"])
            if next_st_index > last_st_index:
                for i in range(last_st_index + 1, next_st_index + 1):
                    tmp_res = line_list[i] + " " + choosen_line
                    context.user_data[now_day].append(tmp_res)
            else:
                for i in range(last_st_index - 1, next_st_index - 1, -1):
                    tmp_res = line_list[i] + " " + choosen_line
                    context.user_data[now_day].append(tmp_res)
        else:
            res = context.user_data["tmp_station"] + " " + choosen_line
            context.user_data[now_day].append(res)
    else:
        res = context.user_data["tmp_station"] + " " + choosen_line
        context.user_data[now_day].append(res)

    now_route = context.user_data[now_day]
    update.message.reply_text(
        f'Введи следующую станцию или закончи ввод кнопкой\nЗаполняем маршрут на {now_day.lower()}\nТвой текущий маршрут: {now_route}',
        reply_markup=markup_picking,
    )

    return CHOOSING_STATIONS_MIDDLE


def choosing_line(update: Update, context: CallbackContext) -> int:
    """узнали станцию и спрашиваем линию выбранной станции"""
    choosen_station = update.message.text
    context.user_data['tmp_station'] = choosen_station
    now_day = context.user_data['day']
    if len(context.user_data[now_day]) > 0:
        last_station = context.user_data[now_day][len(context.user_data[now_day]) - 1]

        last_st_tmp = last_station.split()

        last_st_line = last_st_tmp[len(last_st_tmp) - 1]
        last_st_name = ""
        for i in range(len(last_st_tmp) - 1):
            if i == 0:
                last_st_name = last_st_tmp[0]
            else:
                last_st_name = last_st_name + " " + last_st_tmp[i]

    possible_lines = []
    for k in lines_stations.keys():
        if choosen_station in lines_stations[k]:
            possible_lines.append(k)

    reply_keyboard_line = [
        possible_lines
    ]
    markup_line = ReplyKeyboardMarkup(reply_keyboard_line, one_time_keyboard=True)

    update.message.reply_text(
        f'Выбери линию, на которой находится станция {choosen_station} ',
        reply_markup=markup_line,
    )

    return CHOOSING_LINE


def choosing_time(update: Update, context: CallbackContext) -> int:
    """Узнали весь маршрут и узнаем номер пары"""
    now_day = context.user_data['day']
    update.message.reply_text(
        f'Выбери номер пары (кнопкой), к которой ты приезжаешь в {now_day.lower()}',
        reply_markup=markup_picking_time,
    )

    return CHOOSING_TIME


def ending_entering(update: Update, context: CallbackContext) -> int:
    """Сохраняем время и показываем итоговый маршрут"""
    choosen_time = update.message.text
    now_day = context.user_data['day']
    context.user_data[now_day + "_time"] = choosen_time

    update.message.reply_text(
        f'Твой путь: {context.user_data[now_day]}\nТы едешь к {choosen_time}\nЗаполняли на {now_day}',
        reply_markup=ReplyKeyboardMarkup([["OK", "Удалить расписание на этот день"]], one_time_keyboard=True)
    )

    return CONFIRMING


def deleting_day(update: Update, context: CallbackContext) -> int:
    """Сброс дня, после ввода"""
    now_day = context.user_data['day']
    del context.user_data[now_day]
    del context.user_data[now_day + "_time"]
    update.message.reply_text(
        f'Расписание на {now_day} удалено',
        reply_markup=ReplyKeyboardMarkup([["OK"]], one_time_keyboard=True)
    )
    return DELETING_DAY


def show_everything(update: Update, context: CallbackContext) -> int:
    """Показать все расписания"""
    update.message.reply_text(
        f'{context.user_data}',
        reply_markup=ReplyKeyboardMarkup([["Начать поиск"], ["В главное меню"]], one_time_keyboard=True)
    )

    return SHOWING_OFF


def delete(update: Update, context: CallbackContext) -> int:
    """Удаляет всё расписание (подтверждение)"""
    update.message.reply_text(
        f'Точно удалить всё расписание?',
        reply_markup=ReplyKeyboardMarkup([["ДА", "НЕТ"]], one_time_keyboard=True)
    )

    return DELETING


def delete_compl(update: Update, context: CallbackContext) -> int:
    """Реальное удаление всех данных"""
    context.user_data["Понедельник"] = []
    context.user_data["Вторник"] = []
    context.user_data["Среда"] = []
    context.user_data["Четверг"] = []
    context.user_data["Пятница"] = []
    context.user_data["Суббота"] = []
    context.user_data["Понедельник_time"] = ""
    context.user_data["Вторник_time"] = ""
    context.user_data["Среда_time"] = ""
    context.user_data["Четверг_time"] = ""
    context.user_data["Пятница_time"] = ""
    context.user_data["Суббота_time"] = ""
    del context.user_data["Понедельник"]
    del context.user_data["Вторник"]
    del context.user_data["Среда"]
    del context.user_data["Четверг"]
    del context.user_data["Пятница"]
    del context.user_data["Суббота"]
    del context.user_data["Понедельник_time"]
    del context.user_data["Вторник_time"]
    del context.user_data["Среда_time"]
    del context.user_data["Четверг_time"]
    del context.user_data["Пятница_time"]
    del context.user_data["Суббота_time"]
    update.message.reply_text(
        f'Ваше расписание удалено, поиск остановлен',
        reply_markup=ReplyKeyboardMarkup([["OK"]], one_time_keyboard=True)
    )

    return DELETING_CONFIRMED


def start_search(update: Update, context: CallbackContext) -> int:
    """Начинает поиск по данным"""
    update.message.reply_text(
        f'Мы начали искать тебе попутчиков!',
        reply_markup=ReplyKeyboardMarkup([["OK"]], one_time_keyboard=True)
    )

    return STARTINGSEARCH


def selectOP1(update: Update, context: CallbackContext) -> int:
    """Выбор ОП, 1 страница"""
    keyboard_1 = [
        ["Античность", "Бизнес-информатика", "Востоковедение", "Восток-ие и африканистика"],
        ["География глобальных изменений", "Городское планирование", "Государственное управление"],
        ["Завершить выбор ОП", "Следующая страница"]
    ]
    update.message.reply_text(
        f'Выбери свою образовательную программу (лист 1/4)',
        reply_markup=ReplyKeyboardMarkup(keyboard_1, one_time_keyboard=True)

    )
    return SELECTINGOP1

def selectOP2(update: Update, context: CallbackContext) -> int:
    """Выбор ОП, 2 страница"""
    keyboard_2 = [
        ["Античность", "Бизнес-информатика", "Востоковедение", "Восток-ие и африканистика"],
        ["География глобальных изменений", "Городское планирование", "Государственное управление"],
        ["Завершить выбор ОП", "Предыдущая страница", "Следующая страница"]
    ]
    update.message.reply_text(
        f'Выбери свою образовательную программу (лист 2/4)',
        reply_markup=ReplyKeyboardMarkup(keyboard_2, one_time_keyboard=True)

    )
    return SELECTINGOP2

def selectOP3(update: Update, context: CallbackContext) -> int:
    """Выбор ОП, 3 страница"""
    keyboard_3 = [
        ["Античность", "Бизнес-информатика", "Востоковедение", "Восток-ие и африканистика"],
        ["География глобальных изменений", "Городское планирование", "Государственное управление"],
        ["Завершить выбор ОП", "Следующая страница"]
    ]
    update.message.reply_text(
        f'Выбери свою образовательную программу (лист 3/4)',
        reply_markup=ReplyKeyboardMarkup(keyboard_3, one_time_keyboard=True)

    )
    return SELECTINGOP3

def selectOP4(update: Update, context: CallbackContext) -> int:
    """Выбор ОП, 4 страница"""
    keyboard_4 = [
        ["Античность", "Бизнес-информатика", "Востоковедение", "Восток-ие и африканистика"],
        ["География глобальных изменений", "Городское планирование", "Государственное управление"],
        ["Завершить выбор ОП", "Следующая страница"]
    ]
    update.message.reply_text(
        f'Выбери свою образовательную программу (лист 4/4)',
        reply_markup=ReplyKeyboardMarkup(keyboard_4, one_time_keyboard=True)

    )
    return SELECTINGOP4

def level_choosing(update: Update, context: CallbackContext) -> int:
    return LEVEL_SELECTING


def delete_pref(update: Update, context: CallbackContext) -> int:
    return DELETING_PREF


# CHOOSING_DAY, CHOOSING_STATIONS_START, CHOOSING_STATIONS_MIDDLE, CHOOSING_LINE, CHOOSING_TIME, CONFIRMING, WAITING_FOR_PEOPLE, IN_OPTIONS = range(7)

def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    persistence = PicklePersistence(filename='convers')

    updater = Updater("1938346821:AAHXQUVOpcgZF1SQ90JnBVXPZilNEySl_y8", persistence=persistence)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', choosing_day)],
        states={
            CHOOSING_DAY: [

                MessageHandler(Filters.regex('^Удалить расписание, прекратить поиск$'), delete),
                MessageHandler(Filters.regex('^Показать расписание и начать поиск людей$'), show_everything),
                MessageHandler(Filters.regex('^Настроить предпочтения$'), settings_main),
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex(
                        '^Удалить расписание, прекратить поиск$') | Filters.regex(
                        '^Показать расписание и начать поиск людей$')), choosing_stations_start)
            ],
            CHOOSING_STATIONS_START: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Отменить ввод$')), choosing_line
                ),
                MessageHandler(Filters.regex('^Отменить ввод$'), choosing_day)
            ],
            CHOOSING_STATIONS_MIDDLE: [
                MessageHandler(
                    Filters.text & ~(
                            Filters.command | Filters.regex('^Отменить ввод$') | Filters.regex('^Завершить ввод$')),
                    choosing_line,
                    ),
                MessageHandler(Filters.regex('^Отменить ввод$'), choosing_day),
                MessageHandler(Filters.regex('^Завершить ввод$'), choosing_time)

            ],
            DELETING_DAY: [
                MessageHandler(Filters.regex('^OK$'), choosing_day)
            ],
            CHOOSING_LINE: [
                MessageHandler(
                    Filters.text & ~(Filters.command),
                    choosing_stations_middle,
                    )
            ],
            CHOOSING_TIME: [
                MessageHandler(
                    Filters.text & ~(Filters.command),
                    ending_entering,
                    )
            ],
            CONFIRMING: [
                MessageHandler(Filters.regex('^OK$'), choosing_day),
                MessageHandler(Filters.regex('^Удалить расписание на этот день$'), deleting_day)

            ],
            STARTINGSEARCH: [
                MessageHandler(Filters.regex('^OK$'), choosing_day)
            ],
            SHOWING_OFF: [
                MessageHandler(Filters.regex('^Начать поиск$'), start_search),
                MessageHandler(Filters.regex('^В главное меню$'), choosing_day),
            ],
            DELETING: [
                MessageHandler(Filters.regex('^ДА$'), delete_compl),
                MessageHandler(Filters.regex('^НЕТ$'), choosing_day)

            ],
            DELETING_CONFIRMED: [
                MessageHandler(Filters.regex('^OK$'), choosing_day),
            ],
            SETTINGS_MENU: [
                MessageHandler(Filters.regex('^В главное меню$'), choosing_day),
                MessageHandler(Filters.regex('^Выбрать курс$'), level_choosing),
                MessageHandler(Filters.regex('^Выбрать ОП$'), selectOP1),
                MessageHandler(Filters.regex('^Очистить предпочтения$'), delete_pref),

            ]

        },
        fallbacks=[MessageHandler(Filters.regex('^Показать расписание и начать поиск людей$'), choosing_day)],
        name="all_conversation",
        persistent=True,
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
