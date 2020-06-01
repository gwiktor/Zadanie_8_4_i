from flask import Flask 
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route("/mypage/me", methods=['GET'])
def me():
    return render_template("Zadanie_8_1.html")

@app.route("/mypage/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        print("We received GET")
        return render_template("Zadanie_8_1_2.html")
    if request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/mypage/contact")


if __name__ == '__main__':
    app.run(debug=True)