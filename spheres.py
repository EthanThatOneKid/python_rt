from sphere import Sphere

def getSpherePosition(x):
    return -1 * x**2 + 1.6

def generateSpheres(n, minX, maxX):
    spheres = []
    for i in range(n):
        x = (maxX - minX) * i / n + minX
        y = getSpherePosition(x)
        z = x - 2
        spheres.append(Sphere(center=(x, y, z), radius=0.1, diffuse=(0, 0.7, 0)))
    return spheres

class Spheres:
    objects = [
        # Floor!
        Sphere(center=(9, -9000, 0), radius = 9000 - 0.7, ambient=(0.1, 0.1, 0.1))
    ]
    objects += generateSpheres(100, -2, 2)

    @staticmethod
    def get_spheres():
        return Spheres.objects

