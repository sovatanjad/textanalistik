from flask import Flask, render_template, request
from collections import Counter
import math
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.txt'):
            text = file.read().decode('utf-8')
            word_counts = Counter(text.split())
            tf = {word: count / len(word_counts) for word, count in word_counts.items()}
            idf = {word: math.log(1 / (count / len(word_counts))) for word, count in word_counts.items()} 
            results = sorted(tf.items(), key=lambda x: x[1], reverse=True)[:50]
            return render_template('index.html', results=results)
    return render_template('index.html', results=[])

if __name__ == '__main__':
    app.run(debug=True)