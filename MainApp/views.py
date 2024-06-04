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

userData = {"name" : "Иван",
            "middleName" : "Петрович",
            "surName" : "Иванов",
            "phone" : "8-923-600-01-02",
            "email" : "vasya@mail.ru"}
             
# Create your views here.
def home(request):
    # text = """
    # <h1>"Изучаем django День первый !"</h1>
    # <strong>Автор</strong>: <i>Иванов И.П.</i>
    # <h2><a href="/about">About</a></h2>
    # <h2><a href="/items">Items<a></h2>
    # """
    # return HttpResponse(text)
    context = {
        "name": "Петров Николай Петрович",
        "email": "my_mail@mail.ru"
    }

    return render(request, "index.html", context)

def about(request):

    return render(request, "about.html", userData)

def items_list(request):
    # text = "<h1>Список товаров:</h1><ol>"
    # for item in items:
    #     text += f"""
    #     <li><a href="/item/{item["id"]}"><strong>{item["name"]}</strong>, {item["quantity"]} шт.</a></li>
    #     """
    # text += "</ol>"
    context = {
        "items" : items
    }

    return render(request, "items-list.html", context)

def item_id(request, id):
    text = "<h1>Товар не найден</h1>"

    for item in items:
        if id == item["id"]:
        #     return HttpResponse(f"""
        #     <h1>Товар: ID {item["id"]}</h1>
        #     <p>Название товара: {item["name"]}</p>
        #     <p>Количество: {item["quantity"]}</p>
        #     <a href="/items">Назад</a>
        #     """)
            context = {
                "item" : item
            }
            return render(request, "item-page.html", context)
        
    return HttpResponseNotFound(f"<h1>Товар ID = {id} не найден</h1>")



