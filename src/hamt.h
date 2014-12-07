/* hamt.h */

#ifndef _HAMT_H_
#define _HAMT_H_

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>         // for malloc, free, etc

// const.go ---------------------------------------------------------
#define MAX_W (uint64_t(6))

// hamt_go/keyI.go --------------------------------------------------

// A Key is anything that returns an unsigned 64-bit value.
//type KeyI interface {
//	Hashcode() uint64
//}

uint64_t Hashcode();    // just a reminder of what the interface is

// hamt_go/nodeI.go -------------------------------------------------

//type HTNodeI interface {
//	IsLeaf() bool
//}
bool IsLeaf();          // another reminder

#endif // _HAMT_H_
