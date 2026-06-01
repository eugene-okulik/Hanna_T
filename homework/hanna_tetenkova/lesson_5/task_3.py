students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_str = ', '. join(students)
subjects_str = ', '.join(subjects)

##my_text = 'Students ' + students_str + ' study these subjects: ' + subjects_str
my_text = f'Students {students_str} study these subjects: {subjects_str}'

print(my_text)
