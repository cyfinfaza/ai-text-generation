import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing
import numpy as np
from flask import Flask, request
from flask_cors import CORS

one_step_reloaded = tf.saved_model.load('one_step_telegram')

app = Flask(__name__)
cors = CORS(app)

def answer(history):
	states = None
	next_char = tf.constant([history])
	result = [next_char]

	while next_char != "\n":
	# for i in range(1):
		next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
		result.append(next_char)

	return tf.strings.join(result)[0].numpy().decode("utf-8")[len(history):]

@app.route('/')
def index():
	return 'Index Page'

@app.route('/predict', methods=['POST'])
def predict():
	data = request.get_data().decode('utf-8')
	return answer(data)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5004, debug=True, threaded=True)