def get_cats_info(path):
    info = []
    dict = {"id": "", "name": "", "age": ""}
    with open(path, 'r') as file:
        for line in file:
            id, name, age = line.strip().split(',')
            dict['id'] = id
            dict['name'] = name
            dict['age'] = age


            info.append(dict)


    return info


cats_info = get_cats_info("files/cats.txt")
print(cats_info)