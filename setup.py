from setuptools import setup, find_packages

setup(
    name='particle_system',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pygame-ce',
    ],
    author='rutra',
    author_email='no',
    description='A particle system library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/particle_system',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)