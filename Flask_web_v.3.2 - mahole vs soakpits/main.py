import os
from app import app
import urllib.request
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for, render_template
import requests
import json
import shutil
from PIL import Image

ALLOWED_EXTENSIONS = set(['jpg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
	if 'files[]' not in request.files:
		flash('No file part')
		return redirect(request.url)
	url = 'http://127.0.0.1:5000/im_size'
	files = request.files.getlist('files[]')
	file_names = []
	filenames_ = []
	results = []
	probs = []
	for file in files:
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			print(filename)
			file_names.append(filename)
			file.save(filename)
			shutil.copy(filename, 'static/uploads/')

	for x in file_names:
		print(x)
		my_img = {'image': open(x, 'rb')}
		r = requests.post(url, files=my_img)
		print(r.json())
		results.append(r.json()['Class'][0])
		probs.append(r.json()['Confidence'][0])

	y = len(results)
	print(file_names)
	for x in file_names:
		z = os.path.join("static/uploads/",x)
		filenames_.append(z)
	print(filenames_)
	return render_template('upload.html', filenames=filenames_,len_=y ,output=results,prob = probs)

@app.route("/display/<filename>")
def display_image(filename):
	print('display_image filename: ' + filename)
	return redirect(url_for(filename), code=301)

if __name__ == "__main__":
    app.run(port=4000)