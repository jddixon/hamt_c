# hamt_c

A C implementation of the HAMT data structure.  This is a translation
of the Golang (Go programming language)
[htmt_go github project.](https://jddixon.github.io/hamt_go)

A **Hash Array Mapped Trie** ([*HAMT*][bagwell2001])
provides fast and memory-efficient access to large amounts of data held
in memory.  Values are stored by **key**.  All HAMT keys are mapped into
fixed length unsigned integers. In this implementation these are 64 bits
long, `uint64`s.  The **value** may be of any type but typically is a
pointer to a data structure of interest.

The HAMT trie is essentially a prefix trie where the nodes in the tree
are either tables or leaf entries.

In a simpler implementation at each level there is either a leaf node
or a table with up to `2^w` slots, where `w` is a small
integer.  The next `w` bits of the hash
derived from the key are construed as an index into that table.  The
table grows dynamically as entries are added.  Whenever there is a
collision at a given level, a child table replaces the current entry,
and both new and old entries move to the child table, possibly
recursing in the process.

The current Go implementation has been tested with values of
3, 4, 5, and 6 for `w`.  Preliminary performance tests indicate
that `w=6` is optimal.  That is, a table with 64 slots gives the best
performance.

An enhancement introduces a fixed size table at the root.  This is
characterized by another small integer `t`: the root has 2^t entries
and the table at the root is indexed by the first t bits of the
key's hashcode.  Go language erformance tests show that for optimal performance
the root table should approach the total number of entries in size.

A further enhancement would allow dynamic resizing of the root table.
This has not yet been implemented.

Whereas a normal hash table would be quite large and might
require expensive resizing periodically, the HAMT data structure is roughly
as fast as a hash table, but starts small and consumes more memory only
as needed.

## Limitations

* This code is not thread-safe.  That is, using code must provide any
necessary locking.

* the HAMT algorithm depends upon bit-counting.  On modern Intel and AMD
processors this
can be done using a specific machine-language instruction, `POPCNT`.  The current
implementation of hamt_c emulates this in software using the
[SWAR][wiki-swar] algorithm,  The emulation code is on the order of ten times
slower than the machine instruction.
*In practice `POPCNT` emulation might slow down accesses by something like 10%,
because the emulation code simply is not run all that often.*
*This is of course not actually a limitation, but rather an observation: the
HAMT algorithm runs faster with hardware support.*

## Project Status

This C version of the HAMT algorithm is currently being translated from the
Go language version,
More information on the **hamt_go** project can be found [here](https://jddixon.github.io/hamt_go)

The Golang code works and is reasonably well-tested.
`Insert`, `Find`, and `Delete` operations, while not yet thoroughly optimized,
take on the order of 1.3 microseconds each on a lightly-loaded server
(about 2.6us each to insert a million values and verify that the
value can be found using the key).  As the root table approaches the
number of entries in size, this falls to about 1.2 us, or 600ns/op.

These figures were obtained from *single-threaded* tests.

## References

[Bagwell, "Ideal Hash Trees"][bagwell2001]  (2001 PDF)

[Wikipeida, "Hash array mapped trie"][wiki-hamt]

[Wikipedia, "SWAR"][wiki-swar]


[bagwell2001]: http://infoscience.epfl.ch/record/64398/files/idealhashtrees.pdf

[wiki-hamt]: http://en.wikipedia.org/wiki/Hash_array_mapped_trie

[wiki-swar]: http://en.wikipedia.org/wiki/SWAR


## On-line Documentation

More information on the **hamt_c** project can be found
[here](https://jddixon.github.io/hamt_c)
