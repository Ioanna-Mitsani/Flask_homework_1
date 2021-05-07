from flask import Flask

app = Flask(__name__)

@app.route('/')
def Home():
    return '<h1>Home Page</h1>'


@app.route('/login')
def Login():
    return f'''
    <html>
        <head></head>
        <body>
        <h1>Login Form</h1><br>
        <form>
        <label for="username">Username: </label>
        <input name="username" type="text" /><br>
        <label for="password">Password: </label>
        <input name="password" type="password" /><br>
        </form>
        </body>
    </html>
    '''


@app.route('/logout')
def Logout():
    return '<h3>Ok</h3>'


@app.route('/profile/')
@app.route('/profile/<username>')
def profile(username='darkness'):
    return f'<h1>Hello {username} my old friend</h1>'


if __name__ =='__main__':
  app.run(host='localhost', port=8080, debug=True)