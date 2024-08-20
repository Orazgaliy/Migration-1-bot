from aiogram import Dispatcher,Bot,executor,types
from keyboards import main_menu,kuzatish_menu,support_menu,support_group_menu,searchs_menu,learn_trening_menu,document_menu,ijara_ish_menu,registr_number
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from datas import start_db,add_user,show_user



api = 'your api'
proxy = "http://proxy.server:3128/"
bot = Bot(api,proxy=proxy)
dp = Dispatcher(bot=bot)

channel_id = '-1002157955004'
async def on_startup(_):
    await start_db()

def inlin_buttons():
    channel_url = InlineKeyboardButton("Kanalimiz",url='https://t.me/testchannellsubscruibe')
    check = InlineKeyboardButton("A'zo bo'ldim",callback_data='subdone')
    markup = InlineKeyboardMarkup(row_width=1).add(channel_url,check)
    return markup

@dp.message_handler(commands=['start'])
async def start(sms:types.Message):
    check_sub_channel = await bot.get_chat_member(chat_id=channel_id,user_id=sms.from_user.id)

    if check_sub_channel['status'] != 'left':
        await sms.answer('''Bo'timizdan foydalanish uchun avval registraciyadan o'ting!''',reply_markup=registr_number)
    else:
        await sms.answer("Botdan foydalanish uchun iltimos kanalimizga a'zo bo'ling! 🚫",reply_markup=inlin_buttons())



@dp.callback_query_handler(lambda call: call.data=='subdone')
async def check_sub(callback : types.CallbackQuery):
    
    if callback.data == "subdone":
        check_sub_channel = await bot.get_chat_member(chat_id=channel_id,user_id=callback.message.from_user.id)


        if check_sub_channel['status']!='left':
                await callback.message.answer('''Bo'timizdan foydalanish uchun avval registraciyadan o'ting!''',reply_markup=registr_number)
        else:
                await callback.message.answer("Botdan foydalanish uchun iltimos kanalimizga a'zo bo'ling! 🚫",reply_markup=inlin_buttons())

# 👋Botimizga xush kelibsiz! Siz bizning botimiz orqali migrantlarga kerakli bo'lgan ma'lumotlar va e'lonlarni topishingiz mumkin

# @dp.message_handler(text='Telefon raqamni yuborish')
# async def
@dp.message_handler(content_types=types.ContentType.CONTACT)
async def regition_comt(sms:types.Message):
    contact=sms.contact
    await add_user(id=sms.from_user.id,
                   username=sms.from_user.username,
                   first_name=sms.from_user.first_name,
                   last_name=sms.from_user.last_name,
                   phone_number=contact.phone_number

    )
    user_id=sms.from_user.id
    ids = await show_user()
    if user_id in ids:
        await sms.answer(text="Siz allaqachon ro'yxatdan o'tgansiz.",reply_markup=main_menu)
    else:
        await sms.answer(text='''👋Botimizga xush kelibsiz! Siz bizning botimiz orqali migrantlarga kerakli 
        bo'lgan ma'lumotlar va e'lonlarni topishingiz mumkin''',reply_markup=main_menu)
@dp.message_handler(text = "Kuzatish va yangilanishlar:")
async def send_kmenu(sms:types.Message):
    await sms.answer(
        text='Kuzatish va yangilanishlar:👇',
        reply_markup=kuzatish_menu
    )

@dp.callback_query_handler(lambda call: call.data =="new_jobs")
async def send_d(call:types.CallbackQuery):
    data = call.data
    if data == "new_jobs":
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f'''Sizga ish izlash uchun uchun quyidagi kanal va guruhlarni tavsiya etamiz:
            @tayanch_moskva01''',
            reply_markup="main_menu"
        )

@dp.callback_query_handler(lambda call: call.data =="new_info")
async def send_info(call:types.CallbackQuery):
    data = call.data
    if data == "new_info":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Sizga migrantlar yangiliklarni yoritib boruvchi quyidagi kanallarni tavsiya etamiz:
            @uz_migrant
            @migrantuzb''' 
        )

@dp.callback_query_handler(lambda call: call.data=="marosim")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "marosim":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Migrantlar uchun mo'ljallangan tadbirlar va o'quv kurslari haqidagi ma'lumotlar xaqida xabardor bo'lish uchun quyidagi kanalni tavsiya etamiz:
            @rustili_uzb
            '''
        )
@dp.message_handler(text = "Qo'llab-quvvatlash va maslahatlar:")
async def send_support(sms:types.Message):
    await sms.answer(
        text='''Qo'llab-quvvatlash va maslahatlar: 👇
        ''',
        reply_markup=support_menu
    )

@dp.message_handler(text = "Qo'llab-quvvatlash guruhlari:")
async def send_support(sms:types.Message):
    await sms.answer(
        text='''Qo'llab-quvvatlash guruhlari: 👇
        ''',
        reply_markup=support_group_menu
    )
@dp.message_handler(text = "Qidiruv va yo'naltirish:")
async def send_support(sms:types.Message):
    await sms.answer(
        text='''Qidiruv va yo'naltirish:👇
        ''',
        reply_markup=searchs_menu
    )
@dp.message_handler(text = "Ta'lim va treninglar:")
async def send_support(sms:types.Message):
    await sms.answer(
        text='''Ta'lim va treninglar: 👇
        ''',
        reply_markup=learn_trening_menu
    )
@dp.message_handler(text = "Hujjatlar va rasmiyatchiliklar:")
async def send_support(sms:types.Message):
    await sms.answer(
        text='''Hujjatlar va rasmiyatchiliklar: 👇
        ''',
        reply_markup=document_menu
    )
@dp.message_handler(text = "Ish va uy-joy qidirish:")
async def send_support(sms:types.Message):
    await sms.answer(
        text='''Ish va uy-joy qidirish: 👇
        ''',
        reply_markup=ijara_ish_menu
    )


@dp.callback_query_handler(lambda call: call.data=="help")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "help":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Huquqiy yordam bo'yicha maslahatlar.
            @migratsiyaagentligi
            '''
        )

@dp.callback_query_handler(lambda call: call.data=="mhelp")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "mhelp":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Sog'liqni saqlash va tibbiy yordam bo'yicha maslahatlar:
            @tibbiyot_haqida
            '''
        )
@dp.callback_query_handler(lambda call: call.data=="socialhelp")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "socialhelp":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Ijtimoiy yordam dasturlari haqida ma'lumotlar:
            @ijtimoiyhimoya_agentligi
            '''
        )

@dp.callback_query_handler(lambda call: call.data=="socialsupport")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "socialsupport":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Hamjamiyat va qo'llab-quvvatlash guruhlari:
            @migration_uzb
            '''
        )
@dp.callback_query_handler(lambda call: call.data=="fsupport")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "fsupport":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Tajriba almashish va yordam so'rash uchun guruh chatlari:
            @rosmigrantuz
            '''
        )

@dp.callback_query_handler(lambda call: call.data=="service")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "service":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Yaqin atrofdagi xizmat ko'rsatish markazlarini topish:
            @musofirlar
            '''
        )

@dp.callback_query_handler(lambda call: call.data=="fromservice")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "fromservice":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Rasmiy idoralarga yo'naltirish:
            @avtmvrf
            '''
        )
@dp.callback_query_handler(lambda call: call.data=="freecourse")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "freecourse":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Bepul yoki arzon narxlardagi til kurslari
            @migraciya_center_video
            '''
        )

@dp.callback_query_handler(lambda call: call.data=="fcourse")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "fcourse":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Malaka oshirish va kasbiy treninglar haqida ma'lumotlar:
            @malakaoshirish_official
            '''
        )

@dp.callback_query_handler(lambda call: call.data=="patent")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "patent":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Patent va boshqa rasmiy hujjatlarni tayyorlash bo'yicha yo'riqnomalar:
            @pitere_moskvad_patent 
            @Moskvada_ish_topish
            '''
        )

@dp.callback_query_handler(lambda call: call.data=="mpatent")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "mpatent":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Muhojirlik jarayonlarida kerak bo'ladigan hujjatlar ro'yxati:
            «Госуслуги» orqali migratsion qaydga (регистрация) topshirilganda javob kelmasa nima qilish kerak?
            
            Agar migratsion qaydni uzaytirish uchun «Госуслуги» orqali ariza topshirilgan va javob chiqmayotgan bo‘lsa qaytadan yana topshiraverish kerak. 
            Qolaversa, “МВД” bo‘limiga qabul uchun ham yozilish lozim.
            “МВД” qabuli vaqti kelguncha «Госуслуги» orqali qaytadan migratsion qayd uchun arizani yuborish mumkin va tajribada bu juda yaxshi samara berishiga guvohmiz. 
            Qayta ariza yuborganda orada necha kun o‘tib ketganining ahamiyati yo‘q. «Госуслуги» orqali arizani faqat bir marta yuborish mumkin, degan qoida yo‘q. 
            Shuning uchun “регистрация” tayyor  bo‘lguncha qayta-qayta ariza yuborsa bo‘ladi. 
            Agar “МВД”ga qabul vaqti kelganda qayta yuborilgan arizalar bo‘yicha ham registratsiya tayyor bo‘lmagan bo‘lsa, 
            unda “МВД” qabuliga kelganda registratsiyani «Госуслуги» orqali topshirilgani haqida xabar berish kerak. 
            Shunda xodimlar «регистрация» uchun hech qanday to‘sqinlik bo‘lmasa va taqdim qilingan hujjatlar yetarli 
            bo‘lsa “МВД” bo‘limining o‘zida rasmiylashtirib berishadi.
            '''
        )

@dp.callback_query_handler(lambda call: call.data=="jobsd")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "jobsd":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Ish o'rinlari va ish beruvchilar bilan bog'lanish:
            @Maskvada_ishbor
            '''
        )

@dp.callback_query_handler(lambda call: call.data=="homed")
async def send_lm(call:types.CallbackQuery):
    data = call.data
    if data == "homed":
        await bot.send_message(
            chat_id=call.from_user.id,
            text='''Ijaraga uy-joy topish bo'yicha maslahatlar:
            @Moskva_rabota_kvartira
            '''
        ) 


# @dp.message_handler(commands=['start'])
# async def send_hi(sms:types.Message):
#     await sms.answer(text='Assalamu aleykum',reply_markup=main_menu)
# @dp.message_handler(text='1')
# async def send_photo(sms:types.Message):
#     suwret = open(file='images/lion.jpg',mode="rb")
#     await bot.send_photo(
#         chat_id=sms.from_user.id,
#         photo=suwret,
#         caption=f'Mine sizge Arislan suretin jiberdim {sms.from_user.first_name}'
#     )
# @dp.message_handler(text='2')
# async def send_account(sms:types.Message):
#     await sms.answer(text='https://t.me/Tmtr72')
#
# @dp.message_handler(text='3')
# async def send_sticker(sms:types.Message):
#     stick_id = 'CAACAgIAAxkBAAEMmdBmr1xAW3PuNZ8tSrJzI1HF9jDFBwACxgADMNSdEehWhUGT8OdyNQQ'
#     await bot.send_sticker(
#         chat_id=sms.from_user.id,
#         sticker=stick_id
#     )

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True,on_startup=on_startup)
