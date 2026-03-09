# Curso de Python. Paquetes distribuibles. Vídeo 36
# Practica 035 paquetes distrubuibles

from setuptools import setup # importamos setup de setuptools

setup( # el comando setup espera que se le añada una dirección 
    name="Paquete Distribuible de Calculos",
    version="1.0",
    description="Paquete de operaciones de redondeo y potencia",
    author="Shintesu",
    author_email="leisberth.an24@gmail.com",
    url="www.miDirecciónPrivada.com",
    packages=["PaqueteCalculos","PaqueteCalculos.Modulo_RedondeoPotencia"] # packages indexa la dirección del paquete

)



















#USANDO EL SÍMBOLO DEL SISTEMA O POWERSHELL INGRESAMOS A NUESTRA CARPETA y creamos un paquete distribuible

#C:\Users\Shintesu>..

#C:\Users\Shintesu>cd Desktop

#C:\Users\Shintesu\Desktop>cd Python Prácticas

#C:\Users\Shintesu\Desktop\Python prácticas>

#C:\Users\Shintesu\Desktop\Python prácticas>python setup.py sdist

#running sdist
#running egg_info
#writing Paquete_Distribuible_de_Calculos.egg-info\PKG-INFO
#writing dependency_links to Paquete_Distribuible_de_Calculos.egg-info\dependency_links.txt
#writing top-level names to Paquete_Distribuible_de_Calculos.egg-info\top_level.txt
#reading manifest file 'Paquete_Distribuible_de_Calculos.egg-info\SOURCES.txt'
#writing manifest file 'Paquete_Distribuible_de_Calculos.egg-info\SOURCES.txt'
#warning: sdist: standard file not found: should have one of README, README.rst, README.txt, README.md

#running check
#creating paquete distribuible de calculos-1.0
#creating paquete distribuible de calculos-1.0\PaqueteCalculos
#creating paquete distribuible de calculos-1.0\PaqueteCalculos\Modulo_RedondeoPotencia
#creating paquete distribuible de calculos-1.0\Paquete_Distribuible_de_Calculos.egg-info
#copying files to paquete distribuible de calculos-1.0...
#copying setup.py -> paquete distribuible de calculos-1.0
#copying PaqueteCalculos\__init__.py -> paquete distribuible de calculos-1.0\PaqueteCalculos
#copying PaqueteCalculos\modulo_CalculosGenerales.py -> paquete distribuible de calculos-1.0\PaqueteCalculos
#copying PaqueteCalculos\Modulo_RedondeoPotencia\RedondeoPotencia.py -> paquete distribuible de calculos-1.0\PaqueteCalculos\Modulo_RedondeoPotencia
#copying PaqueteCalculos\Modulo_RedondeoPotencia\__init__.py -> paquete distribuible de calculos-1.0\PaqueteCalculos\Modulo_RedondeoPotencia
#copying Paquete_Distribuible_de_Calculos.egg-info\PKG-INFO -> paquete distribuible de calculos-1.0\Paquete_Distribuible_de_Calculos.egg-info
#copying Paquete_Distribuible_de_Calculos.egg-info\SOURCES.txt -> paquete distribuible de calculos-1.0\Paquete_Distribuible_de_Calculos.egg-info
#copying Paquete_Distribuible_de_Calculos.egg-info\dependency_links.txt -> paquete distribuible de calculos-1.0\Paquete_Distribuible_de_Calculos.egg-info
#copying Paquete_Distribuible_de_Calculos.egg-info\top_level.txt -> paquete distribuible de calculos-1.0\Paquete_Distribuible_de_Calculos.egg-info
#copying Paquete_Distribuible_de_Calculos.egg-info\SOURCES.txt -> paquete distribuible de calculos-1.0\Paquete_Distribuible_de_Calculos.egg-info
#Writing paquete distribuible de calculos-1.0\setup.cfg
#creating dist
#Creating tar archive
#removing 'paquete distribuible de calculos-1.0' (and everything under it)
