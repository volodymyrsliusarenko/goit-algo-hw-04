def get_cats_info(path):
    info = []
    with open(path, 'r') as file:
        for line in file:
            id, name, age = line.strip().split(',')
            info.append({
                'id': id,
                'name': name,
                'age': int(age)
            })
    return info


cats_info = get_cats_info("files/cats.txt")
print(cats_info)