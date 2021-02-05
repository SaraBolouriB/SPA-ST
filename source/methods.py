def generate_Ljk(students_pref, lecturers_pref, offers, number_of_lect):
    L_jk = {}

    for lecturer in range(number_of_lect):
        L_jk[lecturer] = {}

        for project in offers[lecturer]:
            L_jk[lecturer][project] = []

            for student in lecturers_pref[lecturer]:
                if project in students_pref[student]:
                    L_jk[lecturer][project].append(student)
            

    return L_jk

def calculate_alpha(project_capacity, Gp, projects):
    alpha = 0
    for project in projects:
        c = project_capacity[project]
        dG = len(Gp[project])
        alpha += min(c, dg)
    return alpha