# csv 파일 읽기
with open('./Mars_Base_Inventory_List.csv', 'r') as file:
    csv_data = file.readlines()
    
    
# 리스트로 저장
csv_list = [data.strip().split(',') for data in csv_data]

print(csv_list)
print('\n-------------------------------------------------------------------\n')


# 리스트 인화성 기준으로 정렬
header = csv_list[0]
data_rows = csv_list[1:]

data_rows.sort(key=lambda x : x[-1], reverse=True)

print(data_rows)
print('\n-------------------------------------------------------------------\n')


# 인화성이 0.7 이상인 값만 filter_list에 저장
filter_list = [row for row in data_rows if float(row[-1]) >= 0.7]

print(filter_list)


# filter_list를 csv 파일로 작성
with open('./1-3/Mars_Base_Inventory_danger.csv', 'w') as file:
    file.write(','.join(header) + '\n')
    
    for data in filter_list:
        file.write(','.join(data) + '\n')