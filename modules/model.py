#!/usr/bin/env python3
""" Class representing an AI Model.

Represents an AI Model. AI Models are used by classifiers to process
incoming data.

MIT License

Copyright (c) 2021 Asociación de Investigacion en Inteligencia Artificial
Para la Leucemia Peter Moss

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files(the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contributors:

"""

from modules.AbstractModel import AbstractModel


class model(AbstractModel):
	""" Class representing an AI Model.

	Represents an AI Model. AI Models are used by classifiers
	to process incoming data.
	"""

	def prepare_data(self):
		""" Creates/sorts dataset. """
		pass

	def prepare_network(self):
		""" Builds the network. """
		pass

	def train(self):
		""" Trains the model

		Compiles and fits the model.
		"""
		pass

	def save_model_as_json(self):
		""" Saves the model as JSON """
		pass

	def save_weights(self):
		""" Saves the model weights """
		pass

	def predictions(self):
		""" Gets a prediction for an image. """
		pass

	def evaluate(self):
		""" Evaluates the model """
		pass

	def plot_accuracy(self):
		""" Plots the accuracy. """
		pass

	def plot_loss(self):
		""" Plots the loss. """
		pass

	def plot_auc(self):
		""" Plots the AUC. """
		pass

	def plot_precision(self):
		""" Plots the precision. """
		pass

	def plot_recall(self):
		""" Plots the recall. """
		pass

	def confusion_matrix(self):
		""" Plots the confusion matrix. """
		pass

	def figures_of_merit(self):
		""" Calculates/prints the figures of merit.

		https://homes.di.unimi.it/scotti/all/
		"""
		pass

	def load(self):
		""" Loads the model """
		pass

	def predict(self, img):
		""" Gets a prediction for an image. """
		pass

	def reshape(self, img):
		""" Reshapes an image. """
		pass

	def test(self):
		""" Test mode

		Loops through the test directory and classifies the images.
		"""
		pass

	def http_reshape(self, img):
		""" Classifies an image sent via HTTP. """
		pass

		return processed

	def http_request(self, img_path):
		""" Sends image to the inference API endpoint. """
		pass

	def test_http(self):
		"""Server test mode

		Loops through the test directory and sends the images to the
		classification server.
		"""
		pass
