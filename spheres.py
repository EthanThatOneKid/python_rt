from sphere import Sphere

class Spheres:
    objects = [
        Sphere(center=(-0.2, 0, -1), radius=0.7, diffuse=(0.7, 0, 0)),

        Sphere(center=(1.2, 0, -1), radius=0.7, diffuse=(0, 0, 0.7)),
        Sphere(center=( -1.6, 0, -1), radius=0.7, diffuse=(0.7, 0.7, 0)),

        Sphere(center=(9, -9000, 0), radius = 9000 - 0.7, ambient=(0.1, 0.1, 0.1))
    ]

    @staticmethod
    def get_spheres():
        return Spheres.objects

