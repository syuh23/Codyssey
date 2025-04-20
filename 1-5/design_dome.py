import numpy as np

arr1 = np.genfromtxt('./mars_base_main_parts-001.csv', delimiter = ',', dtype = None, encoding = 'utf-8', names = ['parts', 'strength'], skip_header = 1)
arr2 = np.genfromtxt('./mars_base_main_parts-002.csv', delimiter = ',', dtype = None, encoding = 'utf-8', names = ['parts', 'strength'], skip_header = 1)
arr3 = np.genfromtxt('./mars_base_main_parts-003.csv', delimiter = ',', dtype = None, encoding = 'utf-8', names = ['parts', 'strength'], skip_header = 1)

def arr_to_dict(array):
    return {row['parts']: int(row['strength']) for row in array}

dict1 = arr_to_dict(arr1)
dict2 = arr_to_dict(arr2)
dict3 = arr_to_dict(arr3)

rows = arr1['parts']

parts_dict = []
for row in rows:
    strength1 = dict1.get(row, 0)
    strength2 = dict2.get(row, 0)
    strength3 = dict3.get(row, 0)
    parts_dict.append([str(row), strength1, strength2, strength3])

parts = np.array(parts_dict)

averages = []

for row in parts:
    part = row[0]
    strength_values = np.array(row[1:], dtype=float)
    avg_strength = np.mean(strength_values)
    averages.append([str(part), float(avg_strength)])

filtered_parts = [part for part in averages if part[1] < 50]

filtered_parts_array = np.array(filtered_parts)

np.savetxt('parts_to_work_on.csv', filtered_parts_array, delimiter = ',', header = 'Part,Average Strength', fmt = '%s', comments = '')