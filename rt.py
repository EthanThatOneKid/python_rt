import numpy as np
import matplotlib.pyplot as plt
import sys
from sphere import Sphere 
from light import Light 
from spheres import Spheres


def normalize(vector): return vector / np.linalg.norm(vector)


def reflected(vector, axis): return vector - 2 * np.dot(vector, axis) * axis


def sphere_intersect(center, radius, ray_origin, ray_direction):
    b = 2 * np.dot(ray_direction, ray_origin - center)
    c = np.linalg.norm(ray_origin - center) ** 2 - radius ** 2
    delta = b ** 2 - 4 * c
    if delta > 0:
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
    return None


def nearest_intersected_object(objects, ray_origin, ray_direction):     # next line is a list comprehension -- LEARN THIS
    distances = [sphere_intersect(obj.center, obj.radius, ray_origin, ray_direction) for obj in objects]
    nearest_object = None
    min_distance = np.inf
    for index, distance in enumerate(distances):
        if distance and distance < min_distance:
            min_distance = distance
            nearest_object = objects[index]
    return nearest_object, min_distance      # returns a tuple


def show_plot_image(image, width, height):
  plt.imshow(image, extent=[0, width, 0, height])
  plt.title(file, fontweight="bold")
  plt.axis('off')
  plt.tight_layout()
  plt.show()


def ray_trace(file, width=300, height=200):
  max_depth = 3

  camera = np.array([0, 0, 1])
  ratio = float(width) / height
  screen = (-1, 1 / ratio, 1, -1 / ratio) # left, top, right, bottom

  light = Light(position=(5, 5, 5))

  objects = Spheres.get_spheres()       # student supplies file spheres.py

  image = np.zeros((height, width, 3))
  print(f'creating file: {file} with {height} lines... ', end=' ', flush=True)

  for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
      for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
          # screen is on origin
          pixel = np.array([x, y, 0])
          origin = camera
          direction = normalize(pixel - origin)

          color = np.zeros((3))
          reflection = 1

          for _ in range(max_depth):      # not accessing loop variable, use _ to indicate this
              # check for intersections
              nearest_object, min_distance = nearest_intersected_object(objects, origin, direction)
              
              if nearest_object is None:  
                  break

              intersection = origin + min_distance * direction
              normal_to_surface = normalize(intersection - nearest_object.center)
              shifted_point = intersection + 1e-5 * normal_to_surface
              intersection_to_light = normalize(light.position - shifted_point)

              _, min_distance = nearest_intersected_object(objects, shifted_point, intersection_to_light)
              intersection_to_light_distance = np.linalg.norm(light.position - intersection)
              is_shadowed = min_distance < intersection_to_light_distance

              if is_shadowed:
                  break

              illumination = np.zeros((3))

              # ambient       nearest_object.ambient    * light.ambient
              illumination += nearest_object.ambient * light.ambient
              
              #diffuse
              illumination += nearest_object.diffuse * light.diffuse * np.dot(intersection_to_light, normal_to_surface)

              # specular
              intersection_to_camera = normalize(camera - intersection)
              H = normalize(intersection_to_light + intersection_to_camera)
              illumination += nearest_object.specular * light.specular * np.dot(normal_to_surface, H) ** (nearest_object.shininess / 4)

              # reflection
              color += reflection * illumination
              reflection *= nearest_object.reflection

              origin = shifted_point
              direction = reflected(direction, normal_to_surface)

          image[i, j] = np.clip(color, 0, 1)
      if (i + 1) % (height / 10) == 0:
        print(i + 1, end=' ', flush=True)

  show_plot_image(image=image, width=width, height=height)
  plt.imsave(file, image)


def process_cmd_line_args():
    file = sys.argv[1] if len(sys.argv) == 2 else ""     # argv[0] is the name of the program, argv[1] is the name of our imagefile 
    if (len(file) == 0):
        file = 'image.png'
    elif len(file) > 0 and file.find(".") == -1:
        file += ".png"
    return file


def main(file):
    print(f'filename is {file}')
    ray_trace(file=file, height=200)


if __name__ == '__main__':
    # main()

    file = process_cmd_line_args()
    main(file)
