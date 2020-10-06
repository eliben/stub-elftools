import setuptools

FULL_DESCRIPTION = r'''\
This is not an actual project; you're probably looking for `pyelftools`
instead. To install `pyelftools` run:

    pip install pyelftools
'''

setuptools.setup(
    name="elftools",
    version="0.0.1",
    author="Eli Bendersky",
    author_email="eliben@gmail.com",
    description="Placeholder for pyelftools",
    long_description=FULL_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/eliben/pyelftools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
