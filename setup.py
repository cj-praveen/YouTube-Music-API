import setuptools

setuptools.setup(
    name="YouTubeMusicAPI",
    version="2.8",
    description="The YouTube Music search scraper for the Python programming language.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cj-praveen/YouTube-Music-API/",
    keywords="youtube music api, YouTubeMusicAPI, python youtube music api, youtube music api python, youtube api "
               "pypi, youtube api, youtube music search api, youtube music search, praveen cj",
    package_dir={"": "src"},
    python_requires=">=3.9"
)
