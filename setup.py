from setuptools import setup, find_packages

setup(
    name="YouTubeMusicAPI",
    version="2.7.1",
    description="The search API for YouTube Music.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cj-praveen/YouTube-Music-API",
    keywords = "youtube music api, YouTubeMusicAPI, python youtube music api, youtube music api python, youtube api pypi, youtube api",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    license="MIT"
)