'''Statistical operations without using numpy operation'''

def mean_calculate(list):
    '''mean calculate  
        input parameters are list. Ex- list = [10,20,30,40,50]
        output as mean which is in float format
    '''    
    sum = 0
    sum_val = [ sum :=sum+ i for i in list][-1]
    return sum_val / len(list) 

def mode_calculate(list):
    ''' Mode calculate 
         input parameters are list. Ex- list = [10,20,20,30,20,30,40,50]
        output as mode values which are repeated max values'''
    dummy_list = sorted(list)
    count_val = {}
    for val in dummy_list:
        if val in count_val:
            count_val[val] +=1 
        else:
            count_val[val] = 1
    max_val = max(count_val.values())
    verify_max_keys = [key for key, val in count_val.items() if val == max_val]
    if len(verify_max_keys) == 1:
        return verify_max_keys[0]
    return verify_max_keys 
            
    
def median_calculate(list):
    '''Median calculate
        input parameters are list. Ex- list = [10,20,30,40,50]
        output as median value (30)
    '''
    dummy_list = sorted(list)
    n = len(dummy_list)
    if n % 2 == 0 :
        return ( dummy_list[n //2 - 1] + dummy_list [n // 2] ) /2 
    else:
        return dummy_list [n // 2] 



'''
def variance_calculate():
def absoulte_mean_calculate():
def standard_deviation_calculate():
def emperial_rule_caluclate():
def covariance_calculate():
def coreleation_calculate():'''
