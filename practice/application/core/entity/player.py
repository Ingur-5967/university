class Player:
    attempt: int
    last_record: int

    def __init__(self, last_record: int = 0):
        self.last_record = last_record
        self.attempt = 7

    def check_input(self, generated_word: str, value: str) -> bool:
        return generated_word.__contains__(value) or generated_word == value

    def get_record(self) -> int:
        return self.last_record

    def get_attempt(self) -> int:
        return self.attempt

    def set_attempt(self, new_attempt: int) -> None:
        self.attempt = new_attempt
