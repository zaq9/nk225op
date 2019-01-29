from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

setup(
    name='nk225op',
    version='0.1.0',
    description='Download latest Option Price(nk255) from JPX',
    url='https://github.com/zaq9/nk225op',
    author='zaq',
    author_email='zaq_9@yahoo.co.jp',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    keywords=['options', 'python', 'finance'],
    py_modules=['nk225op'],
    install_requires=['pandas', 'bs4'],
)
