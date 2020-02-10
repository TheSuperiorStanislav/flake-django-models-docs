import setuptools

with open('README.md', 'r') as read_me_file:
    long_description = read_me_file.read()

setuptools.setup(
    name='flake8-django-docstrings',
    version='0.0.1',
    description='Flake 8 plugin that checks docstrings for Django models',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Saritasa',
    author_email='example@example.com',
    url='url',
    packages=[
        'flake8_plugin',
    ],
    python_requires='>=3.5',
    install_requires=[
        'flake8',
        'packaging'
    ],
    tests_require=[
        'pytest',
        'pytest-flake8',
        'pytest-isort',
    ],
    entry_points={
        'flake8.extension': [
            'DMD = flake8_plugin:DjangoModelDocString',
        ],
    },
    classifiers=[
        'Framework :: Flake8',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
    keywords=[
        'development code_style docstrings'
    ]
)
