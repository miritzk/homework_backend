from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/home_page")
def home_page():
    return redirect(url_for('index_page'))

@app.route("/professional")
def professional_page():
    return render_template('cv.html')

@app.route("/cv")
def cv_page():
    return redirect('/professional')

@app.route("/successful_contact")
def successful_contact_page():
    return render_template('successful_contact.html')

@app.route("/assignment8")
def assignment8_page():
    name = 'Mirit'
    last_name = 'Zelichonok'
    return render_template('assignment8.html',
                           name=name,
                           last_name=last_name,
                           profile={'Favorite hobbie': 'Netflix',
                                    'Favorite music': 'Ariana Grande',
                                    'Favorite place': 'The beach'})


if __name__ == '__main__':
    app.run(debug=True)

