from setuptools import setup

setup(
    name="gute",
    version="0.1.0",
    packages=["gute"],
    entry_points={"console_scripts": ["gute = gute.__main__:main"]},
)
