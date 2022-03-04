#로또 번호 생성기 ver.1
import random

lotto_set = []

def lotto_num(*args):
    lotto = set()
    while len(lotto) < 6 :
        lotto.add(random.randint(1,45))
    lotto_set.append(sorted(lotto))
    if len(lotto_set) == 5:
        return lotto_set
    else:
        return lotto_num(lotto_set)

print(*lotto_num(), sep='\n')
# 리스트 내부의 리스트 요소를 한 줄씩 출력하는 방법

#로또 번호 생성기 ver.2
def lotto_num2():
    for _ in range(5):
        numbers = sorted(random.sample(range(1,46), 6))
        # random 모듈의 sample 함수는 중복되지 않게 값을 반환한다.
        print(numbers)

lotto_num2()