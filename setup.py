from setuptools import setup, find_packages

setup(
    name='particle_systemszcz',
    version='1.0.4',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pygame-ce',
    ],
    author='rutra',
    author_email='ruterszcz@gmail.com',
    description='A particle system library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rutra8002/particle_system',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)