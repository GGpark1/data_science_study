PI = 3.14

#원의 면적을 구하는 함수
def circle(radius):
    return PI * radius * radius

#정사각형의 면적을 구하는 함수
def square(length):
    return length * length


#해당 모듈이 __main__일 때만 실행, 즉 모듈이 직접 스크립트로 작동할 때만 실행
if __name__ == '__main__':
    # circle 함수 테스트
    print(circle(2) == 12.56)
    print(circle(5) == 78.5)

    # square 함수 테스트
    print(square(2) == 4)
    print(square(5) == 25)