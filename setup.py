import os
from setuptools import find_packages

__location__ = os.path.dirname(__file__)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def __path(filename):
    return os.path.join(os.path.dirname(__file__),
                        filename)

build = 0
if os.path.exists(__path('build.info')):
    build = open(__path('build.info')).read().strip()

#revision number will always be the build number from jenkins, for simplicity; force change major and minors where appropriate
version= '0.0.{build}'.format(build = (int(build)))

setup(
    name='aztek',
    version = version, 
    description='api tools',
    packages = find_packages(),
    install_requires=[
        "azure-storage-blob",
    ],
    include_package_data = True,
)
