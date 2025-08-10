class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _get_average_grade(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades.extend(grade)
        return sum(all_grades)/len(all_grades) if all_grades else 0

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self._get_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {courses_in_progress}\nПройденные курсы: {finished_courses}'

    def __lt__(self, other):
        return self._get_average_grade() < other._get_average_grade()

    def __le__(self, other):
        return self._get_average_grade() <= other._get_average_grade()

    def __eq__(self, other):
        return self._get_average_grade() == other._get_average_grade()

    def __ne__(self, other):
        return self._get_average_grade() != other._get_average_grade()

    def __gt__(self, other):
        return self._get_average_grade() > other._get_average_grade()

    def __ge__(self, other):
        return self._get_average_grade() >= other._get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _get_average_grade(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades.extend(grade)
        return sum(all_grades)/len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self._get_average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}'

    def __lt__(self, other):
        return self._get_average_grade() < other._get_average_grade()

    def __le__(self, other):
        return self._get_average_grade() <= other._get_average_grade()

    def __eq__(self, other):
        return self._get_average_grade() == other._get_average_grade()

    def __ne__(self, other):
        return self._get_average_grade() != other._get_average_grade()

    def __gt__(self, other):
        return self._get_average_grade() > other._get_average_grade()

    def __ge__(self, other):
        return self._get_average_grade() >= other._get_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    student_1 = Student('София', 'Калугина', 'Ж')
    student_2 = Student('Андрей', 'Малышев', 'М')

    student_1.courses_in_progress = ['Python', 'Git']
    student_2.courses_in_progress = ['Python']
    student_1.finished_courses = ['Основы программирования']

    lecturer_1 = Lecturer('Иван', 'Иванов')
    lecturer_2 = Lecturer('Иванесса', 'Иванова')

    lecturer_1.courses_attached = ['Python']
    lecturer_2.courses_attached = ['Git', 'Python']

    reviewer_1 = Reviewer('Владимир', 'Ульянов')
    reviewer_2 = Reviewer('Надежда', 'Крупская')

    reviewer_1.courses_attached = ['Python']
    reviewer_2.courses_attached = ['Git']

    print('Оценки студента: ')
    reviewer_1.rate_hw(student_1, 'Git', 3)
    reviewer_2.rate_hw(student_1, 'Python', 6)
    reviewer_1.rate_hw(student_2, 'Python', 9)
    reviewer_2.rate_hw(student_2, 'Python', 7)

    print('Оценки лектора: ')
    student_1.rate_hw(lecturer_1, 'Python', 5)
    student_2.rate_hw(lecturer_1, 'Python', 8)
    student_1.rate_hw(lecturer_2, 'Git', 5)
    student_2.rate_hw(lecturer_2, 'Python', 10)

    student1.grades = {"Python": [8, 9, 10]}
    student2.grades = {"Python": [7, 6, 8]}

    lecturer1.grades = {"Python": [9, 9, 10]}
    lecturer2.grades = {"Python": [8, 7, 9]}

    print('Основная информация о студенте: ')
    print(str(student_1))
    print(str(student_2))

    print('Основная информация о лекторе: ')
    print(str(lecturer_1))
    print(str(lecturer_2))

    print('Основная информация о проверяющем: ')
    print(str(reviewer_1))
    print(str(reviewer_2))

    print(student1 > student2)
    print(student1 == student2)


    print(lecturer1 <= lecturer2)
    print(lecturer1 != lecturer2)
    
    def student_average_py(students, course):
        students_grades_py = []
        for student in students:
            if course in student.grades:
                students_grades_py.extend(student.grades[course])
        if not student.grades[course]:
            return 0
        student_average_py = sum(students_grades_py) / len(students_grades_py)
        return student_average_py

    def lecture_average_py(lectures, course):
        lectures_grades_py
        for lecture in lectures:
            if course in lecture.grades:
                lectures_grades_py.extend(student.grades[course])
        if not lecture.grades[course]:
            return 0
        lecture_average_py = sum(lectures_grades_py) / len(lectures_grades_py)
        return lecture_average_py