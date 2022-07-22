from http.client import FOUND
from flask import Flask, render_template, request, session, redirect, flash
from markupsafe import escape
from datetime import datetime
import random 
app = Flask(__name__)
app.secret_key = "secretkey"
@app.route('/')
def gold():
    if 'gold' not in session:
        session['gold'] = 0
    if 'chances' not in session:
        session['chances'] = 5
    if 'found' not in session:
        session['found'] = random.randint(1,100)
    if session['chances'] < 0:
        session.clear()
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

# @app.route('/activities')
# def activities():
#     if 'activities' not in session:
#         session['activities'] = []
#     session['activities'].append(f"You won {session['gold']} ")
#     return redirect('/')



class Activities:
    # Other Burger methods up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_activities(activities):
        is_valid = True # we assume this is true
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        found = random.randint(1,5)
        if request.form['place'] == 'farm' or request.form['place'] == 'cave' or request.form['place'] == 'house':
            flash(f"You earned golds, your total is {session['gold']}, {dt_string}")
            is_valid = False
        if request.form['place'] == 'casino':
            flash(f"You lost golds, your total is {session['gold']}, {dt_string}")
        if session['gold'] == session['found']:
            print("is the number. You Won!")
        return is_valid


@app.route('/process_money', methods=['POST'])
def process_money():
    found = random.randint(1,2)
    if request.form['place'] == 'farm':
        session['gold'] += random.randint(10, 20)
        session['chances'] -= 1
    if request.form['place'] == 'cave':
        session['gold'] += random.randint(5, 10)
        session['chances'] -= 1
    if request.form['place'] == 'house':
        session['gold'] += random.randint(1, 2)
        session['chances'] -= 1
    if request.form['place'] == 'casino':
        session['gold'] -= random.randint(0, 50)
        session['chances'] -= 1
    if not Activities.validate_activities(request.form):
        print(" validation working")
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
