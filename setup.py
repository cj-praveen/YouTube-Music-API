import setuptools

setuptools.setup(
    name="YouTubeMusicAPI",
    version="2.9",
    description="An unofficial search API for YouTube Music.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cj-praveen/YouTube-Music-API/",
    keywords="youtube music api, YouTubeMusicAPI, python youtube music api, youtube music api python",
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "httpx"
    ]
)
