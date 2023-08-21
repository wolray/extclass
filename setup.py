import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='extclass',
    version='1.0.0',
    author='wolray',
    author_email='wolray@foxmail.com',
    description='A Python approach for class extensions like C# and Kotlin',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wolray/extclass',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
