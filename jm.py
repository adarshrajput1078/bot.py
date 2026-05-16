import telebot
import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

# 👉 Render Port Bind Fix Trick 👈
def keep_alive():
    port = int(os.environ.get('PORT', 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=keep_alive, daemon=True).start()


# 🎫 Yahan aapka demo token fit kar diya hai
BOT_TOKEN = '8928404549:AAEIDWFYDQ76v388cbUB42xjtgepejWLqYE'  
bot = telebot.TeleBot(BOT_TOKEN)

@bot.chat_join_request_handler()
def handle_join_request(message):
    user_id = message.from_user.id
    
    text = """⏳ <b>Request mil gayi hai, approval jaldi ho jayega!</b>

👇 Tab tak turant is link se ID banao aur Admin ko message karke verify karwao:

🔗 <b>Game Link:</b> Http://www.sikkimgg.vip/#/register?invitationCode=481415207260
👤 <b>Admin:</b> @Ns_Rocky

🔥 <b>Secret Trick:</b> Game mein bas 3-4 level ka fund maintain karke khelo aur daily apna profit chhapo! 💸"""

    try:
        # 1. Text message bhejega
        bot.send_message(user_id, text, parse_mode="HTML")
        print(f"✅ Text message sent to: {user_id}")
        
        # 2. Voice note bhejega
        voice_file_path = 'voice.ogg'
        if os.path.exists(voice_file_path):
            with open(voice_file_path, 'rb') as voice:
                bot.send_voice(user_id, voice)
            print(f"🎙️ Voice note sent to: {user_id}")
        else:
            print(f"⚠️ Warning: '{voice_file_path}' file nahi mili!")
        
    except Exception as e:
        print(f"❌ Error aayi: {e}")

print("🚀 Bot is running with Demo Token... Aag lagane ke liye taiyaar! 🔥")
bot.infinity_polling()
        
