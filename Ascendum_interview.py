
# from word2num import 
def starpattern1(n):
    try:

        ###Sample Test 1
        
        # Sample Star Code
        #Star pattern 
        for i in range (0,n):
            if i == 0:
                print('    A    ')
            elif i == 1:
                print('   A B    ')
            elif i == 2:
                print('  A B C  ')
            elif i == 3:
                print(' A B C D ' )
            elif i == 4:
                print('A B C D E')
            # elif i =5:
            #     print('A B C D E')
                 
        for i in range (n):
            if n ==6:
                if i == 5:
                    print('   A    ')
                if i == 4:
                    print('     A B   ')
                elif i == 3:
                    print('    A B C   ' )
                elif i == 2:
                    print('   A B C D   ')
                elif i == 1:
                    print('  A B C D E  ')
                elif i == 0:
                    print('A B C D E F')
            if n ==5:
                if i == 4:
                    print('    A    ')
                elif i == 3:
                    print('   A B   ' )
                elif i == 2:
                    print('  A B C  ')
                elif i == 1:
                    print(' A B C D ')
                elif i == 0:
                    print('A B C D E')
            if n ==4:
                if i == 3:
                    print('    A    ')
                elif i == 2:
                    print('   A B   ' )
                elif i == 1:
                    print('  A B C  ')
                elif i == 0:
                    print(' A B C D ')
            if n ==3:
                if i == 2:
                    print('    A    ')
                elif i == 1:
                    print('   A B   ' )
                elif i == 0:
                    print('  A B C  ')
            if n ==2:
                
                if i == 1:
                    print('    A    ')
                elif i == 0:
                    print('   A B   ' )
            # if n ==1:
            #     if i == 0:
            #         print('A')
            
        
    except Exception as e:
        print(e)
        
        
def starpattern(n):
    try:
        ###Sample Test2
        # Star pattern Code         
        alphabet = [chr(i) for i in range(65, 65 + n)]        
        
        for i in range(n):
            print(" " * (n - i - 1) + " ".join(alphabet[:i+1]))        
       
        for i in range(n - 2, -1, -1):
            print(" " * (n - i - 1) + " ".join(alphabet[:i+1]))        

    except Exception as e:
        print(e)



# def 
        
n = 5
starpattern(n)
# starpattern1(n)
