import numpy as np


class Sphere:
  def __init__(self, center=(0.0, 0.0, 0.0), radius=1.0, ambient=(0.1, 0, 0), diffuse=(1, 1, 1), specular=(1, 1, 1), shininess=100, reflection=0.5):
      self.center = np.array(list(center))
      self.radius = radius 
      self.ambient = np.array(list(ambient))
      self.diffuse = np.array(list(diffuse))
      self.specular = np.array(list(specular))
      self.shininess = shininess
      self.reflection = reflection

  def __str__(self): pass 

  @staticmethod
  def run_tests(): pass 
