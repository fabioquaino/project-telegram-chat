# Telegram Chat with Sentiment Analysis in Jupyter Notebook (Spanish)
This project seamlessly integrates a Telegram bot using the telebot library, incorporating sentiment analysis through the sentiment_analysis.SentimentAnalysisSpanish() class. Messages received by the bot are processed to extract relevant information, including message ID, chat ID, text content, and user details. The sentiment analysis feature evaluates the sentiment of the message content, and the results, along with other message details, are stored in a MySQL database. Configuration parameters, such as the Telegram token, bot name, and database credentials, are set up through a ConfigParser reading values from a conexiones.properties file.

## Usage Instructions

1. Clone this repository to your development environment.
2. Modify the files according to your specific requirements.
3. Use Docker Compose to deploy and manage the services.

```bash
docker-compose up -d
```

## Docker Compose Configuration

The project uses Docker Compose to deploy a Jupyter Notebook environment with machine learning libraries and a Telegram bot API.

```yaml
version: '1.0'

services:
  python-notebook:
    image: quaino/jupyter-notebook-ml:1.0
    build:
      context: .
    volumes:
      - ./Ejecutables:/home/jovyan/work # Se deben agregar los archivos .properties a la carpeta Ejecutables/Local
    ports:
      - "8888:8888"
    #Uncomment the following line if you want the Clasificador.ipynb to run at Jupyter startup
    #command: jupyter nbconvert --to script --execute --ExecutePreprocessor.timeout=-1 Clasificador.ipynb && python Clasificador.py
```

## Code Overview

The Python code integrates a Telegram bot to handle messages, extract information, and classify text using a machine learning model. Messages are stored in a MySQL database.

### Configuration and Context Access
```yaml
# Create a ConfigParser object and read the conexiones.properties file
config = configparser.ConfigParser()
config.read('Local/conexiones.properties')

# Access context values
TELEGRAM_TOKEN = config.get('PRUEBA', 'TELEGRAM_TOKEN')
TELEGRAM_BOT_NAME = config.get('PRUEBA', 'TELEGRAM_BOT_NAME')
# ... (other context values)
```
### Database Connection and Message Storage
```yaml
def load_message_db(id_mensaje, id_chat, texto, usuario, fecha_hora, clasificacion):
    # Database connection logic...
    # Insert message into the database...
```
### Message Handler
```yaml
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    # Message handling logic...
    clasificacion = analize_text(text)
    load_message_db(message_id, chat_id, text, user_info, date, clasificacion)
```

The project utilizes Docker to provide a reproducible and isolated environment for running the Jupyter Notebook and the Telegram bot. Additionally, it leverages MySQL for message storage and configuration via a properties file.

Feel free to adjust or expand the summary based on additional details you may want to include.