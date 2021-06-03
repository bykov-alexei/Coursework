from app import app
from app.database import connect
from app.utils import get_embedding

from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO
import os
import base64
from flask import request, jsonify, render_template, send_from_directory, redirect
import numpy as np


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/camera', methods=['post'])
def add_camera():
    title = request.form.get('title')
    x = request.form.get('x')
    y = request.form.get('y')
    rstp = request.form.get('rstp')
    F = request.form.get('F')
    F = F if len(F) else None
    conn, cursor = connect()
    query = "INSERT INTO cameras (title, x, y, rstp, F) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (title, x, y, rstp, F))
    conn.commit()
    conn.close()
    return redirect('/cameras/page')


@app.route('/cameras', methods=['get'])
def get_all_cameras():
    conn, cursor = connect()
    query = "SELECT title, x, y, rstp, F, current_frame FROM cameras"
    cursor.execute(query)
    conn.close()
    return jsonify(list(cursor.fetchall())) 

@app.route('/camera/<int:id>', methods=['get'])
def get_camera(id: int):
    conn, cursor = connect()
    query = "SELECT title, x, y, rstp, F FROM cameras WHERE id = %s"
    cursor.execute(query, (id,))
    conn.close()
    return jsonify(cursor.fetchone())

@app.route('/plan', methods=['post'])
def add_building_plan():
    file = request.files['file']
    file.save(os.path.join('../images', 'plan.png'))
    return redirect('/cameras/page')


@app.route('/person', methods=['post'])
def add_person():
    file = request.files['file']
    name = request.form.get('name')
    image = np.array(Image.open(BytesIO(file.read())))
    embedding = get_embedding(image)
    if embedding is not None:
        conn, cursor = connect()
        query = f"INSERT INTO known_persons (name, picture, {', '.join(['e%i' % i for i in range(1, 129)])}) "\
                f"VALUES (%s, %s, {','.join(['%s' for i in range(128)])})"
        cursor.execute(query, (name, os.path.join('known_persons', file.filename), *embedding))
        conn.commit()
        conn.close()
        plt.imsave(os.path.join('../images/known_persons', file.filename), image)
        return redirect("/people/page")
    else:
        return "", 400


@app.route('/persons', methods=['get'])
def get_all_persons():
    conn, cursor = connect()
    query = "SELECT * FROM known_persons"
    cursor.execute(query)
    conn.close()
    return jsonify(list(cursor.fetchall())) 

@app.route('/person/<int:id>', methods=['get'])
def get_specific_person(id: int):
    conn, cursor = connect()
    query = "SELECT * FROM known_persons WHERE id = %s"
    cursor.execute(query, (id,))
    conn.close()
    return jsonify(cursor.fetchone())   
    
@app.route('/person/<int:id>/page', methods=['get'])
def get_specific_person_page(id: int):
    conn, cursor = connect()
    query = "SELECT * FROM known_persons WHERE id = %s"
    cursor.execute(query, (id,))
    person = cursor.fetchone()
    conn.close()
    return render_template('person.html', person=person)

@app.route('/person/<int:id>/delete', methods=['get'])
def delete_person(id: int):
    conn, cursor = connect()
    query = "DELETE FROM known_persons WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()
    return redirect('/people/page')  

@app.route('/cameras/page')
def cameras():
    conn, cursor = connect()
    query = "SELECT title, x, y, rstp, F, current_frame FROM cameras"
    cursor.execute(query)
    conn.close()

    return render_template('cameras.html', cameras=cursor.fetchall())

@app.route('/people/page')
def page():
    conn, cursor = connect()
    query = "SELECT * FROM known_persons"
    cursor.execute(query)
    conn.close()

    return render_template('people.html', people=cursor.fetchall())