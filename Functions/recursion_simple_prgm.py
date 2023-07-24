def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
(tri_recursion(5))






#
# def tri_recursion(5):
#     result = 5 + def tri_recursion(4):
#                       result = 4 + def tri_recursion(3):
#                                       result = 3 + def tri_recursion(2):
#                                                       result = 2 + def tri_recursion(1):
#                                                                          result = 1 + def tri_recursion(0):
#                                                                                        result = 0
#                                                                                        return result
#                                                                          return result
#                                                       return result
#                                       return result
#                       return result
#     return result