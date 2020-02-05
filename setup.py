import setuptools

requires = [
    "flake8 > 3.0.0",
]

setuptools.setup(
    name="flake8_example",
    license="MIT",
    version="0.1.0",
    description="our extension to flake8",
    author="Me",
    author_email="example@example.com",
    url="https://gitlab.com/me/flake8_example",
    packages=[
        "flake8_plugin",
    ],
    install_requires=requires,
    entry_points={
        'flake8.extension': [
            'DMD = flake8_plugin:DjangoModelDocString',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
