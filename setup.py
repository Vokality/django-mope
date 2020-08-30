import os
import re
import sys

from setuptools import find_packages, setup

from django_mope import __author__, __email__, __version__


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('django_mope')

if sys.argv[-1] == 'tag':
    print("Tagging the version now:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git tag --tags")
    sys.exit()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='django-mope',
      version=__version__,
      description='A Django app to simplify Mopé integrations',
      long_description=long_description,
      long_description_content_type='text/markdown; charset=UTF-8',
      author=__author__,
      author_email=__email__,
      packages=find_packages(exclude=["tests"]),
      url='https://github.com/Vokality/django-mope',
      include_package_data=True,
      zip_safe=False,
      license='MIT',
      python_requires='>=3.6,<=3.8',
      install_requires=[
          'django>=2.2',
          'python-mope>=0.0.4',
      ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Operating System :: OS Independent",
      ])
