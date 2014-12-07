# flags to pass to the C compiler and linker
CFLAGS = --pedantic -Wall -std=c99 -O2
LDFLAGS = -lm

TESTS = check_hamt
check_PROGRAMS = check_hamt
check_hamt_SOURCES = check_hamt_c $(top_builddir)/src/hamt.h
check_hamt_CFLAGS = @CHECK_CFLAGS@
check_hamt_LDADD = $(top_builddir)/src/libhamt.la @CHECK_LIBS@
