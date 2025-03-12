# Hello Mars 출력
print('Hello Mars')

# 문제 풀이
try:
    file = open('./mission_computer_main.log', 'r', encoding='UTF-8')
    logList = file.readlines()
    file.close()

    # 로그 출력
    for log in logList:
        print(log, end='')
        
    print('\n--------------------------------------------------------\n')

    # 로그 거꾸로 출력 (보너스 문제)
    logList.reverse()

    for log in logList:
        print(log, end='')

except Exception as e:
    # 오류 문구 write
    error_message = str(e)
    error_file = open('./error_file.txt', 'w+')
    error_file.write(error_message)
    error_file.close()