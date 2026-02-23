class Student():
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Жас теріс болмауы керек")
        self.name = name
        self.age = age

students = []
while True:
    name = input("Cтудент атын енгізіңіз (тоқтату үшін 'stop'): ")
    if name.lower() == "stop":
        break

    try:
        age = int(input("Жасын енгізіңіз: "))
        student = Student(name, age)
        students.append(student)
        print(f"{name} қосылды.\n")
    except ValueError as e:
        print(f"Қате: {e}\n")

if len(students) > 0:
    total_age = 0

    for student in students:
        total_age += student.age

    average_age  = total_age / len(students)
    print(f"\nБарлық студент саны: {len(students)}")
    print(f"Орташа жас: {average_age}")
else:
    print("Базада студент жоқ.")