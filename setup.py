"""
WTAlchemy
-----------

WTForms SQAlchemy extension.

"""
from setuptools import setup, find_packages


setup(
    name='WTAlchemy',
    version='0.1b3',
    url='https://github.com/jean-philippe/WTAlchemy',
    license='mit',
    author='Jean-Philippe Serafin',
    author_email='serafinjp@gmail.com',
    description='WTForms SQAlchemy extension',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'WTForms==0.6.3',
        'SQLALchemy'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
