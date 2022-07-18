"""Setup script for object_detection with TF2.0."""
import os
from setuptools import find_packages
from setuptools import setup

# Note: adding apache-beam to required packages causes conflict with
# tf-models-offical requirements. These packages request for incompatible
# oauth2client package.
REQUIRED_PACKAGES = [
    # Required for apache-beam with PY3
    'avro-python3==1.10.1',
    'apache-beam',
    'pillow',
    'lxml',
    'matplotlib',
    'Cython',
    'contextlib2',
    'tf-slim==1.1.0',
    'six',
    'pycocotools',
    'lvis==0.5.3',
    'scipy',
    'pandas',
    'tf-models-official==2.5.1',
    'tensorflow_io',
    # Workaround due to
    # https://github.com/keras-team/keras/issues/15583
    # 'keras',
    'opencv-python-headless==4.5.1.48',
    'tensorflow==2.8.0',
]

setup(
    name='object_detection',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=(
        [p for p in find_packages() if p.startswith('object_detection')] +
        find_packages(where=os.path.join('.', 'slim'))),
    package_dir={
        'datasets': os.path.join('slim', 'datasets'),
        'nets': os.path.join('slim', 'nets'),
        'preprocessing': os.path.join('slim', 'preprocessing'),
        'deployment': os.path.join('slim', 'deployment'),
        'scripts': os.path.join('slim', 'scripts'),
    },
    description='Tensorflow Object Detection Library',
    python_requires='>3.6',
)
