import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token - Replace with your actual bot token
BOT_TOKEN = "7899289311:AAFXua2OsZu1qO0o4sqy3ye70e7n2bq9W6M"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send welcome message with inline keyboard when /start is used."""
    
    welcome_message = """🎯 Welcome to ProfileBot!

Your personal CV creation assistant is here to help you build a professional resume in minutes.

✨ What I can do for you:
• Create a stunning CV tailored to your career
• Guide you through each section step-by-step  
• Generate a professional PDF ready for employers
• Save your progress and update anytime

Ready to build your dream CV? Let's get started! 🚀

Use /help to see all available commands."""
    
    # Create inline keyboard with buttons side by side
    keyboard = [
        [InlineKeyboardButton("🚀 Start CV", callback_data='start_cv'),
         InlineKeyboardButton("📋 Help", callback_data='help')],
        [InlineKeyboardButton("🔄 New Session", callback_data='new_session')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send help message with inline keyboard when /help is used."""
    
    help_message = """📋 ProfileBot Help Center

Available Commands:
/start - Begin creating your CV or start fresh
/help - Show this help message

🔧 How it works:
1. Use /start to begin your CV creation journey
2. I'll guide you through each section:
   • Personal Information
   • Professional Summary
   • Work Experience
   • Education
   • Skills
   • Additional sections (optional)
3. Review and download your professional CV

💡 Tips:
• Take your time with each section
• Be specific about your achievements
• Use action words to describe your experience

Need support? Contact our team for assistance!"""
    
    # Create inline keyboard for help with horizontal layout
    keyboard = [
        [InlineKeyboardButton("🚀 Start CV", callback_data='start_cv'),
         InlineKeyboardButton("🏠 Main Menu", callback_data='main_menu')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        help_message,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button callbacks."""
    query = update.callback_query
    await query.answer()
    
    if query.data == 'start_cv':
        # This will be where CV creation starts
        await query.edit_message_text(
            text="🎯 Great! Let's create your professional CV.\n\n"
                 "First, I'll need some basic information about you.\n\n"
                 "Click 'Begin' when you're ready to start!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ Begin CV Creation", callback_data='begin_cv')],
                [InlineKeyboardButton("🏠 Back to Main Menu", callback_data='main_menu')]
            ])
        )
    
    elif query.data == 'help':
        help_message = """📋 ProfileBot Help Center

Available Commands:
/start - Begin creating your CV or start fresh
/help - Show this help message

🔧 How it works:
1. Use /start to begin your CV creation journey
2. I'll guide you through each section:
   • Personal Information
   • Professional Summary
   • Work Experience
   • Education
   • Skills
   • Additional sections (optional)
3. Review and download your professional CV

💡 Tips:
• Take your time with each section
• Be specific about your achievements
• Use action words to describe your experience

Need support? Contact our team for assistance!"""
        
        await query.edit_message_text(
            text=help_message,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🚀 Start Creating CV", callback_data='start_cv')],
                [InlineKeyboardButton("🏠 Back to Main Menu", callback_data='main_menu')]
            ])
        )
    
    elif query.data == 'new_session':
        await query.edit_message_text(
            text="🔄 Starting a new session...\n\n"
                 "Your previous progress will be cleared. Are you sure you want to continue?",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ Yes, Start Fresh", callback_data='confirm_new')],
                [InlineKeyboardButton("❌ Cancel", callback_data='main_menu')]
            ])
        )
    
    elif query.data == 'confirm_new':
        # Clear user data and start fresh
        context.user_data.clear()
        await query.edit_message_text(
            text="✅ New session started! All previous data cleared.\n\n"
                 "Ready to create your CV from scratch?",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🚀 Start Creating CV", callback_data='start_cv')],
                [InlineKeyboardButton("🏠 Back to Main Menu", callback_data='main_menu')]
            ])
        )
    
    elif query.data == 'main_menu':
        # Return to main menu
        welcome_message = """🎯 Welcome to ProfileBot!

Your personal CV creation assistant is here to help you build a professional resume in minutes.

✨ What I can do for you:
• Create a stunning CV tailored to your career
• Guide you through each section step-by-step  
• Generate a professional PDF ready for employers
• Save your progress and update anytime

Ready to build your dream CV? Let's get started! 🚀

Use /help to see all available commands."""
        
        keyboard = [
            [InlineKeyboardButton("🚀 Start CV", callback_data='start_cv'),
             InlineKeyboardButton("📋 Help", callback_data='help')],
            [InlineKeyboardButton("🔄 New Session", callback_data='new_session')]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text=welcome_message,
            reply_markup=reply_markup
        )
    
    elif query.data == 'begin_cv':
        # This is where we'll start the CV creation process
        await query.edit_message_text(
            text="🚧 CV Creation process will be implemented here!\n\n"
                 "This is where we'll start collecting user information.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Back to Main Menu", callback_data='main_menu')]
            ])
        )

def main() -> None:
    """Start the bot."""
    print("🤖 ProfileBot is starting...")
    print("💫 Initializing flow-based CV creation bot...")
    
    try:
        # Create the Application
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Add command handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        
        # Add callback query handler for buttons
        application.add_handler(CallbackQueryHandler(button_callback))
        
        print("✅ Bot initialized successfully!")
        print("✨ Try sending /start to your bot in Telegram")
        print("🔍 Search for your bot using the username from BotFather")  
        print("Press Ctrl+C to stop the bot")
        print("-" * 50)
        
        # Run the bot until the user presses Ctrl-C
        application.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        print("Check your bot token and internet connection")

if __name__ == '__main__':
    main()