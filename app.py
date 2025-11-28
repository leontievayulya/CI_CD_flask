from flask import Flask, render_template, request


app=Flask(__name__)

@app.route("/")
@app.route('/index')
def say_hello():
    return render_template('home.html')

@app.route('/user/<username>')
def show_user(username):
    return f'hello, {username}'


@app.route('/post<int:post_id>')
def show_post(post_id):
    return f'post number {post_id}'


@app.route('/add', methods=['GET'])
def add():
    try:
        a=float(request.args.get('a'))
        b=float(request.args.get('b'))
    except (TypeError, ValueError):
        return 'a и b - числа'
    return str(a+b)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        return f'попытка входа {username}'
    else:
        return """"
            <form method="post">
                Логин: <input name="username"><br>
                Пароль: <input name="password" type="password"><br>
                <buttom type="submit">Войти</buttom>
            </form>
        """



if __name__=='__main__':
    app.run()