# Usa una imagen base de Python
FROM python:3.8

# Instala las librerías necesarias
RUN pip install notebook \
    pyTelegramBotAPI \
    mysql-connector-python \
    configparser \
    sentiment-analysis-spanish \
    keras \
    tensorflow \
    scikit-learn \
    pandas \
    numpy

# Establece un directorio de trabajo
WORKDIR /home/jovyan/work

# Comando por defecto para iniciar Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''"]
