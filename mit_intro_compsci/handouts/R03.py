example = int(raw_input('Example number: '))

## EXAMPLE 1: Review of Tuples
if example == 1:
    # Tuples may have any type of element in them -
    #  strings, ints, floats, other tuples or other lists
    tupA = ( 1 , 'apple' , 6.00 )
    tupB = ( tupA , 'MIT', [4, 5] )

    print 'tupA is' , tupA , 'with length:' , len(tupA)
    print 'tupB is' , tupB , 'with length:' , len(tupB)

    print '\nIndexing Operation:'
    print 'tupA[0] is: ', tupA[0]
    print 'tupA[2] is: ', tupA[2]
    #print 'tupA[3] is: ', tupA[3] # Error - why?
    print 'tupB[0] is: ', tupB[0]
    print 'tupB[0][1] is: ', tupB[0][1]
    print 'tupB[-1] is: ', tupB[-1]

    print '\nSlicing operation: '
    print 'tupA[0:1] is: ', tupA[0:1]
    print 'tupA[0:100] is: ', tupA[0:100]
    print 'tupA[0:2] is: ', tupA[0:2]
    print 'tupA[:2] is: ', tupA[:2]
    print 'tupA[1:] is: ', tupA[1:]
    print 'tupA[:] is: ', tupA[:]
    print 'tupB[-1:-3] is: ', tupB[-1:-3]
 
    # Iteration through tuple
    print "\nIteration through tupB"
    for item in tupB:
        print item,'is of type', type(item)

    # this is equivalent to
    print '\nIteration through tupB:'
    for i in range(len(tupB)):
        print tupB[i],'is of type', type(tupB[i])
        
## EXAMPLE 2: Review of Tuples
if example == 2:
        
    listA = [ 0.234 , 'apple' , (1,2) , 77 ]
    listB = ( listA , 'MIT' , [3,1,4] )

    print 'list A is' ,listA, 'with length:', len(listA)
    print 'list B is' ,listB, 'with length:', len(listB)

    print '\nIndexing operation:'
    print 'listA[0] is:', listA[0]
    print 'listA[3] is:', listA[3]
    #print 'listA[4] is:', listA[3] # Error -why?
    print 'listB[0[ is:', listB[0]
    print 'listB[0][1] is:', listB[0][1]
    print 'listB[-1] is: ', listB[-1]

    print '\nSlicing operation:'
    print 'listA[0:1] is: ', listA[0:1]
    print 'listA[0:100] is: ', listA[0:100]
    print 'listA[0:2] is: ', listA[0:2]
    print 'listA[:2] is: ', listA[:2]
    print 'listA[1:] is: ', listA[1:]
    print 'listA[:] is: ', listA[:]
    print 'listB[-1:-3] is: ', listB[-1:-3]\

    # Iteration through list
    print '\nIteration through list'
    for item in listB:
        print item,'is of type', type(item)

    # access inner list
    print '\nAccess inner list'
    L = [[ 'MIT' , 'Harvard' ] , [ 'universities' ] , 0 ]
    print 'In list', L
    print 'L[0][1] is', L[0][1]

    print '\n Matrix'
    # create a matrix
    M = [ [0,1] , [1,2] , [2,3] , [3,4] ]
    print M

## EXAMPLE 3  List operations
if example == 3:

    LA = [ 6.00 , 'MIT' , 600 , 600 ]
    LA.append('Harvard')
    print LA

    LA.append(['Yale','Stanford'])
    print LA

    LA.pop() # pop off the last element
    print LA
    LA.pop(0) # pop off element at index 0
    print LA

    LA.extend(['Yale','Stanford'])
    print LA

    LA.remove(600)
    print LA

    #LA.remove(500) # Error
    if 500 in LA:
        LA.remove(500) # Error

    LA.sort()
    print LA

## EXAMPLE 4: Immutability vs. mutability, aliasing
if example == 4:

    tupA = ( 1  , 'apple' , 6.00 )

    listA = [ 0.234 , 'apple' , (1,2) , 77 ]
    listB = [ listA , 'MIT' , [3,1,4] ]

    # Since tuples are immutable, cannot reassign
    #tupA[0] = 3 # This gives an error

    # Lists are mutable!
    print 'listA is:', listA
    print 'listB is:', listB
    listA[0] = 88
    print 'Now listA is:', listA

    # Aliasing givving two names to the same list - pinting
    # the same list
    listX = [ 1 , 4 , 5 ]
    listY = listX
    print "listX is:",listX,'and listY is:',listY
    listX[0] = 'banana'
    print 'listX is:',listX,'and listY is:',listY

    # Aliasing happens when we define a list (like listA, a)
    # and put it inside another list. We canhged listA[0]
    # Since listA was a member of listB, now listB will have
    print 'listB is now:',listB

    # To copy without aliasing use a full slice
    listX = [ 1 , 4 , 5 ]
    listY = listX
    listZ = listX[:] # Full slice!
    print 'listX is:',listX,', listY is:',listY,', listZ is:',listZ
    listX[0] = 'banana'
    print 'listX is:',listX,', listY is:',listY,', listZ is:',listZ

# EXAMPLE 5: casting to list & tuples
if example == 5:
    # Can easily change mutability properties by casting a list --> tuple
    #  or tuple --> list
    # We can cast a tuple to list to change it
    test_tuple = (1, 4, 'apple', 'ziggle')
    print 'test_tuple is', test_tuple
    # Cast the tuple into a list
    tuple_into_list = list(test_tuple)
    print 'I cast it to a list - now it is of type', type(tuple_into_list)
    # Change an element of the list
    tuple_into_list[3] = 'banana'
    # Cast back into a tuple
    test_tuple = tuple(tuple_into_list)
    print 'now test_tuple is', test_tuple
    print '     which is of type',type(test_tuple)

# EXAMPLE 6: dictionaries
if example == 6:
    staff = {'Mitchell' :   'mizhi@mit.edu',
             'Ryan'     :   'rwx@mit.edu',
             'Sarina'   :   'sarina@mit.edu'}
    print len(staff)

    # Made a mistake! Fix Ryan's address
    staff['Ryan'] = 'rwj@mit.edu'
    # Add Heymian
    staff['Heymian'] = 'heymian@mit.edu'

    if 'Heymian' in staff:
        print 'Heymian is in the staff list!'
    if 'Gartbee' not in staff:
        print 'Adding Gartbee to the staff list'
        staff['Gartbee'] = 'gartbee@mit.edu'

    # Can't check for values with the 'in' keyword, only key
    print 'rwj@mit.edu' in staff

    # Order we added doesn't matter; is unordered when we
    print staff

    # One way to order, alphabetically
    staff.keys().sort()
    print staff
    keys = staff.keys()
    keys.sort()
    print keys
    for k in keys:
        print k,',',staff[k]

    # Oops, we fired Sarina!
    del staff['Sarina']
    print staff

    # go through key, value pairs
    for TA, Email in staff.items():
        print 'TA', TA,' can be contacted at', Email

# EXAMPLE 7: Recursion
if example == 7:
    # How might we make a factorial function?

    def factorial(n):
        # if [base case is true] - what is the base case?
        if n == 0:
            # 0! is 1
            return 1
        else:
            return n*factorial(n-1)

    # Test!
    print factorial(0)
    print factorial(5)

    def febo(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return febo(n-1)+febo(n-2)
    i = 0
    lst = []
    x = int(raw_input('value'))
    while i <= x:
        
        lst.append(febo(i))
        i += 1
    print lst

    # Can you write this using while loop?

if example == 8:

    def rec_exponentiation(b,e):
        if e == 0:
            return 1
        else:
            return b*rec_exponentiation(b, e-1)
    # Test!
    print rec_exponentiation(3,0)
    print rec_exponentiation(3,3)

if example == 9:
    # Hanoi exanple
    def hanoi(n,s,t,b):
        assert n > 0
        if n == 1:
            print 'move',s,'to',t
        else:
            hanoi(n-1,s,b,t)
            hanoi(1,s,t,b)
            hanoi(n-1,b,t,s)
    for i in range(1,5):
        print 'New Hanoi Example: hanoi(',i,',source, target, buffer)'
        print '----------------------'
        hanoi(i,'source','target','buffer')

    
