# mission_computer_main.log 파일을 읽어들여서 출력
with open('./mission_computer_main.log', 'r') as file:
    logList = file.readlines()
    
splitLogList = []

for log in logList:
    splitLog = log.strip().split(',')
    splitLogList.append(splitLog)


# 리스트 객체를 화면에 출력
for log in splitLogList:
    print(log)
    
print('\n-------------------------------------------------------------------\n')


# 리스트 객체를 시간의 역순으로 정렬(sort)
splitLogList.sort(reverse=True)

for log in splitLogList:
    print(log)

print('\n-------------------------------------------------------------------\n')


# 리스트 객체를 사전(Dict) 객체로 전환
keys = ["Timestamp", "Event", "Message"]
logDict = [dict(zip(keys, data)) for data in splitLogList]


# dict로 변환된 log data를 json 타입으로 다듬기
stringData = '['

for log in logDict:
    
    stringData += '\n{'
    
    for key, value in log.items():
        keyData = '"' + key + '"'
        valueData = '"' + value + '"'
        
        stringData += '\n \t' + keyData + ' : ' + valueData + ','
        
    stringData += '}, '
stringData += ']'

data = stringData.replace(',},', '\n},').replace(', ]', '\n]')


# JSON 파일 포맷으로 저장
with(open('./mission_computer_main.json', 'w') as file):
    file.write(data)