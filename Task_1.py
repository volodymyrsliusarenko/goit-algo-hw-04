def total_salary(path):
    total = 0
    count = 0
    
    with open(path, 'r') as file:
        for line in file:
            name, salary = line.split(',')
            salary = int(salary)
            total += salary
            count += 1
   
    if count != 0:
        average = total / count
    else:
        average = 0

    return total, average



total, average = total_salary("files/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")