import numpy as np 


class Light:
  def __init__(self, position=(0.0, 0.0, 0.0), ambient=(1, 1, 1), diffuse=(1, 1, 1), specular=(1, 1, 1)):
      self.position = np.array(list(position))
      self.ambient = np.array(list(ambient))
      self.diffuse = np.array(list(diffuse))
      self.specular = np.array(list(specular))

  def __str__(self): pass 

  @staticmethod
  def run_tests(): pass 
