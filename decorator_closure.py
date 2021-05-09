def decorator1(func):         # 호출할 함수를 매개변수로 받음
    def wrapper():       # 호출할 함수를 감싸는 함수
        print('decorator1')
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper

@decorator1
@decorator2
def hello():
    print('hello')

hello()
