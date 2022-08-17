from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# Get requirements
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

extras_require = {
    'voice': ['PyNaCl>=1.3.0,<1.6'],
    'docs': [
        'sphinx==4.4.0',
        'sphinxcontrib_trio==1.1.2',
        'sphinxcontrib-websupport',
        'typing-extensions',
    ],
    'speed': [
        'orjson>=3.5.4',
        'aiodns>=1.1',
        'Brotli',
        'cchardet',
    ],
    'test': [
        'coverage[toml]',
        'pytest',
        'pytest-asyncio',
        'pytest-cov',
        'pytest-mock'
    ]
}

setup(
    name="pydis_discord",
    version="1.0.1",
    description="An Discord API v10 wrapper for Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RinkaGI/Pydis",
    author="RinkaDev",
    author_email="rinkadevoficial@gmail.com",
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],

    keywords="sample, setuptools, development, discord, bot, wrapper, api, modern, easy, fast",  # Optional
    packages = [
    'pydis',
    'pydis.types',
    'pydis.ui',
    'pydis.webhook',
    'pydis.app_commands',
    'pydis.easy.commands',
    'pydis.easy.tasks',
    ],
    python_requires=">=3.8, <4",
    install_requires=[requirements],
    extras_require=extras_require,
    include_package_data=True,
    project_urls={  # Optional
        "Bug Reports": "https://github.com/RinkaGI/Pydis/issues",
        "Source": "https://github.com/RinkaGI/Pydis/",
    },
)