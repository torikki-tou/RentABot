from enum import Enum


class Database(str, Enum):
    API = 'api'


class Collection(str, Enum):
    USERS = 'users'
    BOTS = 'bots'
