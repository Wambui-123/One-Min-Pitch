from flask import Flask, render_template,request
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

@app.route('/', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('index.html')
    return render_template('signup.html', form = form)

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)