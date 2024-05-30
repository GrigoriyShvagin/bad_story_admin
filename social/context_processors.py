menu = [
    {'title': 'Главная', 'url': 'index'},
    {'title': 'Обсуждения', 'url': 'discussions'},
]

def social_context(requests):
    return {'menu': menu}