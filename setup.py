from setuptools import setup, find_packages

setup(
    name="binloader",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "binloader": ["binaries/*"],
    },
)
