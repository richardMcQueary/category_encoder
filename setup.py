from setuptools import setup, find_packages
from codecs import open
from os import path
from category_encoder import __version__


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='category_encoder',
    version=__version__,
    description='A collection sklearn transformers to encode categorical variables as numeric',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='python data science machine learning pandas sklearn',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    author='Will McGinnis',
    install_requires=[
      'numpy>=1.14.0',
      'scikit-learn>=0.20.0',
      'scipy>=1.0.0',
      'statsmodels>=0.9.0',
      'pandas>=0.21.1',
      'patsy>=0.5.1',
    ],
    author_email='will@pedalwrencher.com'
)
