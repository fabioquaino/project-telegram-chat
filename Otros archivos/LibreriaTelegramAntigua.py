from telegram.ext import Updater, MessageHandler, Filters

def handle_messages(update, context):
    message = update.message
    text = message.text
    print(f"Nuevo mensaje: {text}")

def main():
    # Reemplaza 'TU_TOKEN' con el token que obtuviste del BotFather
    TOKEN = 'TU_TOKEN'

    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # Manejador para capturar mensajes de texto en cualquier chat
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_messages))

    # Inicia el bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
