from setuptools import setup

setup(name='scrobbless',
      version='0.3.0',
      description='Minimal last.fm scrobbler',
      url='http://github.com/sebojanko/scrobbless',
      author='Sebastian Janko',
      author_email='janko.sebastian@gmail.com',
      license='GNU GPL v3',
      keywords='last.fm scrobbler',
      packages=['scrobbless'],
      zip_safe=False,
      install_requires=['requests'])
