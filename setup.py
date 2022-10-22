import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="YouTubeMusicAPI",
    version="2.7",
    author="CJ Praveen",
    author_email="cjpraveen@hotmail.com",
    description="The search API for YouTube Music.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cj-praveen/YouTube-Music-API",
    keywords = "youtube music api, YouTubeMusicAPI, python youtube music api, youtube music api python, youtube api pypi, youtube api",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
