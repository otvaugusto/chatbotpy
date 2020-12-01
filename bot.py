"""
    Faculdade de Americana - Ciência da Computação
                Gabriel Lira © 2019
"""

import os
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Declaração do bot
bot = ChatBot('Fion')
treinador = ListTrainer(bot)

#Leitura do arquivo com as perguntas e respostas
for conversa in os.listdir('base'):
    bot_memoria = open('base/'+ conversa, 'r').readlines()
    treinador.train(bot_memoria)

app = Flask(__name__)

#Rota para a página inicial
@app.route('/home')
def index():
    return render_template('index.html')

#Retorna o mesmo template da página inicial porém no método POST com a interação entre usuário e bot
@app.route('/resposta', methods=['POST'])
def resposta():
    user_input = request.form['user_input']

    bot_response = bot.get_response(user_input)
    bot_response = str(bot_response)
    return render_template('index.html', user_input=user_input, bot_response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)
