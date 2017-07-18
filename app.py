from flask import Flask
from flask_restful import Api
from resources.todo import Todo
from resources.todolist import TodoList

app = Flask(__name__)
api = Api(app)

api.add_resource(Todo, '/Todo', '/Todo/<str:id>')
api.add_resource(TodoList, '/TodoList', '/TodoList/<str:id>')