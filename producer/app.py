from flask import Flask

app = Flask(__name__)

# Configurações de Módulos
import config

# Views
# TODO: Adicionar abaixo todas as views existentes na pasta 'views', usando a sintaxe abaixo.
import views.usuario

if __name__ == '__main__':
    app.run()
