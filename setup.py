from pathlib import Path

from setuptools import find_packages, setup

REPO_ROOT_DIR_PATH = Path(__file__).parent

README = (REPO_ROOT_DIR_PATH / "README.md").read_text()

setup(
    name="airflow-e2e",
    version="0.2.0",
    description="Create E2E test scripts for Airflow DAGs testing",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jw-ng/airflow-e2e",
    author="Jun Wei, Ng",
    author_email="ngjunwei.15@gmail.com",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "airflow-e2e=airflow_e2e.__main__:main",
        ]
    },
)
