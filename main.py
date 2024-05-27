from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# استبدل 'YOUR_TOKEN_HERE' بالتوكن الخاص بتيليجرام بوت
TOKEN = '6839038529:AAHpjGbxIyzR3RxkCjU00wnKV5_0qHQvKL0'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴠɪᴀᴛᴏʀ ᴘʀᴇᴅɪᴄᴛᴏʀ ᴀɴᴅ ᴄʀᴀꜱʜ ʙᴏᴛ\n\n📈 ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ꜰᴏʀ ᴀɴʏ ᴀᴍᴏᴜɴᴛ 100% ʜɪɢʜ ᴀᴄᴄᴜʀᴀᴄʏ ᴘʀᴇᴅɪᴄᴛɪᴏɴꜱ\n\n✴️ ᴀᴠɪᴀᴛᴏʀ ᴘʀᴇᴅɪᴄᴛᴏʀ ɪꜱ ᴀ ᴛᴏᴏʟ ᴅᴇꜱɪɢɴᴇᴅ ᴛᴏ ᴘʀᴇᴅɪᴄᴛ ᴍᴜʟᴛɪᴘʟɪᴇʀꜱ ɪɴ ᴛʜᴇ ʙᴇᴛᴛɪɴɢ ɢᴀᴍᴇ ᴀᴠɪᴀᴛᴏʀ, ʜᴇʟᴘɪɴɢ ᴘʟᴀʏᴇʀꜱ ꜱᴇᴄᴜʀᴇ ᴛʜᴇɪʀ ᴡɪɴɴɪɴɢꜱ.')
    keyboard = [
        [
            InlineKeyboardButton("𝘈𝘭𝘨𝘦𝘳𝘪𝘢", callback_data='algeria'),
            InlineKeyboardButton("𝘔𝘰𝘳𝘰𝘤𝘤𝘰", callback_data='morocco'),
            InlineKeyboardButton("𝘛𝘶𝘯𝘪𝘴𝘪𝘢", callback_data='tunisia')
        ],
        [
            InlineKeyboardButton("𝘌𝘨𝘺𝘱𝘵", callback_data='egypt'),
            InlineKeyboardButton("𝘔𝘢𝘶𝘳𝘪𝘵𝘢𝘯𝘪𝘢", callback_data='mauritania'),
            InlineKeyboardButton("𝘚𝘢𝘶𝘥𝘪 𝘈𝘳𝘢𝘣𝘪𝘢", callback_data='saudi_arabia')
        ],
        [
            InlineKeyboardButton("𝘉𝘳𝘢𝘻𝘪𝘭", callback_data='brazil'),
            InlineKeyboardButton("𝘈𝘧𝘳𝘪𝘤𝘢", callback_data='africa'),
            InlineKeyboardButton("𝘚𝘸𝘦𝘥𝘦𝘯", callback_data='sweden')
        ],
        [
            InlineKeyboardButton("𝘍𝘳𝘢𝘯𝘤𝘦", callback_data='france')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('ᴄʜᴏᴏꜱᴇ ᴀ ᴄᴏᴜɴᴛʀʏ:', reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data in ['algeria', 'morocco', 'tunisia', 'egypt', 'mauritania', 'saudi_arabia', 'brazil', 'africa', 'sweden', 'france']:
        keyboard = [
            [
                InlineKeyboardButton("𝟷𝘹𝘣𝘦𝘵", callback_data=f'{query.data}_1xbet'),
                InlineKeyboardButton("𝘮𝘦𝘭𝘣𝘦𝘵", callback_data=f'{query.data}_melbet'),
                InlineKeyboardButton("𝘭𝘪𝘯𝘦𝘣𝘦𝘵", callback_data=f'{query.data}_linebet'),
                InlineKeyboardButton("𝘣𝘦𝘵𝘸𝘪𝘯𝘯𝘦𝘳", callback_data=f'{query.data}_betwinner')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f"You chose {query.data}. Choose an option:", reply_markup=reply_markup)
    elif any(query.data.endswith(suffix) for suffix in ['_1xbet', '_melbet', '_linebet', '_betwinner']):
        keyboard = [
            [
                InlineKeyboardButton("𝙽𝙴𝚆 𝚁𝙾𝚄𝙽𝙳𝙴 😈", callback_data='new_round_1')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f"You chose {query.data}. Press 𝙽𝙴𝚆 𝚁𝙾𝚄𝙽𝙳𝙴 😈 to continue.", reply_markup=reply_markup)
    elif query.data.startswith('new_round'):
        round_number = int(query.data.split('_')[-1])
        if round_number == 1:
            next_text = "𝟭𝟳.𝟳𝟱𝘅"
            next_round = 2
        elif round_number == 2:
            next_text = "𝟭.𝟬𝟰𝘅"
            next_round = 3
        elif round_number == 3:
            next_text = "𝟭.𝟴𝟰𝘅"
            next_round = 4
        elif round_number == 4:
            next_text = "𝟯.𝟳𝟬𝘅"
            next_round = 5
        elif round_number == 5:
            next_text = "𝟭.𝟭𝟱𝘅"
            next_round = 6
        elif round_number == 6:
            next_text = "𝟭.𝟯𝟬𝘅"
            next_round = None
        else:
            next_text = "End of rounds."
            next_round = None

        keyboard = [
            [
                InlineKeyboardButton("𝙽𝙴𝚆 𝚁𝙾𝚄𝙽𝙳𝙴 😈", callback_data='new_round')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="اتصل بالمسؤول للحصول على صلاحية الروبوت\n𝘊𝘰𝘯𝘵𝘢𝘤𝘵 𝘈𝘥𝘮𝘪𝘯 𝘮𝘦 𝘨𝘦𝘵 𝘣𝘰𝘵 𝘷𝘢𝘭𝘪𝘥𝘪𝘵𝘺\n\n@ivetv", reply_markup=reply_markup)

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    application.run_polling()

if __name__ == '__main__':
    main()
