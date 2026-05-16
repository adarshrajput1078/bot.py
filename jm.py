import telebot
import os

# Yahan apna asli token daalna mat bhulna bhai
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'  
bot = telebot.TeleBot(BOT_TOKEN)

@bot.chat_join_request_handler()
def handle_join_request(message):
    user_id = message.from_user.id
    
    # Aapka exact HTML formatted text message
    text = """⏳ <b>Request mil gayi hai, approval jaldi ho jayega!</b>

👇 Tab tak turant is link se ID banao aur Admin ko message karke verify karwao:

🔗 <b>Game Link:</b> Http://www.sikkimgg.vip/#/register?invitationCode=481415207260
👤 <b>Admin:</b> @Ns_Rocky

🔥 <b>Secret Trick:</b> Game mein bas 3-4 level ka fund maintain karke khelo aur daily apna profit chhapo! 💸"""

    try:
        # 1. Pehle text message bhejega
        bot.send_message(user_id, text, parse_mode="HTML")
        print(f"✅ Text message sent to: {user_id}")
        
        # 2. Ab check karega ki voice file maujood hai ya nahi aur use bhejega
        voice_file_path = 'voice.ogg'
        if os.path.exists(voice_file_path):
            with open(voice_file_path, 'rb') as voice:
                bot.send_voice(user_id, voice)
            print(f"🎙️ Voice note sent to: {user_id}")
        else:
            print(f"⚠️ Warning: '{voice_file_path}' file GitHub/Railway par nahi mili!")
        
    except Exception as e:
        print(f"❌ Error aayi: {e}")

print("🚀 Bot is running on Railway... Aag lagane ke liye taiyaar! 🔥")
bot.infinity_polling()
