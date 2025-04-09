import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Basic dependencies
install_requires = [
]

# Get contents of README file
with open('README.md', 'r') as f:
    readme = f.read()

setup(
    version='1.0.0',
    name='testgres.postgres_configuration',
    packages=['testgres.postgres_configuration'],
    package_dir={'testgres.postgres_configuration': 'src'},
    description='PostgreSQL Configuration Python Library',
    #url='https://github.com/postgrespro/testgres',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='PostgreSQL',
    author='Postgres Professional',
    author_email='testgres@postgrespro.ru',
    keywords=['postgresql', 'postgres', 'test'],
    install_requires=install_requires,
    classifiers=[],
)
