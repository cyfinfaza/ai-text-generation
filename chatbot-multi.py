import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing
import numpy as np

one_step_reloaded = tf.saved_model.load('one_step_telegram2')

# def answer(history):
# 	states = None
# 	next_char = tf.constant([history])
# 	# result = [next_char]
# 	while next_char != "⥹":
# 		semiResult = []
# 		while next_char != "\n":
# 			next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
# 			semiResult.append(next_char)
# 		print(semiResult)
# 		if len(semiResult)<1:
# 			continue
# 		yield tf.strings.join(semiResult)[0].numpy().decode("utf-8")
# 	# return tf.strings.join(result)[0].numpy().decode("utf-8")[len(history):]

# history = ""
# while True:
# 	userIn = input('you: ')
# 	history += userIn + "⥹"
# 	answers = answer(history)
# 	for ans in answers:
# 		history += ans + "⥹"
# 		print('bot:', ans)

def answer(history):
	states = None
	next_char = tf.constant([history])
	result = [next_char]

	while next_char != "⥹":
		next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
		result.append(next_char)

	responses = tf.strings.join(result)[0].numpy().decode("utf-8")[len(history):].strip().split("\n")[:-1]
	if len(responses)>0:
		return responses
	else:
		return None

history = ""
while True:
	userIn = input('you: ')
	history += userIn + "⥹"
	answers = answer(history)
	while not answers:
		print('bot: let me think')
		answers = answer(history)
	for ans in answers:
		history += ans
		print('bot:', ans)
	history += "⥹"