from core import *
from random import *
from constant import ConstantValues


word_file = File(ConstantValues.WORD_PATH)
log_file = File(ConstantValues.LOG_PATH)

record = (-1 if log_file.read_entry("Last record:") == "Not found" else log_file.read_entry("Last record:").split(":")[1])

passed = False
difficult = await_value(lambda entry: str(entry).upper(), ['HARD', 'NORMAL', 'EASY'])

random_index = randrange(1, len(word_file.read()))

game_instance = Game(
    Player(record), Difficult[difficult.upper()], word_file.read_index(random_index),
    len(word_file.read_index(random_index)), log_file
)

game_instance.get_render_tool().render(None)

while not game_instance.is_finished():
    game_instance.await_input()
