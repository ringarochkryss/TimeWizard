import os
from flask import Flask, render_template, redirect, request, url_for
import env
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'faq_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', "Env value not loaded")


mongo = PyMongo(app)

@app.route('/')

@app.route('/view_questions')
def view_questions():
    return render_template("view_questions.html", questions=mongo.db.questions.find(),categories=mongo.db.categories.find())

@app.route('/get_questions')
def get_questions():
    return render_template("questions.html", questions=mongo.db.questions.find(),categories=mongo.db.categories.find())

@app.route('/insert_question')
def ask():
    return render_template('ask.html', questions=mongo.db.questions.find(),categories=mongo.db.categories.find())
    
@app.route('/manuals')
def manuals():
    return render_template("manuals.html", categories=mongo.db.categories.find())
    
@app.route('/insert_question', methods=['POST'])
def insert_question():
    questions = mongo.db.questions
    questions.insert_one(request.form.to_dict())
    return redirect(url_for('get_questions'))

@app.route('/edit_question/<question_id>')
def edit_question(question_id):
    the_question =  mongo.db.questions.find_one({"_id": ObjectId(question_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('edit_question.html', question=the_question,
                           categories=all_categories)


@app.route('/update_question/<question_id>', methods=["POST"])
def update_question(question_id):
    questions = mongo.db.questions
    questions.update( {'_id': ObjectId(question_id)},
    {
        'Asked_by':request.form.get('Asked_by'),
        'question':request.form.get('question'),
        'category_name':request.form.get('category_name'),
        'answer': request.form.get('answer'),
        'question_date': request.form.get('question_date'),
        'is_answered':request.form.get('is_answered')
    })
    return redirect(url_for('get_questions'))
    


@app.route('/delete_question/<question_id>')
def delete_question(question_id):
    mongo.db.questions.remove({'_id': ObjectId(question_id)})
    return redirect(url_for('get_questions'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)