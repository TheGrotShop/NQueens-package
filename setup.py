# setup.py

"""Setup script."""

from setuptools import setup

with open('requirements.txt', 'r', encoding='UTF-8') as f:
    required: list[str] = f.read().splitlines()

with open("README.md", 'r', encoding='UTF-8') as f:
    long_description: str = f.read()

setup(
    name='wolfsoftware.NQueens',
    version='0.1.1',
    packages=['wolfsoftware.nqueens'],
    entry_points={
        'console_scripts': [
            'nqueens=wolfsoftware.nqueens.main:main',
        ],
    },
    author='Wolf Software',
    author_email='pypi@wolfsoftware.com',
    description='A simple solution for the N Queens problem.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/TheGrotShop/NQueens-package',
    project_urls={
        ' Source': 'https://github.com/TheGrotShop/NQueens-package',
        ' Tracker': 'https://github.com/TheGrotShop/NQueens-package/issues/',
        ' Documentation': 'https://github.com/TheGrotShop/NQueens-package',
        ' Sponsor': 'https://github.com/sponsors/WolfSoftware',
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
    python_requires='>=3.9',
    install_requires=required,
)
