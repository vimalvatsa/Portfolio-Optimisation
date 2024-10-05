from setuptools import setup, find_packages

with open(file="README.md", mode="r") as fh:
    long_description = fh.read()

setup(
    name='Portfolio_Optimization',
    author='Vimal Vatsa',
    author_email='vatsavimal095@gmail.com',
    version='0.0.1',
    description='Portfolio optimization in Python, covering all the major techniques from basics to advanced.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    install_requires=[
        'requests==2.24.0',
        'matplotlib==3.3.0',
        'numpy==1.22.0',
        'pandas==1.0.5',
        'scipy==1.5.2',
        'fake_useragent==0.1.11',
        'python_dateutil==2.8.1',
        'scikit_learn==0.23.2'
    ],
    packages=find_packages(
        include=['pyopt']
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>3.7'
)
