# Identity-Based Encryption Scheme

## IBE Basic

### Setup

### Extract

### Encrypt

### Decrypt

## IBE with Chosen Ciphertext Security

package IBE_Group1

import (
	"C"
	"crypto/sha256"
	"fmt"
	"github.com/Nik-U/pbc"
)

func something() {
	fmt.Printf("klnl")
	// rbits = k, qbits = q
	params := pbc.GenerateA(160, 512)

	pairing := params.NewPairing(params)
	G1 := pairing.NewG1()
	G2 := pairing.NewG2()
	// Check if pairing symmetric
	if !pairing.IsSymmetric() {
		fmt.Printf("Error - pairing not symmetric")
	}
	GT := pairing.NewGT()
	//fmt.Printf("%v", G1.Rand())

	fmt.Printf("c = %v", C.random())

	H1 := sha256.Sum256([]byte("orsbf"))
}