# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def read_source(content):
    return [item.split(';') for item in content.split('\n')]

def sort_data(content):
    return sorted(content, key=lambda item: int(item[1]))

def filter_data(content, min_age: int):
    return [item for item in content if int(item[1]) > min_age]

def get_users_from_source(data, filter_min_age: int):
    readed_data = read_source(data)
    sorted_data = sort_data(readed_data)
    return filter_data(sorted_data, filter_min_age)

print(get_users_from_source(csv, 25))
