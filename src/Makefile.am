# flags to pass to the C compiler and linker
# dropped --pedantic
AM_CFLAGS = -Wall -std=c99 -O2

bin_PROGRAMS = main

# list of libraries to build
lib_LTLIBRARIES = libhamt.la

# This library's dependencies.
libhamt_la_SOURCES = hamt.c hamt.h
# This header is public and needed to use the library
include_HEADERS = hamt.h

# See VERSIONING in configure.am for an explanation of how the library
# version number is handled.

#libhamt_la_LDFLAGS = -version-info @HAMT_LD_VERSION@
libhamt_la_LDFLAGS = -version-info '0:0:0'

main_SOURCES = main.c
main_LDADD = libhamt.la

