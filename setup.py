import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hype-html",
    version="2.0.0",
    author="Scott Russell",
    author_email="me@scottrussell.net",
    description="A minimal python dsl for generating html.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scrussell24/hype-html",
    packages=setuptools.find_packages(),
    package_data={"hype": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
