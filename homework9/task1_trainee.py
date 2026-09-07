class Trainee:
    """Класс для отслеживания прогресса и успеваемости стажёра."""

    __score: int

    def __init__(self, name: str, surname: str,
                 score: int = 0, passing_grade: int = 10) -> None:
        self.name: str = name
        self.surname: str = surname
        self.passing_grade: int = passing_grade
        self.score = score

    @property
    def score(self) -> int:
        """Возвращает значение приватного атрибута __score."""
        return self.__score

    @score.setter
    def score(self, value: int) -> None:
        """Устанавливает балл с валидацией типа и значения."""
        # Если тип не int, то выбрасываю ValueError
        if not isinstance(value, int):
            raise ValueError(f"Expected value of type int, got {type(value)}")
        # Если балл отрицательный, то выбрасываю ValueError
        if value < 0:
            raise ValueError("The score shouldn't be less than 0!")
        # Если проверки пройдены, то обновляю приватный атрибут
        self.__score = value

    def do_homework(self) -> None:
        """Increases score by 1"""
        # Меняю балл через свойство score
        self.score += 1

    def miss_homework(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Increases score by 1"""
        self.score += 1

    def miss_lecture(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def is_passing(self) -> bool:
        """Возвращает True, если стажёр набрал проходной балл."""
        return self.score >= self.passing_grade

if __name__ == "__main__":
    print("=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЁРА ===")

    # 1. Создал стажера с начальным баллом 9 и проходным баллом 10
    trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)

    # 2. Выполнил домашнее задание и проверил статус
    trainee.do_homework()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    # 3. Пропустил лекцию и проверил статус
    trainee.miss_lecture()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    # 4. Проверил валидацию (попытка задать неверный тип или отрицательное значение) 
    try:
        trainee.score = -5
    except ValueError as e:
        print(f"Ошибка: {e}")