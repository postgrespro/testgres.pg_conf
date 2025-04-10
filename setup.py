#import sys

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
    packages=[
        'testgres.postgres_configuration',
        'testgres.postgres_configuration.core',
        'testgres.postgres_configuration.core.option',
        'testgres.postgres_configuration.core.option.handlers',
        'testgres.postgres_configuration.core.option.handlers.add',
        'testgres.postgres_configuration.core.option.handlers.get_value',
        'testgres.postgres_configuration.core.option.handlers.prepare_get_value',
        'testgres.postgres_configuration.core.option.handlers.prepare_set_value',
        'testgres.postgres_configuration.core.option.handlers.prepare_set_value_item',
        'testgres.postgres_configuration.core.option.handlers.set_value',
        'testgres.postgres_configuration.core.option.handlers.set_value_item',
        'testgres.postgres_configuration.core.option.handlers.write',
    ],
    package_dir={'testgres.postgres_configuration': 'src'},
    description='PostgreSQL Configuration Python Library',
    url='https://git.postgrespro.ru/d.kovalenko/testgres.postgres_configuration',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='PostgreSQL',
    author='Postgres Professional',
    author_email='d.kovalenko@postgrespro.ru',
    keywords=['postgresql', 'postgres', 'test'],
    install_requires=install_requires,
    classifiers=[],
)
