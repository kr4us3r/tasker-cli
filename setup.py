from setuptools import setup, find_packages

setup(
    name="tasker-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts":[
            "tasker-cli = tasker_cli.cli:main"
        ]
    },
    author="kr4us3r",
    author_email="bakemonowa@gmail.com",
    description="A tool for task management.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kr4us3r/tasker-cli",
    license="MIT",
)