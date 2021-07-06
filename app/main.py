from flask import Flask
app = Flask(__name__)
@app.get('/')
def hello():
    return 'Hello'

@app.get('/index')
def index():
    user = {'username': 'Thai'}
    return '''
    <html>
        <head>
            <title>Home Page - Myblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''


if __name__ == '__main__':
    app.run()
