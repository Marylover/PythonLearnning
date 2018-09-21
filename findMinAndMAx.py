def findMinAndMax(L):
        if len(L) != 0:
                max = L[0] 
                min = L[0]
        else：
            return(None,None)
        for num in L:
             if max <= num :
                 max = num
             if min >= num :                                                                                    min = num                                                                             return (min,max)
