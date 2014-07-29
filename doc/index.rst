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

.. py:function:: read_glimmon([filename='/home/greta/AXAFSHARE/dec/G_LIMMON.dec'])
                 parse_comments([filename='/home/greta/AXAFSHARE/dec/G_LIMMON.dec', startline=603])

    Read G_LIMMON.dec format file

    Reads in a G_LIMMON.dec or any other GRETA limit monitor specification file, such as
    G_LIMMON_SAFEMODE.dec, and returns a dictionary containing the contents of the file.
    
    :param filename: File name of GRETA limit monitoring specification file
    :returns: Dictionary containing the GRETA limit monitoring specifcation 

    Since the limit monitoring specification files generally do not explicitly list limits or
    expected states unless these states differ from those defined in the telemetry databases,
    many mnemonics listed in the output will not include their associated limits or expected
    states.

    Equations for mnemonics defined within the input file are not parsed, associated limit or
    expected state information for these mnemonics are parsed. In many cases these "derived"
    mnemonics are included in the Ska engineering archive.


**Parse G_LIMMON Comment Section**

.. function:: parse_comments([filename='/home/greta/AXAFSHARE/dec/G_LIMMON.dec', startline=603])
    Parse the comment section near the top of a G_LIMMON.dec file.

    :param filename: File name of GRETA limit monitoring specification file.
    :param startline: The line at which the comments began to follow a predictable form similar to the format described below.
    :returns: Dictionary containing parsed comments, keys are the times associated with each comment in the format returned by Chandra.Time.DateTime().sec.

    This relies upon the user editing the G_LIMMON.dec file for each revision to adhere to the
    following format:

    #   09-25-2012  Firstname Lastname Message, can be one or more lines.
    #
    #                  From                      To                      Description
    #         MSID1    LIMIT_TYPE=  Orig_Number  LIMIT_TYPE= New_Number  Description (in one line)
    #         MSID2    LIMIT_TYPE=  Orig_Number  LIMIT_TYPE= New_Number  Description (in one line)
    #         MSID3    LIMIT_TYPE=  Orig_Number  LIMIT_TYPE= New_Number  Description (in one line)

    At this time, this function only processes limit changes, expected state changes are not
    processed. The ability to parse expected state changes may be added in the future.


**Parse G_LIMMON Output File**

.. function:: process_limits_file([filename='limfile.txt'])
    Process the limit file generated using a G_LIMMON.dec type of specification.

    This processes the output of G_LIMMON or any other GRETA limit monitoring specification and
    calculates relevant statistics. 

    :param filename: File name of G_LIMMON output file
    :returns: Dictionary of limit violations and relevant statistics.

    This function is not guaranteed to be able to process limit violations resulting from
    safemodes, normal sun modes, or any other special condition that may result in corrupted
    telemetry.


**Parse GRETA Plot Specification**

.. function:: parse_decplot(decfile)
    Parse a GRETA dec plot file to extract plotting data.

    :param decfile: GRETA plot specification file name
    :returns: dictionary of plot specification details

    This will not parse text display data (e.g. FMAIN.dec) or equations.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

