# flags to pass to the C compiler and linker
# dropped --pedantic
AM_CFLAGS = -Wall -std=c99 -O2

%.o:	%.c
	gcc -c $(AM_CFLAGS) -o $@ $<

%.lo:	%.c
	gcc -c $(CFLAGS) $(AM_CFLAGS) -o $*.o  $<
	gcc -c $(CFLAGS) $(AM_CFLAGS) -fPIC -o $*.pic.o $<
	touch $@

bin_PROGRAMS = main
lib_LTLIBRARIES = libhamt.la

#main_SOURCES = main.c
#main_LDADD = libhamt.la

libhamt_la_SOURCES = hamt.c hamt.h


