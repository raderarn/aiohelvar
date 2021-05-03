import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aiohelvar",
    version="0.0.1",
    author="Tom Playford",
    description="Async HelvarNet comms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomplayford/aiohelvar",
    project_urls={
        "Bug Tracker": "https://github.com/tomplayford/aiohelvar/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

    packages=["aiohelvar"],
    python_requires=">=3.7",
)