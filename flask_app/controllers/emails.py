from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def intake():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect("/display")


@app.route('/display')
def display():
    return render_template('success.html', emails=Email.get_all())

@app.route('/destroy/<int:id>')
def delete_email(id):
    data = {
        "id" : id
    }
    Email.destroy(data)
    return redirect("/display")

