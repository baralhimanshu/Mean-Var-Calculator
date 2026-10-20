import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    else:
        ar = np.array(input_list).reshape(3,3)
    
    column_mean, row_mean, total_mean = np.mean(ar,axis = 0).tolist(), np.mean(ar,axis = 1).tolist(), np.mean(ar)
    column_sd , row_sd , total_sd = np.std(ar, axis = 0).tolist(), np.std(ar, axis =1).tolist(), np.std(ar)
    column_var, row_var, total_var = np.var(ar, axis =0).tolist(), np.var(ar, axis =1).tolist(), np.var(ar)
    column_max, row_max, total_max = np.max(ar, axis = 0).tolist(), np.max(ar, axis =1).tolist(), np.max(ar)
    column_min, row_min, total_min = np.min (ar, axis =0).tolist(), np.min(ar, axis = 1).tolist(), np.min(ar)
    column_sum, row_sum, total_sum = np.sum(ar, axis =0).tolist(), np.sum (ar,axis = 1 ).tolist(), np.sum(ar)
  
    calculations = {
        "mean" : [column_mean, row_mean, total_mean],
        "variance" : [column_var, row_var, total_var],
        "standard deviation" : [column_sd, row_sd, total_sd],
        "max" : [column_max, row_max, total_max],
        "min" : [column_min, row_min, total_min],
        "sum" : [column_sum, row_sum, total_sum]
    }
    return calculations
