

from csp import *
import time


#creates a random graph
def rand_graph(p,n):
    my_dict = {}
    for i in range(n):
        my_dict[i] = []
        for j in range(n):
            if i == j:
                continue
            if j < i and i in my_dict.get(j):
                my_dict[i].append(j)
                continue
            if j > i and decision(p) == True:
                my_dict[i].append(j)
    return my_dict


#random probability
def decision(probability):
    return random.random() < probability


#checks to see if the solution agrees with the graph
def check_teams(graph, csp_sol):
    passedTest = True
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            friendTestSpot = graph.get(i)[j]
            if csp_sol[i] == csp_sol[friendTestSpot]:
                passedTest = False
                break
        if passedTest == False:
            return False
    return True


#counts how many teams are created
def teamCounter(csp_sol):
    groupIDs = []
    counter = 0
    for i in range(len(csp_sol)):
        if csp_sol.get(i) not in groupIDs:
            groupIDs.append(csp_sol.get(i))
            counter += 1
    return counter


#creates 6 random graphs, then runs CSP problem by increasing the domain by 1 each time if the domain is not large enough to find a solution (returns None)
def run_q4():
    graphs = [rand_graph(0.1, 105), rand_graph(0.2, 105), rand_graph(0.3, 105), rand_graph(0.4, 105), rand_graph(0.5, 105), rand_graph(0.6, 105)]
    for i in range(len(graphs)):
        theVariables = list(graphs[i].keys())
        #print(theVariables)
        listLength = len(theVariables)
        theDomains = {}
        theSubDomains = []
        for j in range(listLength):
            theDomains[j] = []
        start_time = time.time()
        for k in range(listLength):
            theSubDomains.append(k)
            for l in range(listLength):
                theDomains[l] = theSubDomains
            theProblem = CSP(theVariables, theDomains, graphs[i], different_values_constraint)
            csp_sol = min_conflicts(theProblem)
            #print(csp_sol)
            #print("")
            if csp_sol != None:
                elapsed_time = time.time() - start_time
                if check_teams(graphs[i], csp_sol) == True:
                    #print(graphs[i])
                    print("")
                    print("The running time of the solver was: " + str(elapsed_time))
                    print("The number of teams that people were divided into is: " + str(teamCounter(csp_sol)))
                    print("The number of times CSP variables were assigned was: " + str(theProblem.nassigns))
                    print("The number of times CSP variables were unassigned was: " + str(theProblem.uassigns))
                    break


run_q4()

