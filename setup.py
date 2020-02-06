import setuptools

setuptools.setup(
    name='flake8-django-docstrings',
    version='0.0.1',
    description='our extension to flake8',
    long_description='long_description',
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
    ],
    tests_require=[
        'pytest',
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
