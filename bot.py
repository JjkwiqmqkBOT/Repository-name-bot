import telebot, os, time, yt_dlp
from deep_translator import GoogleTranslator
TOKEN="8837004327:AAFXhbeYtObuzmHmv0tZCcwtni3d0NFv3Q4"
bot=telebot.TeleBot(TOKEN, threaded=True)
@bot.message_handler(commands=['start'])
def s(m): bot.send_message(m.chat.id,"البوت شغال 24 ساعة 🔥")
@bot.message_handler(func=lambda m:True)
def all(m):
    try:
        t=m.text
        if "tiktok.com" in t or "vm.tiktok" in t:
            bot.reply_to(m,"⏳ جاري التحميل...")
            ydl_opts={'outtmpl':'v.mp4','quiet':True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([t])
            bot.send_video(m.chat.id, open('v.mp4','rb'))
            os.remove('v.mp4')
        else:
            tr=GoogleTranslator(source='auto', target='ar').translate(t)
            bot.reply_to(m,tr)
    except Exception as e: bot.reply_to(m,str(e))
while True:
    try: bot.infinity_polling()
    except: time.sleep(5)
