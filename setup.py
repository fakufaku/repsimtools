import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="repsimtools",  # Replace with your own username
    version="0.0.1",
    author="Robin Scheibler",
    author_email="fakufaku@gmail.com",
    description="Tools for parallel simulation with git source control.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fakufaku/repsimtools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["ipyparallel", "gitpython"],
)
