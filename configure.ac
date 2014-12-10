#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])

# make sure we are in the right directory
AC_CONFIG_SRCDIR([src/Makefile.am])

# LIBRARY VERSIONING ################################################
#
# See https://www.gnu.org/software/libtool/manual/html_node/Updating-version-info.html
#
# The libtool version number is not normally the component version number.
# Serialized, libtool's version-info consists of one to three numbers, 
# CURRENT:REVISION[:AGE].  CURRENT is the interface version number.
# Conventionally CURRENT is incremented before each public releast, except 
# that where interfaces have only been added, CURRENT is unchanged and 
# REVISION and AGE areincremented.  CURRENT is also incremented if any 
# interfaces have been changed or removed, in which case, REVISION and AGE 
# are zeroed.  If AGE is non-zero, the library implements all interfaces 
# between CURRENT - AGE and CURRENT, inclusive.
# 
# Given these rules, AGE may not exceed CURRENT.

HAMT_CURRENT="0" 
HAMT_REVISION="0"     
HAMT_AGE="0"     
HAMT_LD_VERSION="$HAMT_CURRENT:$HAMT_REVISION:$HAMT_AGE"
AC_SUBST(HAMT_LD_VERSION)

# PACKAGE VERSION ###################################################

m4_define([hamt_major_version],[0])
m4_define([hamt_minor_version],[0])
m4_define([hamt_micro_version],[0])
m4_define([hamt_version],
          [hamt_major_version.hamt_minor_version.hamt_micro_version])

# INITIALIZATION ####################################################

AC_INIT([hamt], [hamt_version], [hamt-dev at xlattice dot org])

AM_PROG_AR
LT_INIT()

AC_CONFIG_MACRO_DIR([m4])
AC_PROG_MAKE_SET

# Dropped -Werror, warnings treated as errors
AM_INIT_AUTOMAKE([-Wall foreign 1.11.2])

# Checks for programs.
AC_PROG_CC
AC_PROG_LIBTOOL

# Checks for libraries.
AM_PROG_CC_C_O

# Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADERS([stdlib.h])

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.

# Output files
AC_CONFIG_HEADERS([config.h])

AC_OUTPUT(Makefile 
          src/Makefile 
          doc/Makefile 
          examples/Makefile 
          man/Makefile 
          scripts/Makefile 
          tests/Makefile)

