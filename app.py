from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/index.html')
def index():
    return render_template('index.html', style_href=url_for('static', filename='styles/style.css'))


@app.route('/2.html')
def food():
    return render_template('2.html', style_href=url_for('static', filename='styles/style2.css'))


@app.route('/3.html')
def breeds():
    return render_template('3.html', style_href=url_for('static', filename='styles/style3.css'))


@app.route('/4.html')
def games():
    return render_template('4.html', style_href=url_for('static', filename='styles/style4.css'))


if __name__ == '__main__':
    app.run(debug=True)
