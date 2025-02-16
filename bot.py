from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Replace this with your actual bot token
TOKEN = "YOUR_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🍔 Order Now", callback_data="order_now")],
        [InlineKeyboardButton("📜 Credits", callback_data="credits")],
        [InlineKeyboardButton("🆘 Support", callback_data="support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 Welcome! Tap below to place an order:",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "credits":
        await query.edit_message_text("📜 This bot was developed by *Your Name*.", parse_mode="Markdown")
    elif query.data == "support":
        await query.edit_message_text("🆘 For support, contact *support@example.com*", parse_mode="Markdown")
    else:
        await query.edit_message_text("⚠ Unknown option selected.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
