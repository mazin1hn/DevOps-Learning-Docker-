# app.py

from flask import Flask
import redis
import os #import module for reeading enviroment variables 

redis_host = os.getenv("REDIS_HOST", 'redis') #define said env variables and their defaults 
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_db = int(os.getenv("REDIS_DB", 0))

app = Flask(__name__)

#connect to redis 

redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

@app.route('/')
def welcome_page():
    # Create first route / return welcome message 
     return f'Hello, welcome to my flask web page!'


@app.route('/count')
def count():
    #Create second route /count handles the incremenets  
    visits = redis_client.incr("visits")   # increment and get updated count
    return f'You have visited my website {visits} times!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)