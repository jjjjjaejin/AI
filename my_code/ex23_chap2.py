# 2024/03/12
# 백, 십, 일의 자리 값 출력

n=int(input('세 자리 정수를 입력하세요:'))
print('백의 자리:', n//100)
print('십의 자리:', n%100//10)
print('일의 자리:', n%10)