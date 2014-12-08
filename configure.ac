#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])

m4_define([hamt_major_version],[0])
m4_define([hamt_minor_version],[0])
m4_define([hamt_micro_version],[0])
m4_define([hamt_version],
          [hamt_major_version.hamt_minor_version.hamt_micro_version])
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

