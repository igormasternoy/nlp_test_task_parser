from distutils.core import setup

setup(
    # Application name:
    name="tree_parser",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Igor Masternyi",
    author_email="igormasternoy@gmail.com",

    # Packages
    packages=["parser"],

    # Include additional files into the package
    include_package_data=True,

    #
    # license="LICENSE.txt",
    description="Pretty printing of string formatted left oriented trees",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[   ],
)