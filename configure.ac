#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])

# PACKAGE VERSION ###################################################
# Set the package version here.  The library version data is in a 
# separate section, below.
#
m4_define([hamt_major_version],[0])
m4_define([hamt_minor_version],[0])
m4_define([hamt_micro_version],[0])
m4_define([hamt_version],
          [hamt_major_version.hamt_minor_version.hamt_micro_version])

# INITIALIZATION ####################################################

AC_INIT([hamt], [hamt_version], [hamt-dev at xlattice dot org])

# LIBRARY VERSIONING ################################################
# 
# This section must follow AC_INIT
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
#
# SET THE LIBRARY VERSION HERE:
HAMT_CURRENT='0'    # increment if interface changed or deleted, zero others
HAMT_REVISION='0'   # increment revision and age if interface added and
HAMT_AGE='0'        #   none changed or deleted

HAMT_LD_VERSION="$HAMT_CURRENT:$HAMT_REVISION:$HAMT_AGE"
AC_SUBST([HAMT_LD_VERSION])

# XXX PLAYING AROUND XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# works
GEEP2='geep2'
AC_SUBST([GEEP2]) 

# works
GEEP3="geep3"
AC_SUBST(GEEP3)

# This works:
GEEP4='geep4 value'
AC_SUBST([GEEP4])

# works
AC_SUBST([GEEP5], [geep5 value])

# works
GEEP7=[geep7]
AC_SUBST(m4_toupper(GEEP7))
# XXX END PLAY  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# make sure we are in the right directory
AC_CONFIG_SRCDIR([config.h.in])
AC_CONFIG_HEADERS([config.h])

AM_PROG_AR
LT_INIT()

AC_CONFIG_MACRO_DIR([m4])
AC_PROG_MAKE_SET

# Dropped -Werror, warnings treated as errors
AM_INIT_AUTOMAKE([-Wall foreign 1.11.2])

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
