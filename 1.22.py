class Student:
    def __init__(self, name, age):
        if len(name) < 2:
            raise ValueError("Студенттің аты кемінде 2 таңбадан болуы керек!")
        if age <= 0:
            raise ValueError("Жас 0-ден үлкен болуы керек!")
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Аты: {self.name}, Жасы: {self.age}")


student_list = []

while True:
    name = input("\nСтуденттің аты (тоқтату үшін 'stop'): ")
    if name.lower() == "stop":
        break

    try:
        age = int(input("Жасы: "))
    except ValueError:
        print("Қате: Жас сан түрінде болуы керек!")
        continue

    exists = any(s.name == name and s.age == age for s in student_list)
    if exists:
        print(f"{name}, {age} базада бар!")
        continue

    try:
        student = Student(name, age)
        student_list.append(student)
        print(f"{name} студент базада қосылды!")
    except ValueError as e:
        print("Қате:", e)
        continue

print("\nБарлық студенттер:")
for s in student_list:
    s.show_info()
