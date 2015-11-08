#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Flask"""

from flask import Flask, render_template, request, redirect
import pickle
import re
import os.path


app = Flask(__name__)
filesave = 'todolist.p'
filepath = os.path.isfile(filesave)


if(filepath is True):
	thefile = open(filesave)
	todolist = pickle.load(thefile)
	thefile.close()
else:
	todolist = []


@app.route('/')
def hello_world():
    return render_template('index.html', todolist=todolist)


@app.route('/submit', methods=['POST'])
def submit():

    email = request.form['email']
    task = request.form['task']
    priority = request.form['priority']

    if not re.match('(\w+[.|\w])*@(\w+[.])*\w+', email):
        return redirect('/')
    elif len(task) == 0:
        return redirect('/')
    elif priority not in ('low', 'medium', 'high'):
        return redirect('/')
    else:
        todolist.append((email, task, priority))
        return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    todolist[:] = []
    return redirect('/')


@app.route('/save', methods=['POST'])
def save():
    thefile = open(filesave, 'wb')
    pickle.dump(todolist, thefile)
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete():
    email = request.form['email']
    deltask = request.form['deltask']
    priority = request.form['priority']
    entry = (email, task, priority)
    todolist.remove(entry)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
