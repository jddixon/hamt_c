# flags to pass to the C compiler and linker
CFLAGS = --pedantic -Wall -std=c99 -O2
LDFLAGS = -lm

lib_LTLIBRARIES = libhamt.la
libhamt_la_SOURCES = hamt.h
bin_PROGRAMS = main
main_SOURCES = main.c
main_LDADD = libhamt.la

