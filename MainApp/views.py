from django.shortcuts import render, HttpResponse, Http404
def test(request):
    return HttpResponse('test complete')

def home(request):#тут ответы на запросы(их надо вводить после айдишника)
    # text = f'''<h1>'Изучаем django'</h1> <strong>Автор</strong>: <i>Лазурненко Н. С.'''
    # return HttpResponse(text)
    return render(request,'index.html')
def about(request):#br - новая строка,bl-выделение(чтоб жирным шрифтом писалось)
    # info = f'''Имя: <b> Артем </b> <br>
    # Отчество: <b>  Игоревич </b> <br>
    # Фамилия: <b> Авдюшкин </b> <br>
    # телефон: <b> 8-923-600-01-02 </b> <br>
    # email: <b> developer@nlazurenko.ru </b> <br>'''
    # return HttpResponse(info)
    return render(request, 'about.html')#render - вызов к html странице
items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":0},
   {"id": 5, "name": "Кепка" ,"quantity":124},
]
def items_list(request):#выдает список товаров
    # items_result = '<ol>'
    # for item in items:
    #     items_result += '<li>' + f"<a href='/item/{item['id']}'>" + item['name'] + "</a>" +"</li>"#a-гиперссылка( a href = - открываем гиперссылку, /a-закрываем гиперссылку),li маркерованный(чтобы каждый пункт был на новой строчке и с точечкой)
    # items_result += "</ol>"#ol-это нумерованный список(чтобы каждый новый товар был пронумерован свое цифрой)
    # return HttpResponse(items_result)
    context = {
        'items': items
    }
    return render(request, 'items.html', context)
def item_page(request,id):#выдает инфу по каждому товару
    for item in items:
         if item['id']==id:
    #         item_str = f"товар {item['name']} количество {item['quantity']}"
    #         return HttpResponse(item_str)
    # return HttpResponse(f'Товар с id = {id} не найден')#все что в скобках для того чтобы выводить на несуществующий айдишник что такого товара нет
            return render(request, 'item_page.html', item)
    raise Http404(f'Товар с id = {id} не найден')#raise это к return как else к if