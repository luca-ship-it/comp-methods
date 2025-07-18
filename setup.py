from setuptools import setup, find_packages

setup(
    name="comp-methods",
    version="0.1.0",
    description="Numerical methods",
    author="Luca Soszynski",
    author_email="luca@example.com",
    url="https://github.com/luca-ship-it/comp-methods",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=1.5.0",
        "numba>=0.57.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)

