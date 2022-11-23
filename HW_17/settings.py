import os

from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DEBUG = os.getenv('DEBUG')


DIALECT_BD = os.getenv('DIALECT_BD')
USER_BD = os.getenv('USER_BD')
PASSWORD_BD = os.getenv('PASSWORD_BD')
HOST_BD = os.getenv('HOST_BD')
PORT_BD = os.getenv('PORT_BD')
NAME_BD = os.getenv('NAME_BD')




print(HOST)
