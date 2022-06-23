# 중첩for를 이용한 * 모양 출력

print('*****')
print('****')
print('***')
print('**')
print('*')

for y in range(5,0,-1):
    for x in range(y):
        print('*', end='')
    print()
'''
for x in range(4):
    print('*', end='')
print(
    
for x in range(3):
    print('*', end='')
print()

for x in range(2):
    print('*', end='')

for x in range(1):
    print('*', end='')
    
print()
'''
# 삼각형 모양의 별 출력
for i in range(1, 6):
    for j in range(5-i):
        print(' ', end='')
    for j in range(1,2*i):
        print('*', end='')
    print()