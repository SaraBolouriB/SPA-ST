def spa_st(Ss, Pp, Ll, students_pref, lecturers_pref, offers, projects_capacity, lecturers_capacity):

    #Variables --------------------------------------------------------------------------------------
    students_pref_copy = list(students_pref)
    lecturers_pref_copy = list(lecturers_pref)
    project_lecturer = lecturer_offers(offers=offers)

    number_of_stu = len(Ss)                                 #Number of student
    number_of_lect = len(Ll)                                #Number of lecturer
    number_of_proj = len(Pp)                                #Number of project

    Gs = initialization(number_of_stu)                  
    Gp = initialization(number_of_proj)     
    Gl = initialization(number_of_lect) 
    LP_to_s = lp_initialization(number_of_lect, offers)
    Ljk = 

    graph = [[-1] for row in range(lenS)]       #Primary Graph
    ## -----------------------------------------------------------------------------------------------
    lecturerC, projectC = [0 for i in range(number_of_lect)], [0 for i in range(number_of_proj)
    project_replete, lecturer_replete = [], []

    for student in range(number_of_stu):
        if not Gs[student] and not studens_pref_copy[student]:
            head_project = studens_pref_copy[student].pop(0)

            if type(head_project) == tuple:     #Is it tie?
                lenL = len(head_project)
            else:
                lenL = 1
            
            for project in range(lenL):
                lecturer = project_lecturer[project]
                graph[student] = project
                #Update Lists -------------------------------------------------------------------------
                Gs[student] = project
                Gp[project] = student
                Gl[lecturer] = student
                ##-------------------------------------------------------------------------------------
                if project_capacity[project] <= projectC[project]:
                    project_replete.append(project)
                    alpha = calculate_alpha(project_capacity, Gp, offers[lecturer])
                    check_domained = 
                    pass

                if lecturer_capacity[lecturer] <= lecturerC[lecturer]:
                    lecturer_replete.append(lecturer)
                    alpha = calculate_alpha(project_capacity, Gp, offers[lecturer])
                    dominated_students = dominated( alpha=alpha,
                                                    assign_students=list(Gl[lecturer]), 
                                                    lecturer_capacity=lecturers_capacity[lecturer], 
                                                    students=lecturers_pref[lecturer])
                                                    
                



def dominated(alpha, assign_students, lecturer_capacity, students):
    dG = len(assign_students)
    if min(alpah, dG) >= lecturer_capacity:
        for pref_stu in students:





                                



def initialization(length):
    init = {}
    for i in range(length):
        init[i] = []
    return init

def lp_initialization(lengthL, offers):
    init = {}
    for i in range(length):
        init[i] = {}
        projects = offers[i]
        for pro in projects:
            init[i][pro] = []
    return init

def lecturer_offers(offers):
    project_offered = {}
    i = 0

    for offer in offers:
        for p in offer:
            project_offered[p] = i

        i += 1
    
    return project_offered