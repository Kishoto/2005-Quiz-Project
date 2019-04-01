from flask import Flask,render_template, request, flash

app = Flask(__name__)

app.secret_key = 'danny'


@app.route('/', methods=['GET', 'POST'])
def index():


    if request.method == 'POST':


        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')


        if not all([username,password,password2]):
            flash('imcomplete')

        elif password != password2:
            flash('not same')
        else:
            return 'success'


    return render_template('login_form.html')


