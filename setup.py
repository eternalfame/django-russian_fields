import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-closable_admin_filter',
    version='0.1.0',
    packages=['closable_admin_filter'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to add hide/show ability to the filter in Django admin.',
    long_description=README,
    url='https://github.com/eternalfame/django-closable_admin_filter',
    author='Vyacheslav Sukhenko',
    author_email='eternalfame@mail.ru',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)