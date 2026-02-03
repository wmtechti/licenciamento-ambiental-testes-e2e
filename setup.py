"""
Setup para instalação do pacote de testes E2E
==============================================
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="licenciamento-testes-e2e",
    version="1.0.0",
    description="Testes E2E para Sistema de Licenciamento Ambiental",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Miltec TI",
    author_email="contato@miltec.com.br",
    url="https://github.com/wmiltecti/licenciamento-ambiental-testes-e2e",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "selenium>=4.15.2",
        "pytest>=7.4.3",
        "pytest-html>=4.1.1",
        "webdriver-manager>=4.0.1",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "Pillow>=10.1.0",
    ],
    extras_require={
        "dev": [
            "pytest-xdist>=3.5.0",
            "pytest-timeout>=2.2.0",
            "allure-pytest>=2.13.2",
            "black>=23.12.1",
            "flake8>=7.0.0",
            "mypy>=1.8.0",
        ],
        "db": [
            "supabase>=2.0.3",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.11",
)
