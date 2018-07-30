from flask import Flask, render_template, request, redirect, url_for

import numpy as np
import os
from PIL import Image


#-------------------------------------------#

image_dir = 'static/image/'
data_count = 151
random_number = []

#-------------------------------------------#

app = Flask(__name__)

for i in range(0, 20):
	number = np.random.randint(data_count)
	random_number.append(number)


def get_path_random():
	img_paths = []
	return_paths = []
	return_pokemon_names = []

	file_names = os.listdir(image_dir)
	file_names.sort()

	for file_name in file_names:
		abs_name = image_dir + file_name
		img_paths.append(abs_name)

	for i in random_number:
		img_path = img_paths[i]
		pokemon_name, extension = os.path.splitext(os.path.basename(img_path))

		return_paths.append(img_path)
		return_pokemon_names.append(pokemon_name)

	return return_paths, return_pokemon_names


@app.route('/')
def index():
	title = "ポケモンシルエットクイズ"
	img_paths, pokemon_names = get_path_random()

	return render_template('index.html', title=title, img_path1=img_paths[0], img_path2=img_paths[1], img_path3=img_paths[2], img_path4=img_paths[3], img_path5=img_paths[4], img_path6=img_paths[5], img_path7=img_paths[6], img_path8=img_paths[7], img_path9=img_paths[8], img_path10=img_paths[9], img_path11=img_paths[10], img_path12=img_paths[11], img_path13=img_paths[12], img_path14=img_paths[13], img_path15=img_paths[14], img_path16=img_paths[15], img_path17=img_paths[16], img_path18=img_paths[17], img_path19=img_paths[18], img_path20=img_paths[19])


@app.route('/post', methods=['GET', 'POST'])
def post():
	title = "ポケモンシルエットクイズ-結果-"
	point = 0
	ansers = []

	if request.method == 'POST':
		anser1 = request.form['anser1']
		ansers.append(anser1)
		anser2 = request.form['anser2']
		ansers.append(anser2)
		anser3 = request.form['anser3']
		ansers.append(anser3)
		anser4 = request.form['anser4']
		ansers.append(anser4)
		anser5 = request.form['anser5']
		ansers.append(anser5)
		anser6 = request.form['anser6']
		ansers.append(anser6)
		anser7 = request.form['anser7']
		ansers.append(anser7)
		anser8 = request.form['anser8']
		ansers.append(anser8)
		anser9 = request.form['anser9']
		ansers.append(anser9)
		anser10 = request.form['anser10']
		ansers.append(anser10)
		anser11 = request.form['anser11']
		ansers.append(anser11)
		anser12 = request.form['anser12']
		ansers.append(anser12)
		anser13 = request.form['anser13']
		ansers.append(anser13)
		anser14 = request.form['anser14']
		ansers.append(anser14)
		anser15 = request.form['anser15']
		ansers.append(anser15)
		anser16 = request.form['anser16']
		ansers.append(anser16)
		anser17 = request.form['anser17']
		ansers.append(anser17)
		anser18 = request.form['anser18']
		ansers.append(anser18)
		anser19 = request.form['anser19']
		ansers.append(anser19)
		anser20 = request.form['anser20']
		ansers.append(anser20)

		img_paths, pokemon_names = get_path_random()

		for i in range(0, len(pokemon_names)):
			if ansers[i] == pokemon_names[i]:
				point += 1

		accuracy = point / len(pokemon_names) * 100

		return render_template('index.html', title=title, point=accuracy, anser1=anser1, anser2=anser2, anser3=anser3, anser4=anser4, anser5=anser5, anser6=anser6, anser7=anser7, anser8=anser8, anser9=anser9, anser10=anser10, anser11=anser11, anser12=anser12, anser13=anser13, anser14=anser14, anser15=anser15, anser16=anser16, anser17=anser17, anser18=anser18, anser19=anser19, anser20=anser20, img_path1=img_paths[0], img_path2=img_paths[1], img_path3=img_paths[2], img_path4=img_paths[3], img_path5=img_paths[4], img_path6=img_paths[5], img_path7=img_paths[6], img_path8=img_paths[7], img_path9=img_paths[8], img_path10=img_paths[9], img_path11=img_paths[10], img_path12=img_paths[11], img_path13=img_paths[12], img_path14=img_paths[13], img_path15=img_paths[14], img_path16=img_paths[15], img_path17=img_paths[16], img_path18=img_paths[17], img_path19=img_paths[18], img_path20=img_paths[19], pokemon_name1 = pokemon_names[0], pokemon_name2 = pokemon_names[1], pokemon_name3 = pokemon_names[2], pokemon_name4 = pokemon_names[3], pokemon_name5 = pokemon_names[4], pokemon_name6 = pokemon_names[5], pokemon_name7 = pokemon_names[6], pokemon_name8 = pokemon_names[7], pokemon_name9 = pokemon_names[8], pokemon_name10 = pokemon_names[9], pokemon_name11 = pokemon_names[10], pokemon_name12 = pokemon_names[11], pokemon_name13 = pokemon_names[12], pokemon_name14 = pokemon_names[13], pokemon_name15 = pokemon_names[14], pokemon_name16 = pokemon_names[15], pokemon_name17 = pokemon_names[16], pokemon_name18 = pokemon_names[17], pokemon_name19 = pokemon_names[18], pokemon_name20 = pokemon_names[19],)


	else:
		return redirect(url_for('index'))


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
