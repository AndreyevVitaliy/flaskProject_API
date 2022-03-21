from datetime import datetime

def decoration(func):
    """ функция декорация
    """
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        print(datetime.now() - start)
        print(datetime.today().isoformat())
    return wrapper

@decoration
def title_(_anytext):
    _list = []
    for i in range(10**1):
       if i % 2 == 0:
            _list.append(i)
    print(_list)



title_("Сама функция_1")