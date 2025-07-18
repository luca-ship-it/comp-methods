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
        "numpy>=1.21.0,<1.22.2",    # passt noch zu pymc3 (<1.22.2)
        "pandas>=1.4.0,<2.0.0",     # pandas v1.x ist mit numpy 1.21–1.22 kompatibel
        "numba>=0.55.0,<0.58.0",    # wähle hier eine Version, die ohne numpy‑1.24 auskommt
    ],
    python_requires=">=3.8",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)

