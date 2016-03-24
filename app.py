from flask import Flask, jsonify
from wordsegment import segment

app = Flask(__name__)

@app.route('/split/<word>')
def split(word):
    return jsonify(result=segment(word))

if __name__ == '__main__':
    app.run()
