range(start, end, step)
# end -1 까지만 step 간격으로 순차적으로 진행
# step 인자를 설절하지 않으면 default 1
# step인자를 -1로 설정하면 역순으로 가능 단, start에 큰수 end에 작은수를 넣어야함

# array
array.count(n)
# 배열 array에서 n이 등장하는 횟수를 count
map(자료형, array)
# array의 배열을 for문처럼 반복하면서 첫인자인 자료형으로 바꿔준다.

# list
# 리스트의 요소들을 뒤집는다.
list.reverse() # 반환하지 않고 변환만 한다. (변수에 저장해야함)
reversed(list) # 변환하고 반환한다.
list() # 인자를 리스트로 만들어줌
input().split()
# 입력받는 인자를 split으로 나누어 리스트화 한다.
# split()함수는 결과를 리스트로 반환한다.

# string
str[start:end:step]
# 문자열 슬라이싱
str[::-1]
# ::-1 은 문자열의 요소들을 뒤집어서 슬라이싱 한다.
str.swapcase()
# 소문자는 대문자로 대문자는 소문자로 변환 후 복사본을 반환

# if
'Yes' if True else 'No'
# if문 한줄로 표현
# 단 if문을 중첩하게 되면 구분이 어려워질 수 있다. ※ 신중히 사용

# tuple
tuple = [(1, 2), (3, 4)]
tuple[0][0] # 1
tuple[0][1] # 2
tuple[1][0] # 3
tuple[1][1] # 4
# 튜플 접근 방법 (2번 인덱싱)

# bit
k << n(int) # k를 왼쪽으로 n(int)만큼 비트이동 시킨다.
# 왼쪽으로 비트를 이동시킨다는 의미는 값이 2배씩 커진다는 의미
k >> n(int) # 위와 반대

#------------------------------------------------------
set()
# 집합을 만든다. 집합은 형태는 딕셔너리처럼 중괄호를 사용하지만
# 키가 없고 값만 있다는 것이 특징
# 또한 중복값이 없고 uniaue한 값만 있다는 것또한 특징이다.

s.add(item)
# 집합에 item에 해당하는 값을 넣는다. 위치는 랜덤

s.update(배열)
# set에서의 update는 여러값을 한번에 추가할때 주로 사용
# 중복값을 자동으로 제거된다.

s.remove(item)
# item의 값을 집합에서 제거 item이 집합에 없으면 에러 발생
s.discard(item)
# remove와 동일하지만 에러가 발생하지 않음

a | b, a.union(b) # 합집합 연산자
a & b, a.intersection(b) # 교집합 연산자
a - b, a.difference(b) # 차집합 연산자
a ^ b, a.symmetric_difference(b) # 대칭차집합 연산자 (합 - 교)
a |= b, a &= b, a -= b, a ^= b # 연산과 동시에 할당

a.issubset(b) # 부분집합 여부 확인
# a집합의 값이 b집합안에 있는가의 여부를 bool값으로 반환
a.issuperset(b) # issubset과 반대 의미
a.isdisjoint(b) # 교집합이 있으면 True 없으면 False
#------------------------------------------------------

