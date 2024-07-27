from flask import render_template, request, redirect, url_for
from app import app

@app.route("/", methods=["GET", "POST"])
def form():
    user_data = {}
    if request.method == "POST":
        # Получаем данные из формы
        user_data['name'] = request.form.get("name")
        user_data['city'] = request.form.get("city")
        user_data['hobby'] = request.form.get("hobby")
        user_data['age'] = request.form.get("age")

        # Здесь можно добавить обработку данных или сохранить их в базе данных

    return render_template("forms.html", user_data=user_data)



