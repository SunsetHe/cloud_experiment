with open('$GITHUB_WORKSPACE/sorted.txt', 'r') as file:
    lines = file.readlines()
    sorted_numbers = [int(line.strip()) for line in lines]
if sorted_numbers == sorted(sorted_numbers):
    print("sort succeed")
else:
    print("sort failed")
