# Отчёт

## Part 1: Выбор сценария

Для данной работы выбран сценарий: **система высшего образования**.  
Эта система будет управлять студентами, предметами, преподавателями, расписанием и группами.

---

## Part 2: Проектирование базы данных и документация

### Идентификация сущностей и атрибутов

- Студенты (`Students`)
- Преподаватели (`Teachers`)
- Предметы (`Subjects`)
- Группы (`StudyGroups`)
- Расписание (`Schedule`)

---

## Проектирование таблиц

### 1. Table Name: `Students`

**Description:**  
Хранит информацию о студентах университета.

**Attributes:**

| Attribute     | Data Type     | Constraints                                                        |
|---------------|---------------|--------------------------------------------------------------------|
| StudentID     | INTEGER       | PK, NOT NULL                                                       |
| FirstName     | VARCHAR(30)   | NOT NULL                                                           |
| LastName      | VARCHAR(30)   | NOT NULL                                                           |
| Phone         | VARCHAR(16)   | NOT NULL, UNIQUE                                                   |
| BirthDate     | DATE          | NOT NULL                                                           |
| StudyGroupID  | INTEGER       | FK REFERENCES StudyGroups(StudyGroupID), NOT NULL                  |

**Constraints:**

- `PK_Students`: PRIMARY KEY(StudentID)
- `UQ_Students_Phone`: UNIQUE(Phone)
- `CHK_Students_BirthDate`: CHECK(BirthDate < CURRENT_DATE)
- `FK_Students_StudyGroups`: FOREIGN KEY(StudyGroupID) REFERENCES StudyGroups(StudyGroupID)

---

### 2. Table Name: `Teachers`

**Description:**