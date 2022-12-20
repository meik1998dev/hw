from django.shortcuts import render
from django.contrib import messages
from copy import deepcopy
import numpy as np
import time
 #************************************************


#************************************************
 
def home(request):
   
    context={
        'title':'plane',
        
    }
    
    return render(request , 'blog/index.html',context)




 
















# ----------  Program start -----------------





def solve (request):
            
    # takes the input of current states and evaluvates the best path to goal state - يأخذ مدخلات الحالات الحالية ويقيم أفضل مسار إلى حالة الهدف
    def bestsolution(state):
        bestsol = np.array([], int).reshape(-1, 9)
        count = len(state) - 1
        while count != -1:
            bestsol = np.insert(bestsol, 0, state[count]['puzzle'], 0)
            count = (state[count]['parent'])
        return bestsol.reshape(-1, 3, 3)

        
    # this function checks for the uniqueness of the iteration(it) state, weather it has been previously traversed or not. - تتحقق هذه الوظيفة من تفرد حالة التكرار  ، سواء تم اجتيازها مسبقًا أم لا.
    def all(checkarray):
        set=[]
        for it in set:
            for checkarray in it:
                return 1
            else:
                return 0


    # calculate Manhattan distance cost between each digit of puzzle(start state) and the goal state- احسب تكلفة المسافة في مانهاتن بين كل رقم من أرقام اللغز (حالة البداية) وحالة الهدف
    def manhattan(puzzle, goal):
        a = abs(puzzle // 3 - goal // 3)
        b = abs(puzzle % 3 - goal % 3)
        mhcost = a + b
        return sum(mhcost[1:])




    # will calcuates the number of misplaced tiles in the current state as compared to the goal state-سيحسب عدد المربعات الخاطئة في الحالة الحالية مقارنة بحالة الهدف
    def misplaced_tiles(puzzle,goal):
        mscost = np.sum(puzzle != goal) - 1
        return mscost if mscost > 0 else 0
        


    #3[on_true] if [expression] else [on_false] 


    # will indentify the coordinates of each of goal or initial state values-سيحدد إحداثيات كل هدف أو قيم الحالة الأولية
    def coordinates(puzzle):
        pos = np.array(range(9))
        for p, q in enumerate(puzzle):
            pos[q] = p
        return pos



    # start of 8 puzzle evaluvation, using Manhattan heuristics -بداية تقييم 8 لعبة باستخدام استدلال مانهاتن
    def evaluvate(puzzle, goal):
            steps = np.array([('up', [0, 1, 2], -3),('down', [6, 7, 8],  3),('left', [0, 3, 6], -1),('right', [2, 5, 8],  1)],
            dtype =  [('move',  str, 1),('position', list),('head', int)])

            dtstate = [('puzzle',  list),('parent', int),('gn',  int),('hn',  int)]
            
            # initializing the parent, gn and hn, where hn is manhattan distance function call  -gn و hn ، حيث hn هو استدعاء دالة المسافة في مانهاتن
            costg = coordinates(goal)
            parent = -1
            gn = 0
            hn = manhattan(coordinates(puzzle), costg)
            state = np.array([(puzzle, parent, gn, hn)], dtstate)

        # We make use of priority queues with position as keys and fn as value.0-   نحن نستخدم قوائم الانتظار ذات الأولوية مع الموضع كمفاتيح و fn كقيمة.
            dtpriority = [('position', int),('fn', int)]
            priority = np.array( [(0, hn)], dtpriority)



            while 1:
                priority = np.sort(priority, kind='mergesort', order=['fn', 'position'])     
                position, fn = priority[0]                                                 
                priority = np.delete(priority, 0, 0)  
                # sort priority queue using merge sort,the first element is picked for exploring remove from queue what we are exploring     -فرز قائمة انتظار الأولوية باستخدام دمج الفرز ، يتم اختيار العنصر الأول لاستكشاف إزالة ما نستكشفه من قائمة الانتظار              
                puzzle, parent, gn, hn = state[position]
                puzzle = np.array(puzzle)
                # Identify the blank square in input  -حدد المربع الفارغ في الإدخال
                blank = int(np.where(puzzle == 0)[0])       
                gn = gn + 1                              
                c = 1
                start_time = time.time()
                for s in steps:
                    c = c + 1
                    if blank not in s['position']:
                        # generate new state as copy of current -توليد حالة جديدة كنسخة الحالية
                        openstates = deepcopy(puzzle)                   
                        openstates[blank], openstates[blank + s['head']] = openstates[blank + s['head']], openstates[blank]             
                        # The all function is called, if the node has been previously explored or not  -  يتم استدعاء وظيفة الكل ، إذا تم استكشاف العقدة مسبقًا أم لا
                        if ~(np.all(list(state['puzzle']) == openstates, 1)).any():    
                            end_time = time.time()
                            if (( end_time - start_time ) > 2):
                                print(" The 8 puzzle is unsolvable ! \n")
                                exit 
                            # calls the manhattan function to calcuate the cost - يستدعي دالة مانهاتن لحساب التكلفة
                            hn = manhattan(coordinates(openstates), costg)    
                            # generate and add new state in the list -توليد وإضافة حالة جديدة في القائمة                    
                            q = np.array([(openstates, position, gn, hn)], dtstate)         
                            state = np.append(state, q, 0)
                            # f(n) is the sum of cost to reach node and the cost to rech fromt he node to the goal state
                            #f (n) هو مجموع تكلفة الوصول إلى العقدة وتكلفة الوصول   إلى حالة الهدف
                            fn = gn + hn                                        
                    
                            q = np.array([(len(state) - 1, fn)], dtpriority)    
                            priority = np.append(priority, q, 0)
                            # Checking if the node in openstates are matching the goal state.- التحقق مما إذا كانت العقدة في الحالة المفتوحة تطابق حالة الهدف.  
                            if np.array_equal(openstates, goal):                              
                                print(' The 8 puzzle is solvable ! \n')
                                return state, len(priority)
                
                                
            return state, len(priority)




    # ----------  Program start -----------------


    # User input for initial state 
    puzzle = []
    node0 =int(request.POST['b0'])
    puzzle.append( (node0))
    node1 =int(request.POST['b1'])
    puzzle.append( (node1))
    node2 =int(request.POST['b2'])
    puzzle.append( (node2))
    node3 =int(request.POST['b3'])
    puzzle.append( (node3))
    node4 =int(request.POST['b4'])
    puzzle.append( (node4))
    node5 =int(request.POST['b5'])
    puzzle.append( (node5))
    node6 =int(request.POST['b6'])
    puzzle.append( (node6))
    node7 =int(request.POST['b7'])
    puzzle.append( (node7))
    node8 =int(request.POST['b8'])
    puzzle.append( (node8))
   

    # User input of goal state       
    goal = []
    node00 =int(request.POST['b00'])
    goal.append( (node00))
    node11 =int(request.POST['b11'])
    goal.append( (node11))
    node22 =int(request.POST['b22'])
    goal.append( (node22))
    node33 =int(request.POST['b33'])
    goal.append( (node33))
    node44 =int(request.POST['b44'])
    goal.append( (node44))
    node55 =int(request.POST['b55'])
    goal.append( (node55))
    node66 =int(request.POST['b66'])
    goal.append( (node66))
    node77 =int(request.POST['b77'])
    goal.append( (node77))
    node88 =int(request.POST['b88'])
    goal.append( (node88))
 

     # User input for initial state 

 
    goal2=goal
    puzzle2=puzzle
    n =1
    a=[] 
     
    if(n == 1 ):

        state, visited = evaluvate(puzzle2, goal2) 
        bestpath = bestsolution(state)
        arr= str(bestpath).replace('[', ' ').replace(']', '')
        print('arr---------------------')
        print(arr)
        a=arr.split('\n')

        totalmoves = len(bestpath) - 1
        print('Steps to reach goal:',totalmoves)
        visit = len(state) - visited
        print('Total nodes visited: ',visit, "\n")
        print('Total generated:', len(state))
 
 
    # ----------  Program End ----------------- python manage.py runserver
     
    context={
        'title':'Solve',
        'node0':puzzle[0],
        'node1':puzzle[1],
        'node2':puzzle[2],
        'node3':puzzle[3],
        'node4':puzzle[4],
        'node5':puzzle[5],
        'node6':puzzle[6],
        'node7':puzzle[7],
        'node8':puzzle[8],
        
        'node00':goal[0],
        'node11':goal[1],
        'node22':goal[2],
        'node33':goal[3],
        'node44':goal[4],
        'node55':goal[5],
        'node66':goal[6],
        'node77':goal[7],
        'node88':goal[8],
        
        'Steps':totalmoves,
        'visit':visit,
        'generated':len(state),
        'arr0':a,
          
    }
    print(arr)
    return render(request , 'blog/solve.html',context)

