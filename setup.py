import setuptools

with open("README.md",'r',encoding='utf-8') as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="end-to-end-ML-Project-with-MLFlow"
AUTHOR_USER_NAME="ajairosen11"
SRC_REPO="mlProject" #Source (SRC) repository name
AUTHOR_EMAIL='vishalajairosen@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),

)