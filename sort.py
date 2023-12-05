import random
import os

# 排序函数：对列表进行排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]


# 生成从0到9的随机数列表
random_numbers = random.sample(range(10), 10)

print(random_numbers)

# 对列表进行排序
sorted_numbers = random_numbers.copy()  
selection_sort(sorted_numbers)

# 输出排序后的列表
print(sorted_numbers)

# 创建一个新的文件夹，用来存放输出文件
output_directory = 'output'
os.makedirs(output_directory, exist_ok=True)

# 保存文件 sorted.txt
output_file_path = os.path.join(output_directory, 'sorted.txt')
with open(output_file_path, 'w') as file:
    for num in sorted_numbers:
        file.write(str(num) + '\n')