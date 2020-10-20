from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')

def main():
    return render_template("tittle.html")


@app.route('/about')

def about():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nibh augue, " \
           "suscipit a, scelerisque sed, lacinia in, mi. Cras " \
           "vel lorem. Etiam pellentesque aliquet tellus."




if __name__ == '__main__':
    app.run(debug=True)