from setuptools import setup, find_packages


def read_requirements(file_name: str) -> list:
    with open(file_name, "r") as f:
        requires = [
            requirement.strip()
            for requirement in f.readlines()
            if (requirement.strip() and requirement.strip()[:1] != "#")
        ]
    return requires


requires = read_requirements('requirements.txt')
dev_requires = read_requirements('requirements-dev.txt')

setup(
    name='model monitoring',
    version='0.1.0',
    author="Ha Quan Nguyen",
    author_email="quan.ngha95@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"": "src"},
    packages=find_packages(where='src', exclude=['tests']),
    # requirements.txt
    install_requires=requires,
    # install including interactive option
    # pip install -e ".[interactive, dev]"
    extras_require={
        'interactive': ['plotly==5.5.0'],
        'dev': dev_requires,
    },
)
