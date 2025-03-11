# Hello Mars 출력
print('Hello Mars')

# 문제 풀이
try:
    file = open('./mission_computer_main.log', 'r', encoding='UTF-8')
except FileNotFoundError:
    print('해당 파일이 존재하지 않습니다.')

logList = file.readlines()
file.close()

# 로그 출력
for log in logList:
    print(log)

print('\n--------------------------------------------------------\n\n')

# 로그 거꾸로 출력 (보너스 문제)
logList.reverse()

for log in logList:
    print(log)