import math
'''Calculate distance using Euclidean distance 
distance calculation
        parameters (list1, list2 , methodType)
        example : list1 = [(2,5),(3,7),(4,8)
        list2 = (5,10)
        methodType = 'Old' or methodType = 'New'
        and return the output as both min and max values (min,max)
        '''
def distance_calculation(self,list1, list2, methodType):
    distances = [calculate_distance(point, list2, methodType) for point in list1]
    return min(distances),max(distances)

def calculate_distance(self,point1, point2 ,val):   
    if val != 'Old': 
        return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    else:
        return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5