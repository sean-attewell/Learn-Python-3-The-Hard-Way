try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Sean Attewell',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'sean.attewell@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['learning'],
    'scripts': [],
    'name': 'learning'
}

setup(**config)