# flags to pass to the C compiler and linker
# dropped --pedantic
AM_CFLAGS = -Wall -std=c99 -O2

bin_PROGRAMS = main
# our 'primary':
lib_LTLIBRARIES = libhamt.la

# This builds a .so:
libhamt_la_SOURCES = hamt.c hamt.h

# This works, but the major/minor/micro numbers are interpreted as
# current/age/revision.
#libhamt_la_LDFLAGS = -version-info @HAMT_LD_VERSION@

# The line above stopped working; this one still works:
libhamt_la_LDFLAGS = -version-info 0:0:0

main_SOURCES = main.c
main_LDADD = libhamt.la

