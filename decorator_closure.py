def trace(func):         # 호출할 함수를 매개변수로 받음
    def wrapper():       # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수시작')   # __name__으로 함수 이름 출력
        func()           # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수끝')    # wrapper 함수 반환

    return wrapper

@trace           # @데코레이터
def hello():
    print('hello')

@trace           # @데코레이터
def world():
    print('world')


hello()     # 함수를 그대로 호출
world()     # 함수를 그대로 호출
