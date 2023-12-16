from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = "Your Name"
    age = 25
    return render_template('index.html', name=name, age=age)

@app.route('/father')
def father():
    father_name = "Father's Name"
    father_age = 50
    return render_template('father.html', father_name=father_name, father_age=father_age)

@app.route('/mother')
def mother():
    mother_name = "Mother's Name"
    mother_age = 48
    return render_template('mother.html', mother_name=mother_name, mother_age=mother_age)

@app.route('/friend')
def friend():
    friend_name = "Friend's Name"
    friend_age = 30
    return render_template('friend.html', friend_name=friend_name, friend_age=friend_age)

if __name__ == '__main__':
    app.run(debug=True)
