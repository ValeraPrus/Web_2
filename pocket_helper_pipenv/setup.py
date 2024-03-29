from setuptools import setup

setup(
    name='pocket_helper',
    version='1.0.0',
    description='adressbook',
    url='https://github.com/Vladosinfo/knowledge_base',
    author='Pasko Vladyslav, Prus Valerii, Tsybrovskyi Oleksii, Palamar Anna',
    author_email='vladyslav.pasko@gmail.com, prusvalerii@gmail.com, tsybrovsky@gmail.com, anna.palamar1210@gmail.com',
    license='BSD',
    install_requires=[],
    package_dir={'': 'src'},
    entry_points={'console_scripts': ['pocket_helper = main:main']}
)
