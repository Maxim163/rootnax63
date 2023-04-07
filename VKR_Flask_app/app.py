#прогноз показателя "Прочность при растяжении"
import flask
from flask import render_template
import pickle
import sklearn

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])

def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        with open('vkr_m.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        z1 = float(flask.request.form['Соотношение матрица-наполнитель'])
        z2 = float(flask.request.form['Плотность, кг/м3'])
        z3 = float(flask.request.form['модуль упругости, ГПа'])
        z4 = float(flask.request.form['Количество отвердителя, м.%'])
        z5 = float(flask.request.form['Содержание эпоксидных групп,%_2'])
        z6 = float(flask.request.form['Температура вспышки, С_2'])
        z7 = float(flask.request.form['Поверхностная плотность, г/м2'])
        z8 = float(flask.request.form['Модуль упругости при растяжении, ГПа'])
        z9 = float(flask.request.form['Потребление смолы, г/м2'])
        z10 = float(flask.request.form['Угол нашивки, град'])
        z11 = float(flask.request.form['Шаг нашивки'])
        z12 = float(flask.request.form['Плотность нашивки'])

        y_pred = loaded_model.predict([[z1, z2, z3, z4, z5, z6,
                                        z7, z8, z9, z10, z11, z12]])

        return render_template('main.html', result=y_pred)

if __name__ == '__main__':
    app.run()
