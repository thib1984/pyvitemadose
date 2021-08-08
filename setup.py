from setuptools import setup


setup(
    name="pyvitemadose",
    version="0.2.1",
    description="pyvitemadose displays available chronodoses of covid vaccine for your departement in France",
    long_description="The complete description/installation/use/FAQ is available at : https://github.com/thib1984/pyvitemadose#readme",
    url="https://github.com/thib1984/pyvitemadose",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="MIT",
    packages=["pyvitemadose"],
    install_requires=[],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "pyvitemadose=pyvitemadose.__init__:pyvitemadose"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
