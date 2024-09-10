from setuptools import setup

setup(
    name="markdown-smartbreaks",
    version="1.0.0",
    author="zetaloop",
    author_email="zetaloop@outlook.com",
    description="",
    keywords="markdown nl2br breaks",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zetaloop/markdown_smartbreaks",
    license="MIT",
    packages=["smartbreaks"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Markup :: HTML",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["Markdown>=3.0.1"],
    python_requires=">=3.8",
)
