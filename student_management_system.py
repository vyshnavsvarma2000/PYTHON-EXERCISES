class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name : {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            print(student)

    def find_student(self, name):
        for student in self.students:
            if name in student.name:
                return student
        return None

    def update_student(self, name, new_age, new_grade):
        student = self.find_student(name)
        if student:
            student.age = new_age
            student.grade = new_grade
            print('Student info updated successfully', student)
        else:
            print('Student not found')

    def delete_student(self, name):
        student = self.find_student(name)
        if student:
            self.students.remove(student)
            print("Student deleted successfully")
        else:
            print("Student not found")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.add_student(Student("John", 18, "A"))
    sms.add_student(Student("David", 18, "C"))
    sms.update_student('John', 30, 'B')
    sms.delete_student("John")
    sms.display_all_students()