n = int(input())

def calculate_sort_weight(student, dep_name):
    weighted_mark = 0
    if dep_name == "Physics":
        weighted_mark = (student["physics_mark"] + student["math_mark"])/2
    elif dep_name == "Chemistry":
        weighted_mark = student["chemistry_mark"]
    elif dep_name == "Mathematics":
        weighted_mark = student["math_mark"]
    elif dep_name == "Engineering":
        weighted_mark = (student["cs_mark"] + student["math_mark"]) / 2
    elif dep_name == "Biotech":
        weighted_mark = (student["chemistry_mark"] + student["physics_mark"]) / 2
    else:
        return None
    return max(student["special_mark"], weighted_mark)

students = []
with open('applicants.txt', "r") as fin:
    for line in fin.readlines():
        name, surname, physics_mark, chemistry_mark, math_mark, cs_mark, special_mark, dep1, dep2, dep3 = line.split()
        student = {"name": name + " " + surname, "physics_mark": float(physics_mark),
                   "chemistry_mark": float(chemistry_mark), "math_mark": float(math_mark),
                   "cs_mark": float(cs_mark), "special_mark": float(special_mark), "dep1": dep1, "dep2": dep2, "dep3": dep3}
        students.append(student)

accepted_students = []
departments_with_students = dict()

for priority in range(1, 4):

    dep_name = "dep" + str(priority)

    students.sort(key=lambda x: (x[dep_name], -calculate_sort_weight(x, x[dep_name]), x["name"]))

    department_list = []
    for student in students:
        if student[dep_name] not in department_list:
            department_list.append(student[dep_name])

    department_list.sort()

    for dep in department_list:
        if dep in departments_with_students:
            list_of_students = departments_with_students[dep]
        else:
            list_of_students = []

        best_students_of_dep = [x for x in students if x[dep_name] == dep]
        count = len(list_of_students)
        for student in best_students_of_dep:
            if count == n:
                break
            student_elem = {"name": student["name"], "mark": calculate_sort_weight(student, dep)}
            if dep in departments_with_students:
                departments_with_students[dep].append(student_elem)
            else:
                departments_with_students[dep] = [student_elem]

            students.remove(student)

            count += 1

for dep, list_of_students in departments_with_students.items():
    with open(dep + ".txt", "w") as fout:
        # print(dep, file=fout)
        list_of_students.sort(key=lambda x: (-x["mark"], x["name"]))
        for elem in list_of_students:
            print(elem["name"], elem["mark"], file=fout)

