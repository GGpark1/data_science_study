import area

x = float(input('원의 지름을 입력해 주세요: '))
print(f"지름이 {x}인 원의 면적은 {area.circle(x)}입니다.")

y = float(input('정사각형의 변의 길이를 입력해 주세요: '))
print(f'변의 길이가 {y}인 정사각형의 면적은 {area.square(y)}입니다.')
