total_sum = 0

with open('largeNums.txt', 'r') as file:
    for _ in range(100):
        line = file.readline().strip()  
        if line:  
            total_sum += int(line)  

first_ten_digits = str(total_sum)[:10]

print("First 10 digits of the sum:", first_ten_digits)