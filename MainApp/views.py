from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import response

items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity":5},
   {"id": 2, "name": "Куртка кожаная", "quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity":12},
   {"id": 7, "name": "Картофель фри", "quantity":0},
   {"id": 8, "name": "Кепка", "quantity":124}
]


userData = """<p>Имя: <strong>Иван</strong></p>
<p>Отчество: <strong>Петрович</strong></p>
<p>Фамилия: <strong>Иванов</strong></p>
<p>телефон: <strong>8-923-600-01-02</strong></p>
<p>email: <strong>vasya@mail.ru</strong></p>"""

# Create your views here.
def home(request):
    text = """<h1>"Изучаем django День первый !"</h1>
            <strong>Автор</strong>: <i>Иванов И.П.</i>"""
    return HttpResponse(text)

def about(request):
    return HttpResponse(userData)

def items_list(request):
    text = "<h1>Список товаров:</h1><ol>"
    for item in items:
        text += f"""<li><strong>ID {item["id"]}</strong>, Название товара: {item["name"]}, Количество: {item["quantity"]}</li>"""
    text += "</ol>"
    return HttpResponse(text)

def item_id(request, id):
    text = "<h1>Товар не найден</h1>"

    for item in items:
        if id == item["id"]:
            return HttpResponse(f"""
            <h1>Товар: ID {item["id"]}</h1>
            <p>Название товара: {item["name"]}</p>
            <p>Количество: {item["quantity"]}</p>
            """)

    return HttpResponseNotFound(f"<h1>Товар ID = {id} не найден</h1>")



