import numpy as np

def calculate(list):
  
  #test if the list is shorter than 9 flag error
  if len(list) < 9: 
    raise ValueError("List must contain nine numbers.")

  #create the numpy array and the 2d numpy array from list
  np_array_flattened=np.array(list)
  np_array=np.array([list[:3],list[3:6],list[6 :]])
  

  #make the calculation dict
  calculations={
  'mean': [np.mean(np_array, axis=0).tolist(),
           np.mean(np_array, axis=1).tolist(),     
           np.mean(np_array_flattened)],
  'variance': [np.var(np_array, axis=0).tolist(),
               np.var(np_array, axis=1).tolist(),     
           np.var(np_array_flattened)],
  'standard deviation': [np.std(np_array, axis=0).tolist(),
                         np.std(np_array, axis=1).tolist(),
                         np.std(np_array_flattened)],
  'max': [np.max(np_array, axis=0).tolist(),
          np.max(np_array, axis=1).tolist(),     
          np.max(np_array_flattened)],
  'min': [np.min(np_array, axis=0).tolist(),
          np.min(np_array, axis=1).tolist(),     
          np.min(np_array_flattened)],
  'sum': [np.sum(np_array, axis=0).tolist(),
          np.sum(np_array, axis=1).tolist(),     
          np.sum(np_array_flattened)],
  }


  return calculations