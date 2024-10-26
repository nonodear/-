import asyncio
import aiogram
from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.filters import Command
from aiogram.types import Message, LinkPreviewOptions, InlineKeyboardButton, InlineKeyboardMarkup, InputFile, chat
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import BotCommand

bot = Bot(token='')
dp = Dispatcher()
router = Router()

@router.message(Command('start'))
async def send_welcome(message: Message):
    kb = [[types.KeyboardButton(text='выставки'),
            types.KeyboardButton(text='коллекция')],
            [types.KeyboardButton(text='о музее'),
            types.KeyboardButton(text='третьяковка онлайн')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('привет! я бот помощник третьяковской галереи. чем я могу помочь?', reply_markup=keyboard)

@router.message(F.text.lower() == 'выставки')
async def all_exhibitions(message: Message):
    kb = [[types.KeyboardButton(text='выставки в москве'),
            types.KeyboardButton(text='будущие выставки')],
            [types.KeyboardButton(text='архив выставок'),
            types.KeyboardButton(text='внешние выставки')],
            [types.KeyboardButton(text='постоянные экспозиции'),
            types.KeyboardButton(text='выставки в филиалах')],
            [types.KeyboardButton(text='в меню')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('please, choose', reply_markup=keyboard)

@router.message(F.text.lower() == 'в меню')
async def back_to_menu(message: Message):
    kb = [
        [types.KeyboardButton(text='выставки'),
         types.KeyboardButton(text='коллекция')],
        [types.KeyboardButton(text='о музее'),
         types.KeyboardButton(text='третьяковка онлайн')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('вы вернулись в главное меню. чем я могу помочь?', reply_markup=keyboard)

@dp.message(Command("help"))
async def helpme(message: Message):
    helper = LinkPreviewOptions(url="https://t.me/nonodear", prefer_small_media=True)
    await message.answer(f"if you have a problem, contact with my mommy", link_preview_options=helper)

#бонус для игроков!
@dp.message(Command("lucky"))
async def goodluck(message: types.Message):
    await message.answer_dice(emoji="🎲")

#боковое меню
async def menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/start', description='в начало'.lower()),
        BotCommand(command='/help', description='помогите'.lower()),
        BotCommand(command='/lucky', description='игрок'.lower())
    ]
    await bot.set_my_commands(main_menu_commands)
#dp.startup.register(menu)
#dp.run_polling(bot)

@router.message(F.text.lower() == 'выставки в москве')
async def exhibit(message: Message):
    builder1 = InlineKeyboardBuilder()
    builder1.button(text="адепты красного. малявин & архипов", callback_data='red')
    builder1.button(text="васнецовы. связь поколений", callback_data='vasne')
    builder1.button(text="живопись предельного состояния", callback_data='larin')
    builder1.button(text="алексей моргунов. среди первых", callback_data='morgunov')
    builder1.button(text="от мала до велика", callback_data='smallbig')
    builder1.button(text="александр иванов", callback_data='ivanov')
    builder1.button(text="история российского дизайна", callback_data='rudesign')
    builder1.button(text="природа предмета", callback_data='moderndesign')
    builder1.adjust(1)
    await message.answer('в настоящий момент в москве проходят следующие выставки', reply_markup=builder1.as_markup())


#подробности о выставках
@dp.callback_query(F.data == 'red')
async def callred(callback_query: types.CallbackQuery):
    text = ("*адепты красного. малявин & архипов*\n\n"
            "Государственная Третьяковская галерея представляет выставочный проект, приуроченный к двум юбилейным датам: к 155-летию со дня рождения Филиппа Малявина в 2024 году и 95 лет со дня смерти Абрама Архипова в 2025 году.\n\n"
            "Выставка проходит в Лаврушинском переулке, 12, 2 и 3 этажи.\n\n"
            "*сроки проведения*\n20 сентября 2024 — 16 февраля 2025\n\n"
            "*Адрес и часы работы*\nИнженерный корпус, г. Москва, Лаврушинский переулок, 12\nметро Новокузнецкая/Третьяковская/Полянка\n+7 (495) 957-07-27\n\n"
            "ВС, ВТ, СР: 10:00 — 18:00 (кассы и вход до 17:00)\nПН: выходной\nЧТ, ПТ, СБ: 10:00 — 21:00 (кассы и вход до 20:00)\n\n"
            "*билеты*\nЛьготные — 0, 300, 350 ₽\nВзрослый — 600 ₽\n\n"
            "доступна оплата по пушкинской карте"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/01c/1gmp8huul9rznpciqk54wnn0czvl9zg2.jpg"
    build1 = InlineKeyboardBuilder()
    build1.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/adepty-krasnogo-malyavin-i-arkhipov/")
    )
    build1.row(types.InlineKeyboardButton(
        text="купить билет",
        url="https://www.tretyakovgallery.ru/tickets/#/buy/event/30176/")
    )
    await bot.send_photo(callback_query.from_user.id, photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build1.as_markup())

@dp.callback_query(F.data == 'vasne')
async def callvasne(callback_query: types.CallbackQuery):
    text = ("*васнецовы. связь поколений из XIX в XXI век*\n\n"
            "Государственная Третьяковская галерея представляет масштабный выставочный проект, который познакомит зрителей с разносторонним творчеством выдающейся художественной династии Васнецовых. В экспозицию вошли лучшие произведения Виктора Михайловича (1848–1926), Аполлинария Михайловича (1856–1933) и Андрея Владимировича (1924–2009). Выставка приурочена к 175-летию со дня рождения Виктора Васнецова и к 100-летию со дня рождения Андрея Васнецова.\n\n"
            "Выставка проходит на Крымском Валу, 10, залы 60, 61, 80–82.\n\n"
            "*сроки проведения*\n23 мая 2024 — 4 ноября 2024\n\n"
            "*Адрес и часы работы*\nНовая Третьяковка, г. Москва, Крымский Вал, 10\nметро Парк Культуры/Октябрьская\n+7 (495) 957-07-27\n\n"
            "ВС, ВТ, СР: 10:00 — 18:00 (кассы и вход до 17:00)\nПН: выходной\nЧТ, ПТ, СБ: 10:00 — 21:00 (кассы и вход до 20:00)\n\n"
            "*билеты*\nЛьготные — 0, 450, 540 ₽\nВзрослый — 900 ₽\n\n"
            "доступна оплата по пушкинской карте"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/ef1/psh9501vh6p1l1ggz0glq5m1tvdk7n61.jpg"
    build2 = InlineKeyboardBuilder()
    build2.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/vasnetsovy-svyaz-pokoleniy-iz-xix-v-xxi-vek/")
    )
    build2.row(types.InlineKeyboardButton(
        text="купить билет",
        url="https://www.tretyakovgallery.ru/tickets/#/buy/event/28026/")
    )
    await bot.send_photo(callback_query.from_user.id, photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build2.as_markup())

@dp.callback_query(F.data == 'larin')
async def calllarin(callback_query: types.CallbackQuery):
    text = ("*юрий ларин. живопись предельного состояния*\n\n"
            "Государственная Третьяковская галерея представляет выставочный проект российского художника, живописца и графика Юрия Николаевича Ларина (1936 – 2014).\n\n"
            "Выставка проходит на Крымском Валу, 10, зал 38.\n\n"
            "*сроки проведения*\n11 октября 2024 — 19 января 2025\n\n"
            "*Адрес и часы работы*\nНовая Третьяковка, г. Москва, Крымский Вал, 10\nметро Парк Культуры/Октябрьская\n+7 (495) 957-07-27\n\n"
            "ВС, ВТ, СР: 10:00 — 18:00 (кассы и вход до 17:00)\nПН: выходной\nЧТ, ПТ, СБ: 10:00 — 21:00 (кассы и вход до 20:00)\n\n"
            "*билеты*\nЛьготные — 0, 300, 350 ₽\nВзрослый — 600 ₽\n\n"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/1f8/zrkmj6g83ozm3fdukg9vqb8ql8xn1b5o.jpg"
    build3 = InlineKeyboardBuilder()
    build3.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/yuriy-larin-zhivopis-predelnogo-sostoyaniya/")
    )
    build3.row(types.InlineKeyboardButton(
        text="купить билет",
        url="https://www.tretyakovgallery.ru/tickets/#/buy/event/3775/")
    )
    await bot.send_photo(callback_query.from_user.id, photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build3.as_markup())

@dp.callback_query(F.data == 'morgunov')
async def callmorgunov(callback_query: types.CallbackQuery):
    text = ("*aлексей моргунов. среди первых*\n\n"
            "Государственная Третьяковская галерея представляет выставочный проект, знакомящий с творчеством живописца Алексея Алексеевича Моргунова (1884–1935).\n\n"
            "Выставка проходит на Крымском Валу, 10, зал 10.\n\n"
            "*сроки проведения*\n12 сентября 2024 — 26 января 2025\n\n"
            "*Адрес и часы работы*\nНовая Третьяковка, г. Москва, Крымский Вал, 10\nметро Парк Культуры/Октябрьская\n+7 (495) 957-07-27\n\n"
            "ВС, ВТ, СР: 10:00 — 18:00 (кассы и вход до 17:00)\nПН: выходной\nЧТ, ПТ, СБ: 10:00 — 21:00 (кассы и вход до 20:00)\n\n"
            "*билеты*\nЛьготные — 0, 300, 350 ₽\nВзрослый — 600 ₽\n\n"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/cc3/n88p2w1imx5fjcuh3bkgeou6zzg9h3ow.jpg"
    build4 = InlineKeyboardBuilder()
    build4.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/aleksey-morgunov/")
    )
    build4.row(types.InlineKeyboardButton(
        text="купить билет",
        url="https://www.tretyakovgallery.ru/tickets/#/buy/event/3775/")
    )
    await bot.send_photo(callback_query.from_user.id, photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build4.as_markup())

@dp.callback_query(F.data == 'smallbig')
async def callsmallbig(callback_query: types.CallbackQuery):
    text = ("*от мала до велика. рисунки экстраординарных размеров из фондов графики XVIII – начала XX века*\n\n"
            "На выставке будут представлены экстраординарные по своим размерам произведения графики из собрания Третьяковской галереи: гигантские рисунки и крошечные миниатюры. Появление и тех, и других складывается в занимательную историю, в которой пики активного интереса к необычному формату чередуются с годами забвения.\n\n"
            "Выставка проходит в Лаврушинском переулке, 10, залы 49–54.\n\n"
            "*сроки проведения*\n20 июня 2024 — 17 ноября 2024\n\n"
            "*Адрес и часы работы*\nТретьяковская галерея, г. Москва, Лаврушинский переулок, 10\nметро Новокузнецкая/Третьяковская/Полянка\n+7 (495) 957-07-27\n\n"
            "ВС, ВТ, СР: 10:00 — 18:00 (кассы и вход до 17:00)\nПН: выходной\nЧТ, ПТ, СБ: 10:00 — 21:00 (кассы и вход до 20:00)\n\n"
            "*билеты*\nЛьготные — 0, 350, 400 ₽\nВзрослый — 700 ₽\n\n"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/47d/6aw7o0g65dbc0wmf38kww7b3vbjhy27a.jpg"
    build5 = InlineKeyboardBuilder()
    build5.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/ot-mala-do-velika-risunki-ekstraordinarnykh-razmerov-iz-fondov-grafiki-xviii-nachala-xx-veka/")
    )
    build5.row(types.InlineKeyboardButton(
        text="купить билет",
        url="https://www.tretyakovgallery.ru/tickets/#/buy/event/3765/")
    )
    await bot.send_photo(callback_query.from_user.id, photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build5.as_markup())

@dp.callback_query(F.data == 'ivanov')
async def callivanov(callback_query: types.CallbackQuery):
    text = ("*александр иванов – рисовальщик, вдохновленный классикой*\n\n"
            "Третьяковская галерея – эксклюзивный обладатель графического наследия Александра Андреевича Иванова (1806–1858), включающего в себя более 700 самостоятельных листов и около 40 альбомов. Полнота собрания позволяет сформировать несколько сменяющих друг друга экспозиций, каждая из которых имеет характер мини-выставки.\n\n"
            "Выставка проходит в Лаврушинском переулке, 10, зал 11.\n\n"
            "*сроки проведения*\n31 мая 2024 — 17 ноября 2024\n\n"
            "*Адрес и часы работы*\nТретьяковская галерея, г. Москва, Лаврушинский переулок, 10\nметро Новокузнецкая/Третьяковская/Полянка\n+7 (495) 957-07-27\n\n"
            "ВС, ВТ, СР: 10:00 — 18:00 (кассы и вход до 17:00)\nПН: выходной\nЧТ, ПТ, СБ: 10:00 — 21:00 (кассы и вход до 20:00)\n\n"
            "*билеты*\nЛьготные — 0, 350, 400 ₽\nВзрослый — 700 ₽\n\n"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/95c/lg7votnlplm4ibo0kg0e2t7hmdhaep8a.jpg"
    build6 = InlineKeyboardBuilder()
    build6.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/aleksandr-ivanov-risovalshchik-vdokhnovlennyy-klassikoy/")
    )
    build6.row(types.InlineKeyboardButton(
        text="купить билет",
        url="https://www.tretyakovgallery.ru/tickets/#/buy/event/3765")
    )
    await bot.send_photo(callback_query.from_user.id, photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build6.as_markup())

@dp.callback_query(F.data == 'rudesign')
async def callrudesign(callback_query: types.CallbackQuery):
    text = ("*история российского дизайна. национальные традиции и современность*\n\n"
            "Московский музей дизайна в рамках форума «Российская креативная неделя» представляет обновлённую экспозицию «История российского дизайна. Национальные традиции и современность», исследующую настоящее и прошлое отечественного дизайна.\n\n"
            "Выставка проходит в Западном крыле Новой Третьяковки, зал 3.\n\n"
            "*сроки проведения*\n1 ноября 2022 — 24 ноября 2024\n\n"
            "*Адрес и часы работы*\nЗападное крыло Новой Третьяковки, г. Москва, Крымский Вал, 10\nметро Парк Культуры/Октябрьская\n+7 (495) 957-07-27\n\n"
            "ВС, ВТ, СР: 10:00 — 18:00 (кассы и вход до 17:00)\nПН: выходной\nЧТ, ПТ, СБ: 10:00 — 21:00 (кассы и вход до 20:00)\n\n"
            "*билеты*\nЛьготные — 0, 200, 250 ₽\nВзрослый — 400 ₽\n\n"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/f40/054b7wpn9rjswjxrouydpeu2vrxeftd0.jpg"
    build7 = InlineKeyboardBuilder()
    build7.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/istoriya-rossiyskogo-dizayna-natsionalnye-traditsii-i-sovremennost/")
    )
    build7.row(types.InlineKeyboardButton(
        text="купить билет",
        url="https://www.tretyakovgallery.ru/tickets/#/buy/event/11748")
    )
    await bot.send_photo(callback_query.from_user.id, photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build7.as_markup())

@dp.callback_query(F.data == 'moderndesign')
async def callmodern(callback_query: types.CallbackQuery):
    text = ("*природа предмета. современный дизайн и традиции*\n\n"
            "Фиджитал-выставку представляет Московский музей дизайна совместно с Государственной Третьяковкой галереей и проектом «Трын-Трава. Современный русский стиль».\n\n"
            "Выставка проходит в Западном крыле Новой Третьяковки, зал 5.\n\n"
            "*сроки проведения*\n2 июля 2024 — 4 ноября 2024\n\n"
            "*Адрес и часы работы*\nЗападное крыло Новой Третьяковки, г. Москва, Крымский Вал, 10\nметро Парк Культуры/Октябрьская\n+7 (495) 957-07-27\n\n"
            "ВС, ВТ, СР: 10:00 — 18:00 (кассы и вход до 17:00)\nПН: выходной\nЧТ, ПТ, СБ: 10:00 — 21:00 (кассы и вход до 20:00)\n\n"
            "*билеты*\nЛьготные — 0, 200, 250 ₽\nВзрослый — 400 ₽\n\n"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/189/xfthlshayjd2fp1as8d4hm0wgb0spchi.jpg"
    build8 = InlineKeyboardBuilder()
    build8.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/priroda-predmeta-sovremennyy-dizayn-i-traditsii-/")
    )
    build8.row(types.InlineKeyboardButton(
        text="купить билет",
        url="https://www.tretyakovgallery.ru/tickets/#/buy/event/11748")
    )
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build8.as_markup())



@router.message(F.text.lower() == 'будущие выставки')
async def exhibit(message: Message):
    builder2 = InlineKeyboardBuilder()
    builder2.button(text="передвижники", callback_data='peredvizh')
    builder2.button(text="магия акварели", callback_data='aqua')
    builder2.button(text="виктор попков", callback_data='popkov')
    builder2.button(text="пять веков русского искусства", callback_data='five')
    builder2.adjust(1)
    await message.answer('в ближайшее время планируется открытие следующих выставок', reply_markup=builder2.as_markup())

@dp.callback_query(F.data == 'peredvizh')
async def callperedv(callback_query: types.CallbackQuery):
    text = ("*передвижники*\n\n"
            "Государственная Третьяковская галерея представляет центральный выставочный проект 2024 года, посвященный творческой деятельности художников – членов и экспонентов Товарищества передвижных художественных выставок, которых мы сегодня называем передвижниками.\n\n"
            "Выставка будет проходить на Кадашёвской набережной, 12, залы 3-го этажа.\n\n"
            "*сроки проведения*\n30 октября 2024 — 6 апреля 2025\n\n"
            "*Адрес и часы работы*\nКорпус на Кадашёвской набережной, 119017, г. Москва, Кадашёвская набережная, 12\n+7 (495) 957-07-27\n\n"
            "*билеты*\nЛьготные — 0, 450, 540 ₽\nВзрослый — 900 ₽\n\n"
            "Скоро скоро скоро!"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/4a1/kwmks40pj9h1qh61jekl355ke1lcl8cw.jpg"
    build9 = InlineKeyboardBuilder()
    build9.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/peredvizhniki-/")
    )
    build9.row(types.InlineKeyboardButton(
        text="купить билет",
        url="https://www.tretyakovgallery.ru/tickets/#/buy/event/31936/")
    )
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build9.as_markup())

@dp.callback_query(F.data == 'aqua')
async def callaqua(callback_query: types.CallbackQuery):
    text = ("*Магия акварели. Из фондов графики XVIII – начала XX века*\n\n"
            "Государственная Третьяковская галерея представляет выставку шедевров графики XVIII–XX веков, исполненных акварелью, из собрания музея. \n\n"
            "Выставка будет проходить в Лаврушинском переулке, 10, залы 49–54.\n\n"
            "*сроки проведения*\n29 ноября 2024 — 18 мая 2025\n\n"
            "*Адрес и часы работы*\nТретьяковская галерея, г. Москва, Лаврушинский переулок, 10\nметро Новокузнецкая/Третьяковская/Полянка\n+7 (495) 957-07-27\n\n"
            "покупка билетов пока недоступна\n\n"
            "Скоро скоро скоро!"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/f52/60d74qpmv4586gukt1kn3t8uct4vb0kp.jpg"
    build10 = InlineKeyboardBuilder()
    build10.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/magiya-akvareli-iz-fondov-grafiki-xviii-nachala-xx-veka/")
    )
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build10.as_markup())

@dp.callback_query(F.data == 'popkov')
async def callpopkov(callback_query: types.CallbackQuery):
    text = ("*Виктор Попков*\n\n"
            "Третьяковская галерея представляет крупнейшую монографическую выставку Виктора Попкова (1932–1974) – одного из ведущих мастеров, определивших облик отечественного искусства второй половины ХХ века. В состав выставки войдет более 200 живописных и графических работ мастера.\n\n"
            "Выставка будет проходить на Кадашёвской набережной, 12, залы 1-го этажа.\n\n"
            "*сроки проведения*\n4 декабря 2024 — 11 мая 2025\n\n"
            "*Адрес и часы работы*\nКорпус на Кадашёвской набережной, 119017, г. Москва, Кадашёвская набережная, 12\n+7 (495) 957-07-27\n\n"
            "покупка билетов пока недоступна\n\n"
            "Скоро скоро скоро!"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/8cc/hlix95zn0x68sh4qxw9gym0lcltxal3u.jpg"
    build11 = InlineKeyboardBuilder()
    build11.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/viktor-popkov/")
    )
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build11.as_markup())

@dp.callback_query(F.data == 'five')
async def callfive(callback_query: types.CallbackQuery):
    text = ("*Третьяковская галерея. Пять веков русского искусства*\n\n"
            "Первая выставка, которой откроется филиал, представит хронологический экскурс в историю русского искусства.\n\n"
            "*сроки проведения*\nМарт 2025 — Ноябрь 2025\n\n"
            "*Адрес и часы работы*\nФилиал Третьяковской галереи в Калининграде, г. Калининград, Парадная набережная, 3\n+7 (495) 957-07-27\n\n"
            "покупка билетов пока недоступна\n\n"
            "Скоро скоро скоро!"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/9b1/qbqmq09lfhcbkv7m1dzu9fm3265bwwld.jpg"
    build12 = InlineKeyboardBuilder()
    build12.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/tretyakovskaya-galereya-pyat-vekov-russkogo-iskusstva-/")
    )
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build12.as_markup())



@router.message(F.text.lower() == 'архив выставок')
async def exhibit(message: Message):
    builder3 = InlineKeyboardBuilder()
    builder3.row(types.InlineKeyboardButton(
        text="архив",
        url="https://www.tretyakovgallery.ru/exhibitions/arkhiv-vystavok/")
    )
    await message.answer('архив выставок доступен по ссылке', reply_markup=builder3.as_markup())



@router.message(F.text.lower() == 'внешние выставки')
async def exhibit(message: Message):
    builder4 = InlineKeyboardBuilder()
    builder4.button(
        text="русская душа",
        callback_data='rusoul'
    )
    builder4.adjust(1)
    await message.answer('выездные выставки шедевров третьяковки в других странах', reply_markup=builder4.as_markup())

@dp.callback_query(F.data == 'rusoul')
async def callrusoul(callback_query: types.CallbackQuery):
    text = ("*Русская душа. Избранные произведения живописи из Государственной Третьяковской галереи и цифровые полотна о культурном наследии Суздаля*\n\n"
            "В рамках перекрестных Годов культуры России и Китая Государственная Третьяковская галерея совместно с Владимиро-Суздальским музеем-заповедником при поддержке компании VK представляет выставочный проект в Столичном музее Пекина.\n\n"
            "*сроки проведения*\n25 сентября 2024 — 3 декабря 2024\n\n"
            "*Адрес и часы работы*\nСтоличный музей Пекина, Пекин, улица Фусинмэньвай, 16, район Сичэн\n\n"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/97c/f8tgd3ocd1ikxf5kldrd5njrsolezse7.jpg"
    build13 = InlineKeyboardBuilder()
    build13.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/russkaya-dusha-izbrannye-proizvedeniya-zhivopisi-iz-gosudarstvennoy-tretyakovskoy-galerei-i-tsifrovy/")
    )
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build13.as_markup())



@router.message(F.text.lower() == 'постоянные экспозиции')
async def exhibit(message: Message):
    builder5 = InlineKeyboardBuilder()
    builder5.button(text="туристический билет. маршрут 2", url = 'https://www.tretyakovgallery.ru/exhibitions/o/turisticheskiy-bilet-marshrut-2/')
    builder5.button(text="маршрут для всей семьи", url = 'https://www.tretyakovgallery.ru/exhibitions/o/muzeynyy-marshrut-dlya-vsey-semi-7-shedevrov-avangarda/')
    builder5.button(text="шедевры XI - начала XX века", url = 'https://www.tretyakovgallery.ru/exhibitions/o/shedevry-russkogo-iskusstva-xi-nachala-xx-veka/')
    builder5.button(text="искусство XX века", url='https://www.tretyakovgallery.ru/exhibitions/o/iskusstvo-khkh-veka/')
    builder5.button(text="музей-квартира а.васнецова", url = 'https://www.tretyakovgallery.ru/exhibitions/o/muzey-kvartira-apollinariya-vasnetsova_/')
    builder5.button(text="дом-музей виктора васнецова", url = 'https://www.tretyakovgallery.ru/exhibitions/o/dom-muzey-viktora-vasnetsova_/')
    builder5.button(text="музей павла и сергея третьяковых", url = 'https://www.tretyakovgallery.ru/exhibitions/o/muzey-pavla-i-sergeya-tretyakovykh/')
    builder5.adjust(1)
    await message.answer('основная коллекция третьяковки', reply_markup=builder5.as_markup())



@router.message(F.text.lower() == 'выставки в филиалах')
async def exhibit(message: Message):
    builder6 = InlineKeyboardBuilder()
    builder6.button(text="порт приписки - дальний восток", callback_data='fareast')
    builder6.button(text="на вкус и цвет", callback_data='samara')
    builder6.adjust(1)
    await message.answer('искусство в филиалах третьяковки, шедевры за пределами столицы', reply_markup=builder6.as_markup())

@dp.callback_query(F.data == 'fareast')
async def callfareast(callback_query: types.CallbackQuery):
    text = ("*Интерактивная выставка «Порт приписки – Дальний Восток»*\n\n"
            "Государственная Третьяковская галерея представляет в Общественном пространстве музея во Владивостоке интерактивную выставку «Порт приписки – Дальний Восток». Проект реализован при поддержке Транспортной группы FESCO. Выставка посвящена этапам художественного освоения Дальнего Востока.\n\n"
            "*сроки проведения*\n16 августа 2024 — 10 ноября 2024\n\n"
            "*Адрес и часы работы*\nФилиал Третьяковской галереи во Владивостоке, г. Владивосток, ул. Алеутская, 15\n+7 (914) 723-72-68\n\n"
            "ВС, ВТ, СР: 10:00 — 19:00\nПН: выходной\nЧТ, ПТ, СБ: 10:00 — 21:00\n\n"
            "*билеты*\nДля всех — бесплатно\n\n"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/a5e/969pphljo2q4tdu7d0xax2ikqsluiknp.jpg"
    build14 = InlineKeyboardBuilder()
    build14.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/interaktivnaya-vystavka-port-pripiski-dalniy-vostok/")
    )
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build14.as_markup())

@dp.callback_query(F.data == 'samara')
async def callsamara(callback_query: types.CallbackQuery):
    text = ("*На вкус и цвет. Образы еды в русском искусстве*\n\n"
            "Филиал Третьяковской галереи в Самаре представляет свою первую выставку в отреставрированном здании Фабрики-кухни – выдающемся памятнике конструктивизма. Это пространство бывшего утопического конвейера, место производства и потребления еды. Здание продиктовало тему выставки: еда возвращается в эти стены не как вещь, которую здесь производят, но как знаковый художественный образ, первооснова человеческого опыта и универсальная метафора в российском искусстве с XIX века по настоящее время.\n\n"
            "В состав проекта вошло более 80 произведений из коллекции Государственной Третьяковской галереи, а также 10 произведений из частных собраний.\n\n"
            "*сроки проведения*\n30 мая 2024 — 3 ноября 2024\n\n"
            "*Адрес и часы работы*\nФилиал Третьяковской галереи в Самаре, г. Самара, ул. Ново-Садовая, 149\n+7 (800) 755-90-00\n\n"
            "ВС, ВТ, СР, ЧТ, ПТ, СБ: 10:00 — 21:00 (кассы и вход до 20:00)\nПН: выходной\n\n"
            "*билеты*\nЛьготные — 0, 300, 350 ₽\nВзрослый — 600 ₽\n\n"
            "доступна оплата по пушкинской карте"
            )
    photo_url = "https://www.tretyakovgallery.ru/upload/iblock/f37/n3t2p8tcyeby5ie2z2pyaaobzh2hhmmi.jpg"
    build15 = InlineKeyboardBuilder()
    build15.row(types.InlineKeyboardButton(
        text="подробности мероприятия",
        url="https://www.tretyakovgallery.ru/exhibitions/o/na-vkus-i-tsvet-obrazy-edy-v-russkom-iskusstve/")
    )
    build15.row(types.InlineKeyboardButton(
        text="купить билет",
        url="https://samara.tretyakovgallery.ru/tickets/#/buy/event/28581")
    )
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url, caption=text.lower(), parse_mode='Markdown', reply_markup=build15.as_markup())



#кнопка 'коллекция' = переадресация на сайт третьяковки для просмотра всего собрания шедевров
@router.message(F.text.lower() == 'коллекция')
async def collection(message: Message, bot: Bot):
    builder7 = InlineKeyboardBuilder()
    builder7.row(types.InlineKeyboardButton(
        text="коллекция музея",
        url="https://my.tretyakov.ru/app/gallery/")
    )
    photo_url = 'https://www.tretyakovgallery.ru/upload/iblock/feb/zd5kvywe7pmh26b7hymwylhmilqa09gj.jpg'
    text = "для просмотра полного собрания шедевров третьяковской галереи перейдите по ссылке ниже"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_url, caption=text, parse_mode='Markdown', reply_markup=builder7.as_markup())



#кнопка 'о музее' чтение файла с рассказом о ценностях и описании третьяковки
@router.message(F.text.lower() == 'о музее')
async def museum(message: Message):
    with open('museum.txt') as file:
        amuseum = file.read().lower()
    builder8 = InlineKeyboardBuilder()
    builder8.button(text="история галереи", callback_data='mushistory')
    builder8.button(text="подробности", url = 'https://www.tretyakovgallery.ru/about/mission/')
    builder8.adjust(1)
    await message.answer(amuseum, parse_mode='Markdown', reply_markup=builder8.as_markup())
#чтение файла с краткой историей галереи
@dp.callback_query(F.data == 'mushistory')
async def callmushistory(callback_query: types.CallbackQuery):
    with open('mhistory.txt') as file:
        history = file.read().lower()
    build16 = InlineKeyboardBuilder()
    build16.row(types.InlineKeyboardButton(
        text="интерактивная версия",
        url="https://www.tretyakovgallery.ru/about/history/")
    )
    photo_url = 'https://tunnel.ru/tmp/2O1JLFGYnaS6bVDsBmzi/foto.jpg'
    await bot.send_photo(chat_id = callback_query.from_user.id, photo = photo_url, caption = history, parse_mode='Markdown', reply_markup=build16.as_markup())



#кнопка 'третьяковка онлайн' = выбор новых кнопок: онлайн проекты или соцсети третьяковки
@router.message(F.text.lower() == 'третьяковка онлайн')
async def online(message: Message):
    kb = [[types.KeyboardButton(text='онлайн проекты'),
            types.KeyboardButton(text='соцсети')],
          [types.KeyboardButton(text='в меню')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(text = 'please, choose', reply_markup=keyboard)

#ссылки на онлайн проекты третьяковки
@router.message(F.text.lower() == 'онлайн проекты')
async def project(message: Message, bot: Bot):
    build17 = InlineKeyboardBuilder()
    build17.row(types.InlineKeyboardButton(
        text="моя третьяковка",
        url="https://clck.ru/V6Sg9"))
    build17.row(types.InlineKeyboardButton(
        text="лаврус",
        url="https://lavrus.tretyakov.ru/?utm_source=saitgtg&utm_medium=referral&utm_campaign=mainmenu&utm_content=lavrus")
    )
    build17.row(types.InlineKeyboardButton(
        text="музеи по соседству",
        url="https://clck.ru/V6T3B")
    )
    build17.row(types.InlineKeyboardButton(
        text="третьяковка в самаре",
        url="https://samara.tretyakovgallery.ru/")
    )
    build17.row(types.InlineKeyboardButton(
        text="подкасты",
        url="https://tgallery.mave.digital/")
    )
    await message.answer(
        "приобщайтесь к прекрасному онлайн",
        reply_markup=build17.as_markup()
    )
#ссылки на соцсети третьяковки
@router.message(F.text.lower() == 'соцсети')
async def socmedia(message: Message, bot: Bot):
    build18 = InlineKeyboardBuilder()
    build18.row(types.InlineKeyboardButton(
        text="youtube",
        url="https://www.youtube.com/channel/UCCJR2fHtwpHs5eYirnbCNQA")
    )
    build18.row(types.InlineKeyboardButton(
        text="rutude",
        url="https://rutube.ru/channel/25592111/")
    )
    build18.row(types.InlineKeyboardButton(
        text="telegram",
        url="https://t.me/GT_Gallery")
    )
    build18.row(types.InlineKeyboardButton(
        text="вконтакте",
        url="https://vk.com/tretyakovgallery")
    )
    build18.row(types.InlineKeyboardButton(
        text="одноклассники",
        url="https://ok.ru/tretyakovgallery")
    )
    await message.answer(
        "оставайтесь на связи и следите за анонасами",
        reply_markup=build18.as_markup()
    )

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

