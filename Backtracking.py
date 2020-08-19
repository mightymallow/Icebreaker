

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
def run_q3():
    graphs = [rand_graph(0.1, 31), rand_graph(0.2, 31), rand_graph(0.3, 31), rand_graph(0.4, 31), rand_graph(0.5, 31), rand_graph(0.6, 31)]
    for i in range(len(graphs)):
        theVariables = list(graphs[i].keys())
        #print(graphs[i])
        #print("The variables are: " + str(theVariables))
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
            #print(theDomains)
            theProblem = CSP(theVariables, theDomains, graphs[i], different_values_constraint)
            csp_sol = backtracking_search(theProblem)
            #print(csp_sol)
            #print("")
            if csp_sol != None:
                elapsed_time = time.time() - start_time
                if check_teams(graphs[i], csp_sol) == True:
                    #print(graphs[i])
                    print("")
                    print("The number of teams that people were divided into is: " + str(teamCounter(csp_sol)))
                    print("The running time of the solver was: " + str(elapsed_time))
                    print("The number of times CSP variables were assigned was: " + str(theProblem.nassigns))
                    print("The number of times CSP variables were unassigned was: " + str(theProblem.uassigns))
                    break


"""This section was dedicated to debugging and testing"""
#theVariables = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
            
#theDomain = {0: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 1: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 2: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 3: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 4: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 5: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 6: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 7: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 8: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 9: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 10: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 11: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 12: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 13: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 14: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 15: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 16: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 17: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 18: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 19: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 20: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 21: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 22: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 23: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 24: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 25: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 26: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 27: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 28: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], 29: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]}

#theNeighbors = {0: [6, 11, 27], 1: [4, 7, 8, 9, 13, 16, 18, 19], 2: [3, 9, 12, 14, 15, 28], 3: [2, 7, 25, 29], 4: [1, 6, 15, 22], 5: [8, 14, 24, 25, 26], 6: [0, 4, 7, 9, 11, 14, 16, 19, 26, 27, 29], 7: [1, 3, 6, 12, 20, 21, 22], 8: [1, 5, 16, 25, 29], 9: [1, 2, 6, 11, 14, 20, 27], 10: [12, 13, 19, 22, 29], 11: [0, 6, 9, 19], 12: [2, 7, 10, 15, 18, 24, 27], 13: [1, 10], 14: [2, 5, 6, 9, 23], 15: [2, 4, 12, 18, 21, 25, 27], 16: [1, 6, 8], 17: [20, 29], 18: [1, 12, 15, 19, 22, 23, 26], 19: [1, 6, 10, 11, 18, 20, 22, 24, 25, 26, 28], 20: [7, 9, 17, 19, 24, 26, 27], 21: [7, 15, 28], 22: [4, 7, 10, 18, 19, 28], 23: [14, 18, 26], 24: [5, 12, 19, 20], 25: [3, 5, 8, 15, 19, 27, 28], 26: [5, 6, 18, 19, 20, 23, 27], 27: [0, 6, 9, 12, 15, 20, 25, 26, 28], 28: [2, 19, 21, 22, 25, 27], 29: [3, 6, 8, 10, 17]}


#theProblem = CSP(theVariables, theDomain, theNeighbors, different_values_constraint)
#print(min_conflicts(theProblem))
#treeSetup = MapColoringCSP(theVariables, theNeighbors)
#print(tree_csp_solver(treeSetup))
#print(backtracking_search(theProblem))


run_q3()

