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

def initialization_list(length):
    init = {}
    for i in range(length):
        init[i] = []
    return init

def calculate_alpha(projects_capacity, Gp, projects):
    '''
        alpha = SIGMA(qj of each project)
        qj = min(capacity of pj, number of student provisionally assigned to pj)
    '''
    alpha = 0
    for project in projects:
        c = projects_capacity[project]              #Capacity of project
        dG = len(Gp[project])                       #Number of student provisionally assigned to project
        alpha += min(c, dg)                         #SIGMA(qj of each project)  
    return alpha

def dominated_Lk(alpha, lecturer_capacity, lecturer_pref, Gl, lecturer):
    dG = len(Gl)
    students = []
    if min(alpah, dG) >= lecturer_capacity:
        last_stu = to_list(lecturer_pref.pop())      
        for ls in last_stu:
            if ls in Gl[lecturer]:
                students.append(ls)     
    return students

def dominated_Lkj(Ljk, lecturer, project, Gp):
    last_stu = to_list(Ljk[lecturer][project].pop())
    students = []
    for ls in last_stu:
        if ls in Gp[project]:
            students.append(ls)
    return students
        
def lecturer_proposed(offers):
    '''
        For each project, its lecturer is assigned
    '''
    project_offered = {}
    i = 0
    for offer in offers:
        for p in offer:
            project_offered[p] = i

        i += 1
    
    return project_offered

def to_list(date):
    if type(date) == tuple:
        return list(data)
    else:
        dataL = []
        dataL.append(date)
        return dataL
    
def intersection(A, B):
    intersection = []
    for a in A:
        for b in B:
            intersection.append(b) if a == b else None

def reduce_graph(graph, project_lecturer, lecturers_pref, Ljk, Gp, Gl, projects_capacity, lecturers_capacity):
    projects_capacity_copy = list(projects_capacity)
    lecturers_capacity_copy = list(lecturers_capacity)
    for student in graph:
        for project in student:
            lecturer=project_lecturer[project]
            is_bounded = bounded_edge(student=student, project=project, lecturer=lecturer,
                                        Lk=lecturers_pref[lecturer], Ljk=Ljk, Gp=Gp, Gl=Gl, 
                                        projects_capacity=projects_capacity, lecturers_capacity=lecturers_capacity)
            if is_bounded:
                graph[student].remove(project)
                Gp[project].remove(student)
                Gl[lecturer].remove(student)
                projects_capacity_copy[project] -= 1
                lecturers_capacity_copy[lecturer] -= 1
                #Remove all unbounded edge
            if not graph[student]:
                del graph[student]      #Isolated vertex(student)
            
            if not Gp[project]:
                del Gp[project]
            
            #It's not complete
            pass
            

def bounded_edge(student, project, lecturer, Lk, Ljk, Gp, Gl, projects_capacity, lecturers_capacity):

    oversubscribed = True if len(Gp[project]) > project_capacity[project] else False
    in_tail_Ljk = True if student == Ljk[lectrur][project].pop() else False
    in_tail_Lk = True if student == Lk[lecturer].pop() else False

    alpha = calculate_alpha(projects_capacity=projects_capacity, Gp=Gp, projects=project)   # ??
    is_lower_edge = lower_edge( student=student, project=project, lecturer=lecturer, Lk=Lk,
                                Gl=Gl, alpha=alpha, lecturers_capacity=lecturers_capacity) 

    if not oversubscribed and not in_tail_Ljk:
        if not is_lower_edge and not in_tail_Lk:
            return True
    return False

def lower_edge(student, project, lecturer, Lk, Gl, alpha, lecturers_capacity):
    in_tail_Lk = True if student == Lk[lecturer].pop() else False
    check = True if min(len(Gl[lecturer]), alpha) > lecturers_capacity[lecturer] else False

    return True if in_tail_Lk and check else False

def find_critical_set(students):
    pass

