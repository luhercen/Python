#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final project is211 Blog"""


import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE='finalpostsdatabase.db',
    DEBUG=True,
    SECRET_KEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT',
    USERNAME='admin',
    PASSWORD='admin'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():

    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():

    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.teardown_appcontext
def close_db(error):

    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('SELECT id, title,text FROM entries ORDER BY id DESC')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('INSERT INTO entries(title,text) VALUES (?,?)', [request.form['title'], request.form['text']])
    db.commit()
    flash('Your new entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/edit', methods=['GET','POST'])
def edit():
    if not session.get('logged_in'):
        abort(401)
    id = request.args.get('id')
    sql = 'select id, title, text from entries where id= ?'
    db = get_db()
    cur = db.execute(sql,(id,))
    rows = [dict(id=r[0], title=r[1], text=r[2]) for r in cur.fetchall()]
    row =rows[0]
    index = row['text'].find('<br>')
    if index>=0:
        row['text'] = row['text'].replace('<br>','\r\n')
    return render_template('edit.html', row = row)


@app.route('/edit_post', methods=['POST'])
def edit_post():
    
    text = request.form['text']
    text = text.replace('\r\n','<br>')
    sql = 'update entries set title=\'' + request.form['title'] + '\', text=\'' + text + '\' where id=\'' + request.form['id'] + '\'' 
    db = get_db()
    db.execute(sql)
    db.commit()

    flash('The post was successfully edited')
    return redirect(url_for('show_entries'))


@app.route('/delete', methods = ['GET'])
def delete_entry():
    if not session.get('logged_in'):
        abort(401)
    id = request.args.get('id')
    sql = 'DELETE FROM entries WHERE ID = ?'
    db = get_db()
    db.execute(sql,(id,))
    db.commit()
    flash("Your post was succesfully deleted:")
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
