a = 9
def wrap_result_decorator(func):
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        modified_result = {'result': result}
        return modified_result

    return wrapper


def aut(number):
    if aut == int:
        p = a + 10
        print(p)
        return p
    if aut == float:
       return a


aut(1)
