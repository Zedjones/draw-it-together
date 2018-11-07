from setuptools import setup 

setup(name='draw_it_together',
      version='1.0',
      description='Runs the web server for the draw it together application',
      url='https://github.com/Zedjones/draw-it-together',
      author='Nicholas Jones, Ellie Parobek',
      install_requires=[
          'psycopg2-binary', 'flask'
      ],
      zip_safe=False)