import math
'''Calculate distance using Euclidean distance formula'''

def calculate(list1, list2, methodType):
    ''' parameters (list1, list2 , methodType)
        example : list1 = [(2,5),(3,7),(4,8)
                  list2 = (5,10)
                  methodType = 'Old' or methodType = 'New'
                  if methodType is 'Old', means calculate step by step without using math package
        and return the output as both min and max values (min,max)'''
    distances = [__calculate_distance(point, list2, methodType) for point in list1]
    return min(distances),max(distances)

def __calculate_distance(point1, point2 ,val): 
    '''private method not to refer for calucate distance'''  
    if val != 'Old': 
        return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    else:
        return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5