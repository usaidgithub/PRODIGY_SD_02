import flask
import random
from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin
app=Flask(__name__)
CORS(app)
random_number=random.randint(0,100)
score=0
@app.route('/')
def index():
    return render_template('guess.html')
@app.route('/submit_query',methods=['POST'])
@cross_origin()
def submit_query():
    global score
    if request.method=='POST':
        user_input=int(request.form.get('guess'))
        if(user_input==random_number):
            message=f"You have guessed the correct number on {score+1}th try"
        elif(user_input>random_number):
            message=" Guessed number is greater than the orginal number"
            score=score+1
        else:
            message="Guessed number is smaller than the original number"
            score=score+1
        print(f"The return message is {message}")
        return jsonify({'message':message})
@app.route('/reset_game',methods=["GET"])
@cross_origin()
def reset_game():
    global random_number
    global score
    if request.method=="GET":
        random_number=int(random.randint(0,100))
        score=0
        return jsonify({'message':"game reset successfuuly"})


if(__name__=='__main__'):
    app.run(debug=True,port=3000)