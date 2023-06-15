import os

path = '.idea/Test'
data = {}
directory = ".idea/Test/data.csv"

class Row:
    idx = 0

    def __init__(self, idx: int):
        self.idx = idx

    def get_idx(self):
        return self.idx

    def set_idx(self, val):
        self.idx = val


class RowModel(Row):
    idx = 0
    date_in = ""
    date_off = ""
    count_car = 0
    count_wait_car = 0

    def __init__(self, idx: int, date_in: str, date_off: str, count_car: int, count_wait_car: int):
        super().__init__(idx)
        self.date_in = date_in
        self.date_off = date_off
        self.count_car = count_car
        self.count_wait_car = count_wait_car

    def __str__(self):
        return f"{self.idx}, {self.date_in}, {self.date_off}, {self.count_car}, {self.count_wait_car}"

    def __setattr__(self, __name, __value):
        self.__dict__[__name] = __value


class Svetofor:
    pointer = 0
    data = []
    file_path = "data.csv"
    def __repr__(self):
        return f'Svetofor({self.data})'

    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.data):
            return self.data[self.index]
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.data[key]

    def generator(self):
        for item in self.data:
            yield item

    def count(path):
        files = [file for file in os.listdir(path) if os.path.isfile(f'{path}/{file}')]
        print(len(files))

    def add_new(self, date_in, date_off, count_car, count_wait_car):
        if len(self.data) == 0:
            self.data.append(RowModel(1, date_in, date_off, count_car, count_wait_car))
        else:
            self.data.append(RowModel(self.data[len(self.data) - 1].idx + 1, date_in, date_off, count_car, count_wait_car))
        self.save(self.file_path, self.data)

    @staticmethod
    def save(path, new_data):
        with open(path, "w", encoding='utf-8') as f:
            for rm in new_data:
                f.write(f"{rm.idx}, {rm.date_in}, {rm.date_off}, {rm.count_car}, {rm.count_wait_car}")

    @staticmethod
    def parse_csv(f):
        with open(f) as file:
            lines = file.read().splitlines()
            for line in lines:
                (idx, date_in, date_off, count_car, count_wait_car) = line.replace("\n", "").split(";")
                data.update({int(idx): {"дата и время включения":date_in, "дата и время выключения": date_off, "кол-во проехавших автомобилей": int(count_car), "кол-во автомобилей в ожидании": int(count_wait_car)}})
        return data

    @staticmethod
    def print_data(s):
        f = open(directory, "a")
        f.write("\n")
        f.write(s)
        f.close()


    def sorted_by_number(data) -> dict:
        return dict(sorted(data.items(), key=lambda x: x[1]["кол-во автомобилей в ожидании"], reverse=False))


    def sorted_dif(data, value) -> dict:
        return dict((k,v) for k,v in data.items() if v["кол-во проехавших автомобилей"] < value)


data = Svetofor.parse_csv(directory)
collection = Svetofor(data)

Svetofor.count(path)

print('Словарь "Светофор":')
for k, v in Svetofor.parse_csv(directory).items():
    print(k, v)
print('Сортировка по числовому полю:')
for k, v in Svetofor.sorted_by_number(data).items():
    print(k, v)
print('Сортировка по критерию:')
for k, v in Svetofor.sorted_dif(data, 900).items():
    print(k, v)


print('\nИтератор')
for item in iter(data):
    print(item)

print('\n\nГенератор')
collection_generator = collection.generator()
print(next(collection_generator))

print('\n\nВыбор по индексу' )
idx = int(input("Индекс: "))
print(f"\n{data[idx]}")