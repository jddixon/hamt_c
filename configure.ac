#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])

# PACKAGE VERSION ###################################################

# This is not the library version info, which is set separately and 
# generally much less frequently.

# The minor version number should be stepped whenever the interface changes, 
# and the decimal number is then set to zero.  That is, this can be seen as
# a count of minor revisions to the current API.
#
# Where bug fixes and other code changes do not affect the package interface, 
# the minor version number is left unchanged and the decimal number is stepped.
# In other words, the decimal version number can usually be interpreted as a 
# count of bugs found in the current revision.
# 
# When there is a major change to the package API the major version number is 
# incremented and the minor and decimal version numbers are set to zero.

# SET THE PACKAGE VERSION HERE ############################
m4_define([hamt_major_version],[0])
m4_define([hamt_minor_version],[0])
m4_define([hamt_decimal_version],[4])
# #########################################################

m4_define([hamt_version],
          [hamt_major_version.hamt_minor_version.hamt_decimal_version])

# This approach doesn't work --------------------
# HAMT_MAJOR_VERSION=1
# HAMT_MINOR_VERSION=2
# HAMT_DECIMAL_VERSION=3
# hv = $HAMT_MAJOR_VERSION.$HAMT_MINOR_VERSION.$HAMT_DECIMAL_VERSION
# hamt_version = '$hv'
# END not yet -----------------------------------

# INITIALIZATION ####################################################

# This must be called before doing anything that produces output, and
# so before any AC_SUBST

AC_INIT([hamt_c], [hamt_version], [hamt-c-dev at xlattice dot org])

# LIBRARY VERSIONING ################################################
# 
# Also see 
#   https://www.gnu.org/software/libtool/manual/html_node/Updating-version-info.html
#
# The libtool version number is not normally the package version number.
# Serialized, libtool's version-info consists of one to three numbers, 
# CURRENT[:REVISION[:AGE]].  CURRENT is the interface version number.
# Conventionally version information is only updated before a public releast.
# Rules: (1) If the library source code has been changed at all, increment
# the revision number.  (2) If any interfaces have been added, removed, or
# changed, increment CURRENT and set REVISION to zero.  (3) If any interfaces
# have been added, increment AGE except that (4) if any interfaces have been
# removed or changed, set AGE to zero.
# 
# Given these rules, it should be obvious that AGE may not exceed CURRENT.
# 
# The Linux library file names are determined by these numbers.  They are
#   (a) libhamt.so.CURRENT-AGE.AGE.REVISION
#   (b) libhamt.so.CURRENT-AGE
#   (c) libhamt.so
# If for example CURRENT=5, REVISION=3, and AGE=1, then the library 
# names will be 
#   (a) libhamt.so.4.1.3
#   (b) libhamt.so.4
#   (c) libhamt.so
#
# SET THE LIBRARY VERSION INFO HERE: ######################
HAMT_CURRENT=0
HAMT_REVISION=0
HAMT_AGE=0
# #########################################################

HAMT_LD_VERSION=$HAMT_CURRENT:$HAMT_REVISION:$HAMT_AGE
AC_SUBST([HAMT_LD_VERSION])

# END LIBRARY VERSIONING ############################################

# make sure we are in the right directory
AC_CONFIG_SRCDIR([config.h.in])
AC_CONFIG_HEADERS([config.h])

AM_PROG_AR
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_AUX_DIR([config])
LT_INIT()

AC_PROG_MAKE_SET

# Possibly add gnits or --gnits; see
#   http://www.gnu.org/software/automake/manual/html_node/Gnits.html

# -Werror means warnings treated as errors
AM_INIT_AUTOMAKE([-Wall -Werror foreign 1.11.2])

# Checks for programs.
AC_PROG_CC
AC_PROG_LIBTOOL

AC_PROG_CXX
AC_PROG_AWK
AC_PROG_CC
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AC_PROG_RANLIB

# Checks for libraries.

# FIXME: Replace `main' with a function in `-lm':
AC_CHECK_LIB([m], [main])

# Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADERS([stdint.h stdlib.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_CHECK_HEADER_STDBOOL
AC_TYPE_UINT32_T
AC_TYPE_UINT64_T

# Checks for library functions.

AC_CONFIG_FILES([Makefile
                 doc/Makefile
                 examples/Makefile
                 man/Makefile
                 scripts/Makefile
                 src/Makefile
                 tests/Makefile])

AC_OUTPUT
