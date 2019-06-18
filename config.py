from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Celery configuration
    CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
    CELERY_BACKEND = "db+" + os.getenv('DATABASE_URL')
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'

