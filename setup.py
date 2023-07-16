import setuptools

with open('README.md','r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_Name = "NLP-Text-Summarizer-"
AUTHOR_USER_NAME = "MelissaDong"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "jie.dong@sjsu.edu"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package for NLP app",
    long_description=long_description,
    long_description_content="",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_Name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_Name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)