.. gretafun documentation master file, created by
   sphinx-quickstart on Thu Jul 24 21:28:26 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

====================================
Documentation for gretafun utilities
====================================

This module facilitates interaction between aspects of GRETA telemetry tools and the Ska 
environment. Currently the only functions included are those that parse certain GRETA files, 
however greater functionality may be added in the future.

Contents:

.. toctree::
   :maxdepth: 2


GRETA Parsing Functions
=======================

**Parse G_LIMMON Specification**

    readGLIMMON(filename='/home/greta/AXAFSHARE/dec/G_LIMMON.dec')


**Parse G_LIMMON Comment Section**

    parse_comments(filename='/home/greta/AXAFSHARE/dec/G_LIMMON.dec', startline=603):


**Parse G_LIMMON Output File**

    process_limits_file(filename='limfile.txt'):


**Parse GRETA Plot Specification**

    parsedecplot(decfile):


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

