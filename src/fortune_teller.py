from flask import Flask, render_template
import random
from fortune_messages import fortune_messages

app = Flask(__name__)

@app.route('/')
def fortune_teller():
    random_message = random.choice(fortune_messages)
    return render_template('fortune.html', random_message=random_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
