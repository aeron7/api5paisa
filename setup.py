import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="api5paisa", # Replace with your own username
    version="0.0.6",
    author="Amit Ghosh",
    description="5 paisa browser based api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aeron7/api5paisa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)