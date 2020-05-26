class MyClass:
    '''This class contains random numbers generation and ispalindrome functions'''
    def randomNumbers(N, lb, ub):
        import random
        res = [random.randint(lb, ub+1) for var in range(N)]
        return res
    
    def ispalindrome(S):
        if(S == S[::-1]):
            return True
        else:
            return False