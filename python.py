range(start, end, step)
# end -1 까지만 step 간격으로 순차적으로 진행
# step 인자를 설절하지 않으면 default 1
# step인자를 -1로 설정하면 역순으로 가능 단, start에 큰수 end에 작은수를 넣어야함

array.count(n)
# 배열 array에서 n이 등장하는 횟수를 count

# 리스트의 요소들을 뒤집는다.
list.reverse() # 반환하지 않고 변환만 한다. (변수에 저장해야함)
reversed(list) # 변환하고 반환한다.

str[start:end:step]
# 문자열 슬라이싱
str[::-1]
# ::-1 은 문자열의 요소들을 뒤집어서 슬라이싱 한다.

'Yes' if True else 'No'
# if문 한줄로 표현
# 단 if문을 중첩하게 되면 구분이 어려워질 수 있다. ※ 신중히 사용

tuple = [(1, 2), (3, 4)]
tuple[0][0] # 1
tuple[0][1] # 2
tuple[1][0] # 3
tuple[1][1] # 4
# 튜플 접근 방법 (2번 인덱싱)