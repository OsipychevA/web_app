import random
import uuid

from flask import Flask, render_template, request, redirect, url_for
import json
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/illness')
def illness():
    return render_template('illness.html')


@app.route('/create_new_track', methods=['POST'])
def create_new_track():
    timestamp = str(datetime.datetime.now())
    id_ = create_id()
    track_data = {'id_': id_, 'timestamp': timestamp, 'symptoms': []}
    track_filename = f"track_{id_}.json"

    with open(track_filename, 'w') as track_file:
        json.dump(track_data, track_file)

    return redirect(url_for('input_symptoms', id_=id_))


@app.route('/input_symptoms/<id_>', methods=['GET', 'POST'])
def input_symptoms(id_):
    if request.method == 'POST':
        symptoms_input = request.form.get('symptoms')
        symptoms = [symptom.strip() for symptom in symptoms_input.split(',') if symptom.strip()]

        track_filename = f"track_{id_}.json"

        with open(track_filename, 'r') as track_file:
            track_data = json.load(track_file)

        track_data['symptoms'].extend(symptoms)

        with open(track_filename, 'w') as track_file:
            json.dump(track_data, track_file)

    return render_template('input_symptoms.html', id_=id_)


def create_id() -> str:
    return str(uuid.uuid4())


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)