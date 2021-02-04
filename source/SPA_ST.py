def spa_st(Ss, Pp, Ll, studens_pref, lecturers_pref, offers, project_capacity, lecturer_capacity):

    #Variables ------------------------------------------------------------------------------
    studens_pref_copy = list(studens_pref)
    lecturers_pref_copy = list(lecturers_pref)

    number_of_stu = len(Ss)                                 #Number of student
    number_of_lect = len(Ll)                                #Number of lecturer
    number_of_proj = len(Pp)                                #Number of project

    s_to_p = initialization(number_of_stu)                  
    p_to_s = initialization(number_of_proj)     
    l_to_s = initialization(number_of_lect) 

    LP_to_s = lp_initialization(number_of_lect, offers)

    lecturerC, projectC = [], []

    graph = [[-1] for row in range(lenS)]       #Primary Graph
    
    for i in range(number_of_stu):
        if not s_to_p[i]:




    
            



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
    project_offered = []
    for offer in offers:
        for p in offer:
            project_offered.append(p)
    
    return project_offered