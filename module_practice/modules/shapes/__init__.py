#shapes라는 폴더(패키지)를 실행하면 __init__파일이 가장 먼저 실행됨(패키지 초기화)
#__init__이 실행되면서 area, volume을 패키지로 사용할 수 있도록 함
#__init__에 아래와 같이 패키지를 정의하지 않으면 'run.py'에서 area와 volum을 패키지 단위로 import할 수 없음(from A import B로만 사용 가능)

from shapes import area, volume