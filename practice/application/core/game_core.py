from pathlib import Path

def await_value(func, valid_values: list) -> str:
    value = ''

    while func(value) not in valid_values:
        value = input(f"Введите допустимое значение {[entry for entry in valid_values]}: ")

    return func(value)

class File:
    path: str

    def __init__(self, path: str):
        self.path = path
        self.create_file_by_path(self.path)

    def create_file_by_path(self, path: str):
        file = Path(path)
        file.touch()
        return self

    def read(self) -> list[str]:
        try:
            return [entry.replace('\n', '') for entry in open(self.path, 'r', encoding='utf-8')]
        except FileNotFoundError as _:
            print('File not found')

    def read_entry(self, content: str) -> str:
        for item in self.read():
            if content not in item: continue
            return item
        return "Not found"

    def read_index(self, index: int) -> str:
        for line_index, text in enumerate(self.read()):
            if line_index != index - 1: continue
            return text

    def write(self, *content) -> None:
        file = open(self.path, 'w', encoding="utf-8")

        for item in content:
            file.write(f'{item}\n')
