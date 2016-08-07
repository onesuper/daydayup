from setuptools import setup, find_packages
from daydayup import __version__


requirements = []
with open('requirements.txt') as f:
    requirements.extend(f.read().splitlines())


setup(
    name = 'daydayup',
    version = str(__version__),
    author = 'onesuper',
    author_email = 'onesuperclark@gmail.com',
    url = 'https://github.com/onesuper/daydayup',
    description = 'Daily report authoring tool for baixingers',
    long_description = __doc__,
    packages = find_packages(),
    include_package_data = True,
    license = 'MIT',
    entry_points = {
        'console_scripts': 'daydayup = daydayup.cli:CLI'
    },
    install_requires = requirements,
    platforms = 'any',
    zip_safe = False,
)
