from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

# main_menu = ReplyKeyboardMarkup(resize_keyboard=True,row_width=5)
#
# one = KeyboardButton(text='1')
# two = KeyboardButton(text='2')
# three = KeyboardButton(text='3')
#
# main_menu.add(one)
# main_menu.add(two)
# main_menu.add(three)

# main_menu = ReplyKeyboardMarkup(resize_keyboard=True)


# main_menu.add(KeyboardButton('Menu'))



main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

main_menu.add(
    KeyboardButton(text='Kuzatish va yangilanishlar:'),
    KeyboardButton(text="Qo'llab-quvvatlash va maslahatlar:")
)
main_menu.add(
    KeyboardButton(text="Qo'llab-quvvatlash guruhlari:"),
    KeyboardButton(text="Qidiruv va yo'naltirish:")
)
main_menu.add(
    KeyboardButton(text="Ta'lim va treninglar:"),
    KeyboardButton(text='Hujjatlar va rasmiyatchiliklar:')
)
main_menu.add(
    KeyboardButton(text="Ish va uy-joy qidirish:")
)
kuzatish_menu = InlineKeyboardMarkup()

kuzatish_menu.add(
    InlineKeyboardButton(text="Yangi ish o'rinlari haqidagi e'lonlar.", callback_data='new_jobs')
)
kuzatish_menu.add(
    InlineKeyboardButton(text="Migrantlar uchun huquqiy maslahatlar va yangiliklar.", callback_data='new_info')
)
kuzatish_menu.add(
    InlineKeyboardButton(text="Migrantlar uchun mo'ljallangan tadbirlar va o'quv kurslari haqidagi ma'lumotlar.", callback_data='marosim')
)


support_menu = InlineKeyboardMarkup()

support_menu.add(
    InlineKeyboardButton(text="Huquqiy yordam bo'yicha maslahatlar.",callback_data='help')
)
support_menu.add(
    InlineKeyboardButton(text="Sog'liqni saqlash va tibbiy yordam bo'yicha maslahatlar.",callback_data='mhelp')
)
support_menu.add(
    InlineKeyboardButton(text="Ijtimoiy yordam dasturlari haqida ma'lumotlar.",callback_data='socialhelp')
)

support_group_menu = InlineKeyboardMarkup()

support_group_menu.add(
    InlineKeyboardButton(text="Hamjamiyat va qo'llab-quvvatlash guruhlari.",callback_data='socialsupport')
)
support_group_menu.add(
    InlineKeyboardButton(text="Tajriba almashish va yordam so'rash uchun guruh chatlari.",callback_data='fsupport')
)

searchs_menu = InlineKeyboardMarkup()

searchs_menu.add(
   InlineKeyboardButton(text="Yaqin atrofdagi xizmat ko'rsatish markazlarini topish.",callback_data="service")
)
searchs_menu.add(
   InlineKeyboardButton(text="Rasmiy idoralarga yo'naltirish.",callback_data="fromservice")
)

learn_trening_menu = InlineKeyboardMarkup()

learn_trening_menu.add(
    InlineKeyboardButton(text="Bepul yoki arzon narxlardagi til kurslari.",callback_data="freecourse")
)
learn_trening_menu.add(
    InlineKeyboardButton(text="Malaka oshirish va kasbiy treninglar haqida ma'lumotlar.",callback_data="fcourse")
)

document_menu = InlineKeyboardMarkup()

document_menu.add(
    InlineKeyboardButton(text="Patent va boshqa rasmiy hujjatlarni tayyorlash bo'yicha yo'riqnomalar.",callback_data="patent")
)
document_menu.add(
    InlineKeyboardButton(text="Muhojirlik jarayonlarida kerak bo'ladigan hujjatlar ro'yxati.",callback_data="mpatent")
)

ijara_ish_menu = InlineKeyboardMarkup()

ijara_ish_menu.add(
    InlineKeyboardButton(text="Ish o'rinlari va ish beruvchilar bilan bog'lanish.",callback_data="jobsd")
)
ijara_ish_menu.add(
    InlineKeyboardButton(text="Ijaraga uy-joy topish bo'yicha maslahatlar.",callback_data="homed")
)


phone_button = KeyboardButton(text="Telefon raqamni yuborish",request_contact=True)
registr_number = ReplyKeyboardMarkup(resize_keyboard=True).add(phone_button)
