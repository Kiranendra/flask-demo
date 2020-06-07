from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    username = ""
    email = ""
    password = ""
    if request.method == 'POST' and 'userEmail' in request.form and 'userPass' in request.form:
        email = request.form.get('userEmail')
        password = request.form.get('userPass')
        with open('./data/data.txt') as file:
            for line in file.readlines():
                data = line.split(':')
                if data[1] == email and data[2].strip() == password:
                    username = data[0]
                del data
                del line
            file.close()
    return render_template('login.html', username=username)

@app.route('/register', methods=['GET', 'POST'])
def registerPage():
    name = ""
    email = ""
    password = ""
    if request.method == "POST" and 'userName' in request.form and 'userEmail' in request.form and 'userPass' in request.form:
        name = request.form.get('userName')
        email = request.form.get('userEmail')
        password = request.form.get('userPass')
        with open('./data/data.txt', 'a') as file:
            line = name + ":" + email + ":" + password + "\n"
            file.write(line)
            del line
            file.close()
        return redirect(url_for('homePage'))
    return render_template('register.html')

app.run(debug=True)
