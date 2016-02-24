import skd_forms
from setuptools import setup, find_packages

setup(
    name='django-skd-forms',
    version=skd_forms.__version__,
    packages=find_packages(exclude=['skd_forms_tests', 'example_project']),
    description='Django forms alternative',
    long_description=open('README.md').read(),
    author='SteelKiwi Development',
    author_email='sales@steelkiwi.com',
    license='MIT',
    url='https://github.com/steelkiwi/django-skd-forms',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent'])
