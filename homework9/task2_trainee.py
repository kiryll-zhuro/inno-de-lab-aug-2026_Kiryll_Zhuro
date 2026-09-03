from task1_trainee import Trainee


class HardworkingTrainee(Trainee):
    """Трудоголик получает +2 балла за домашнее задание."""

    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score += 2


class AuditTrainee(Trainee):
    def is_passing(self) -> bool:
        """Всегда возвращает True."""
        return True


class Cohort:
    """Учебная группа управляет списком учащихся."""

    def __init__(self, title: str, trainees: list[Trainee] | None = None) -> None:
        self.title: str = title
        self.trainees: list[Trainee] = trainees if trainees is not None else []

    def add_trainee(self, trainee: Trainee) -> None:
        """Добавляет учащегося в группу."""
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        """Проводит лекцию (+1 балл всем)."""
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        """Возвращает учащихся, которые проходят курс."""
        return [trainee for trainee in self.trainees if trainee.is_passing()]

# 1. Создал учащихся разных типов
std_trainee = Trainee("Алексей", "Смирнов", score=8, passing_grade=10)
hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8, passing_grade=10)
audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0, passing_grade=10)

# 2. Создал группу и добавляем студентов
cohort = Cohort("Python Advanced")
cohort.add_trainee(std_trainee)
cohort.add_trainee(hard_trainee)
cohort.add_trainee(audit_trainee)

# 3. Проводим лекцию для всей группы (+1 балл всем)
cohort.conduct_lecture()

# 4. Проверяем работу переопределенного ДЗ для трудоголика (+2 балла)
hard_trainee.do_homework()

# 5. Выводим список тех, кто проходит курс
passing_students = cohort.get_passing_students()


print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===")
for student in cohort.trainees:
    print(f"{student.name} {student.surname} | Баллы: {student.score} | Проходит: {student.is_passing()}")

print("\nУспешно зачислены на следующий модуль:")
for student in passing_students:
    print(f"- {student.name} {student.surname}")