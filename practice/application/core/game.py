from application.core.entity.player import Player
from application.core.game_core import File
from application.core.utils.game_utils import Difficult


class Render:
    game_map: list
    map_size: int

    def __init__(self, map_size: int):
        self.map_size = map_size
        self.game_map = []
        for index in range(map_size):
            self.game_map.append("|▉|")

    def render(self, accepted_symbols: dict = None):

        if accepted_symbols is not None:

            for index in range(self.map_size):
                if not accepted_symbols.keys().__contains__(index): continue
                self.game_map.__setitem__(index, accepted_symbols[index])

        print(f"Текущая карта <Поля чудес>:\n {''.join(self.game_map)}")

    def get_game_map(self) -> list:
        return self.game_map


class Game:
    difficult: Difficult
    log_file: File
    finished: bool

    def __init__(self, player: Player, difficult: Difficult, word: str, map_size: int, log_file: File):
        self.difficult = difficult
        self.log_file = log_file
        self.player = player
        self.word = word
        self.finished = False
        self.render_tool = Render(map_size)

        self.player.set_attempt(self.difficult.value)

        print(f'Ваш прошлый рекорд: {"Нет" if self.player.get_record() == -1 else (self.player.get_record())}\n')

    def await_input(self):
        value = input('Введите символ или слово целиком: ')

        print(self.word)

        accepted_symbol = {}

        if value == self.word:
            print(f"Вы отгадали слово полностью с {self.difficult.value - self.player.get_attempt()} ошибкой(-ми)!")

            for index, symbol in enumerate(value):
                self.render_tool.get_game_map().__setitem__(index, symbol)

            self.set_finished(True)
            pass

        if not self.player.check_input(self.word, value):
            self.player.set_attempt(self.player.get_attempt() - 1)
            print(f"Увы, вы не угадали символ -1 попытка! Осталось: {self.player.get_attempt()}!")

            if self.player.get_attempt() == 0:
                self.set_finished(True)

            pass

        symbol_list = [symbol for symbol in self.word]

        all_joined_indexes = []
        for index, item in enumerate(symbol_list):
            if item != value: continue
            all_joined_indexes.append(index)

        for index in all_joined_indexes:
            accepted_symbol[index] = value

        if not self.is_finished() and ''.join(self.render_tool.game_map) == self.word:
            print(f"Вы отгадали слово по частям с {self.difficult.value - self.player.get_attempt()} ошибкой(-ми)!")
            self.set_finished(True)
            pass

        if self.is_finished(): self.generate_log()

        self.render_tool.render(accepted_symbol)

    def set_finished(self, state: bool) -> None:
        self.finished = state

    def is_finished(self) -> bool:
        return self.finished

    def generate_log(self) -> None:
        self.log_file.write(f"Last record: {self.difficult.value - self.player.get_attempt()} ошибок")

    def get_difficult(self) -> Difficult:
        return self.difficult

    def get_log_file(self) -> File:
        return self.log_file

    def get_render_tool(self) -> Render:
        return self.render_tool
