from flask import Flask

#создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)
app.config['SECRET_KEY'] = '1071falcone'
from app import routes