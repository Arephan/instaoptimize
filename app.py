from flask import Flask, render_template, request
from instagram import find_optimal_tag

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        tags = request.form['tags'].split(' ')
        tags = find_optimal_tag(tags)
        return render_template('index.html', tags=tags)
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)