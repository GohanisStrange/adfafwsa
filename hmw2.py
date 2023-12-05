# Словарь для хранения информации о студентах
students = {}

def add_student():
    """Добавление нового студента"""
    student_id = input("Введите номер студента: ")
    name = input("Введите имя студента: ")
    grade = input("Введите класс студента: ")
    students[student_id] = {'name': name, 'grade': grade}
    print(f"Студент {name} добавлен успешно!")

def view_students():
    """Просмотр списка студентов"""
    print("\nСписок студентов:")
    for student_id, info in students.items():
        print(f"ID: {student_id}, Имя: {info['name']}, Класс: {info['grade']}")

def search_student():
    """Поиск студента по ID"""
    student_id = input("Введите ID студента для поиска: ")
    if student_id in students:
        info = students[student_id]
        print(f"Найден студент: ID: {student_id}, Имя: {info['name']}, Класс: {info['grade']}")
    else:
        print("Студент с указанным ID не найден.")

# Основной цикл программы
while True:
    print("\n1. Добавить студента")
    print("2. Просмотреть список студентов")
    print("3. Поиск студента")
    print("4. Выйти")

    choice = input("Выберите действие (1-4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        print("Программа завершена.")
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите действие от 1 до 4.")
