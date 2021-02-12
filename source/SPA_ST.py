from methods import *

def spa_st(Ss, Pp, Ll, students_pref, lecturers_pref, offers, projects_capacity, lecturers_capacity):
    '''
        students_pref  --> dictionary
        lecturers_pref --> dictionary
        offers, projects_capacity, lecturers_capacity --> List
    '''

    #Variables -------------------------------------------------------------------------------------------
    students_pref_copy = students_pref.copy()               #Copy of student preference list
    lecturers_pref_copy = lecturers_pref.copy()             #Copy of lecturer preference list
    project_lecturer = lecturer_proposed(offers=offers)     #Show which professor proposed each project

    number_of_stu = len(Ss)                                 #Number of student
    number_of_lect = len(Ll)                                #Number of lecturer
    number_of_proj = len(Pp)                                #Number of project
                
    Gp = [[] for row in range(number_of_proj)]    
    Gl = [[] for row in range(number_of_lect)]                     
    graph = [[] for row in range(number_of_stu)]            #Primary Graph
    
    Ljk = generate_Ljk( students_pref=students_pref, 
                        lecturers_pref=lecturers_pref,
                        offers=offers, 
                        number_of_lect=number_of_lect)

    lecturerC, projectC = [0 for i in range(number_of_lect)], [0 for i in range(number_of_proj)
    project_replete, lecturer_replete = [], []
    ## ----------------------------------------------------------------------------------------------------

    while True:
        while True:
            while bool(students_pref_copy):                             #Whether all student assigened or not
                student_info = students_pref_copy.popitem()             #Remove last student of list. return -> (key,value)
                student = student_info[0]                               #Key   -> student index 
                student_projectList = student_info[1]                   #Value -> preferences list of student

                if student_projectList:
                    head_project = to_list(student_projectList.pop(0))  #Thefirst preference, it may be just one project or tuple(tie) 
                    
                    for project in head_project:
                        lecturer = project_lecturer[project]            #Find lecturer who proposed the project
                        graph[student].append(project)
                        #Update Variables -------------------------------------------------------------------
                        Gp[project].append(student)
                        Gl[lecturer].append(student)
                        lecturerC[lecturer] += 1
                        projectC[project] += 1
                        ##-----------------------------------------------------------------------------------
                        if projects_capacity[project] <= projectC[project]:
                            project_replete.append(project)             #Add project to replete list
                            alpha = calculate_alpha(projects_capacity=projects_capacity, Gp=Gp, projects=offers[lecturer])
                            dominated_students = dominated_Lkj(Ljk=Ljk, lecturer=lecturer, project=project, Gp=Gp)
                            for ds in dominated_students:
                                if project in graph[ds]:
                                    graph[ds].remove(project)
                                    Gp[project].remove(ds)
                                    Gl[lecturer].remove(ds)
                                    lecturerC[lecturer] -= 1
                                    projectC[project] -= 1

                        if lecturer_capacity[lecturer] <= lecturerC[lecturer]:
                            lecturer_replete.append(lecturer)
                            alpha = calculate_alpha(projects_capacity=projects_capacity, Gp=Gp, projects=offers[lecturer])
                            dominated_students = dominated_Lk( alpha=alpha,
                                                                lecturer_capacity=lecturers_capacity[lecturer],
                                                                lecturer_pref=lecturers_pref[lecturer],
                                                                Gl=Gl,
                                                                lecturer=lecturer)
                            for ds in dominated_students:
                                intersection_projects = intersection(A=students_pref[ds], B=offers[lecturer])
                                for p in intersection_projects:
                                    if p in graph[ds]:
                                        graph[ds].remove(p)
                                        Gp[project].remove(ds)
                                        Gl[lecturer].remove(ds)
                                        lecturerC[lecturer] -= 1
                                        projectC[project] -= 1
                
            Gr = reduce_graph(graph=graph)              #Reduce graph
            Z = find_critical_set(students=Ss)          #Crtical set   

            for project in Z:
                lecturer = project_lecturer[project]
                L_u_k = to_list(Ljk[lecturer][project]) 
                for student in L_u_k:
                    if project in graph[student]:
                        graph[student].remove(project)
                        Gp[project].remove(student)
                        Gl[lecturer].remove(student)
                        lecturerC[lecturer] -= 1
                        projectC[project] -= 1

            if not Z:                                   #Break form seconf infinitive loop
                break   

            for p in Pp:
                undersubscribed = True if len(Gp[P]) < projects_capacity[p] else False
                if p in project_replete and undersubscribed:
                    lecturer = project_lecturer[p]
                    sr = None # Sr ???
                    lec_pre = lecturers_pref[lecturer]
                    last_pre_index = len(lec_pre) - 1
                    Sr_index = lec_pre.index(sr)
                    if Sr_index < last_pre_index:
                        last_stu = to_list(lec_pre.pop())
                        for student in lec_pre:
                            intersection_projects = intersection(A=students_pref[student], B=offers[lecturer])
                            for p in intersection_projects:
                                if p in graph[student]:
                                    graph[student].remove(p)
                                    Gp[p].remove(student)
                                    Gl[lecturer].remove(student)
                                    lecturerC[lecturer] -= 1
                                    projectC[p] -= 1
    student = 0
    for student_list in graph:
        for project in student_list:        
            alpha = calculate_alpha(projects_capacity=projects_capacity, Gp=Gp, projects=student_list)
            is_lower_edge = lower_edge( student=student, project=project,
                                        lecturer=lecturer_proposed[project], Lk=lecturers_pref, 
                                        Gl=Gl, alpha=alpha, lecturers_capacity=lecturers_capacity)
            if is_lower_edge:
                lecturer = lecturer_proposed[project]
                # unbounded edge 
                # for on each unbounded edge
    M = feasible_mathching()
    if strong_matching(M=M):
        return M
    else:
        print("no strongly stable matching exist")
    