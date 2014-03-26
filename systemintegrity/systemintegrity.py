#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SystemIntegrity
# A very simple system integrity script based on SHA-2
#

__appname__ = "SystemIntegrity"
__version__ = "0.1"
__author__ = "Nicolas Hennion (Thales Alenia Space)"
__licence__ = "MIT"
# Syntax
__doc__ = '''\
Usage: systemintegrity [options]

Compute hash code for file/path using the SHA-512 function

Options:
    -h:             Display help and exit
    -v:             Display version and exit
    -V:             Switch on debug mode (Verbose)
    -f <file/path>: Input file or path 
    -r:             Enable recursive mode over folder
'''

# Import lib
import getopt
import sys
import os
import logging
import hashlib
import ntpath

# Global variables
#...

# Limit import to class...
__all__ = [ ]


# Classes

class hash(object):
    """
    Main class to manage hash code for file
    """

    def __init__(self, language="eng"):
        self.hash_algo = hashlib.sha512()

    def get_hash(self, fd, block_size = 512):
        """
        Return the hexadecimal digest for the <fd>
        """
        while True:
            data = fd.read(block_size)
            if (not data): break
            self.hash_algo.update(data)
        return self.hash_algo.hexdigest()


# Functions

def printSyntax():
    """
    Display the syntax of the command line
    """
    print(__doc__)


def printVersion():
    """
    Display the current software version
    """
    print(__appname__ + " version " + __version__)


def main():
    """
    Main function
    """

    global _DEBUG_
    _DEBUG_ = False

    # No default file
    file_path = None
    # By default no recursivity when walking through folder
    recursive_tag = False

    # Manage args
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvVf:r")
    except getopt.GetoptError as err:
        # Print help information and exit:
        print("Error: " + str(err))
        printSyntax()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h"):
            printVersion()
            printSyntax()
            sys.exit(0)
        elif opt in ("-v"):
            printVersion()
            sys.exit(0) 
        elif opt in ("-f"):
            file_path = arg
        elif opt in ("-r"):
            recursive_tag = True
        elif opt in ("-V"):
            _DEBUG_ = True
            # Verbose mode is ON
            logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s %(levelname)s - %(message)s',
                datefmt='%d/%m/%Y %H:%M:%S',
            )
        # Add others options here...
        else:
            printSyntax()
            sys.exit(0)

    # By default verbose mode is OFF
    if not _DEBUG_:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s %(levelname)s - %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S',
        )
    logging.debug("Running %s version %s" % (__appname__, __version__))
    logging.debug("Debug mode is ON")

    # Test args
    if (file_path is None):
        logging.error("Need an input file or path (use the -f tag)")
        sys.exit(2)

    if (recursive_tag):
        logging.debug("Recursive mode is ON")

    # Main loop
    if (os.path.exists(file_path)):
        # File exist
        h = hash()
        if (os.path.isfile(file_path)):
            # This is a file
            try:
                fd = open(file_path)
            except Exception, e:
                logging.error("Can not open file %s" % file_path)
            else:                    
                logging.debug("Compute hash for %s" % file_path)
                print "{} {}".format(h.get_hash(fd), file_path)
        elif (os.path.isdir(file_path)):
            # This is a path
            logging.debug("Walk recursively into %s" % file_path)
            # Recursive loop over path
            if (recursive_tag):
                # Recursive loop over path
                all_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(file_path) for f in filenames]
            else:
                # Only file in the path (no recursivity)
                all_files = [os.path.join(file_path, f) for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
            # Test file
            # Compute hash for file
            for f in all_files:
                try:
                    fd = open(f)
                except Exception, e:
                    logging.error("Can not open file %s" % f)
                else:
                    logging.debug("Compute hash for %s" % f)
                    print "{} {}".format(h.get_hash(fd), f)
    else:
        # File did not exist
        logging.error("%s did not exist" % file_path)
        sys.exit(1)

    logging.debug("The end...")


# Main
#=====

if __name__ == "__main__":
    main()
    sys.exit(0)

# The end...
