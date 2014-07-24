from distutils.core import setup

from gretafun.version import __version__

setup(
    name='gretafun',
    version=__version__,
    author='Matthew Dahmer',
    author_email='matthew.dahmer@gmail.com',
    packages=['gretafun'],
    url='http://cxc.cfa.harvard.edu/mta/ASPECT/tool_doc/gretafun/',
    license='BSD',
    description='Tools for working with Chandra GRETA utilities',
    long_description=open('README').read(),
)