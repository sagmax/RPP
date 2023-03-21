import os

path = '.idea/Test'
data = {}
directory = ".idea/Test/data.csv"

# Подсчет количества файлов в папке
def count(path):
    files = [file for file in os.listdir(path) if os.path.isfile(f'{path}/{file}')]
    print(len(files))

# считывание данных из файла в словарь
def parse_csv(f):
    with open(f) as file:
        lines = file.read().splitlines()
        # raw_csv = csv.reader(directory, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for line in lines:
            (idx, date_in, date_off, count_car, count_wait_car) = line.replace("\n", "").split(";")
            data.update({int(idx): {"дата и время включения":date_in, "дата и время выключения": date_off, "кол-во проехавших автомобилей": int(count_car), "кол-во автомобилей в ожидании": int(count_wait_car)}})
    return data

# запись в файл и добавление нового элемента
def print_data(s):
    f = open(directory, "a")
    f.write("\n")
    f.write(s)
    f.close()


# сортировка по числовому полю
def sorted_by_number(data) -> dict:
    return dict(sorted(data.items(), key=lambda x: x[1]["кол-во автомобилей в ожидании"], reverse=False))


# сортировка по критерию
def sorted_dif(data, value) -> dict:
    return dict((k,v) for k,v in data.items() if v["кол-во проехавших автомобилей"] < value)
count(path)

print('Словарь "Светофор":')
for k, v in parse_csv(directory).items():
    print(k, v)
print('Сортировка по числовому полю:')
for k, v in sorted_by_number(parse_csv(directory)).items():
    print(k, v)
print('Сортировка по критерию:')
for k, v in sorted_dif(parse_csv(directory), 900).items():
    print(k, v)
