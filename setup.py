# It specifies metadata like the project’s name, version, dependencies, and entry 
# points. You use setup.py when you want to make your project installable via 
# pip, share it on PyPI, or manage dependencies formally for deployment.

from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    description="its a wine Q package", 
    author="CHARAN", 
    packages=find_packages(),
    license="MIT"
)