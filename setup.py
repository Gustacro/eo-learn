import os
from setuptools import setup


def get_long_description():
    this_directory = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

    return long_description

def parse_requirements(file):
    return sorted(set(
        line.partition('#')[0].strip()
        for line in open(os.path.join(os.path.dirname(__file__), file))
    ) - set(''))


setup(name='eo-learn',
      version='0.2.0',
      description='Earth observation processing framework for machine learning in Python',
      long_description=get_long_description(),
      long_description_content_type='text/markdown',
      url='https://github.com/sentinel-hub/eo-learn',
      author='Sinergise EO research team',
      author_email='info@sinergise.com',
      license='MIT',
      packages=[],
      install_requires=parse_requirements("requirements.txt"),
      zip_safe=False)
