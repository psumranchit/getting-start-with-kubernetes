from flask import Flask
import redis
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/query/<key>")
def list(key):
    r = redis.Redis(host='redis-service', port=6379, db=0)
    return r.get(key)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')