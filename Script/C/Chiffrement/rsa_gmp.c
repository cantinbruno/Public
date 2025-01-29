
/*===========================================================================*\
*                                                                             *
*                                  rsa_gmp.c                                  *
*                                                                             *
*=============================================================================*
*                                                                             *
* Copyright (c) 2014 - Nicolas PAGLIERI                                       *
*                                                                             *
* This software may be used under the terms of the GNU General Public         *
* License version 3 as published by the Free Software Foundation              *
* <https://www.gnu.org/copyleft/gpl.html>                                     *
*                                                                             *
* This software is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE *
* WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.   *
*                                                                             *
* --------------------------------------------------------------------------- *
*                                                                             *
* IMPORTANT DISCLAIMER: THE PURPOSE OF THIS FILE IS SOLELY EDUCATIONAL        *
*                       DO NOT USE THIS PROGRAM IN ANY OTHER CONTEXT          *
*                       OR IF YOU INTEND TO PROTECT SENSITIVE INFORMATION     *
*                                                                             *
* The cryptographic primitives presented here are ALL BUT SECURE; their only  *
* purpose is to demonstrate the basic operation of the RSA cryptosystem. The  *
* source code contains several intentional implementation flaws that strongly *
* affect the overall security of the cipher methods. Be wise, don't use them! *
*                                                                             *
*                                                                             *
\*===========================================================================*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "gmp.h"


// Compile this file with:
//
//        gcc rsa_gmp.c -lgmp -o rsa_gmp
//
// You can also specify another public exponent at compile time by running:
//
//        gcc rsa_gmp.c -DPUB_EXP=65537 -lgmp -o rsa_gmp
//


// ========================================================================== //
//                             UTILITY FUNCTIONS                              //
// -------------------------------------------------------------------------- //

// Maximum message size
#define MAX_SIZE 255

// The caller must free s after use
void decode(char** s, mpz_t z) {
	size_t sz;
	*s = mpz_export(NULL,&sz,1,sizeof(char),0,0,z);
	*s = (char*) realloc(*s, (sz+1)*sizeof(char));
	(*s)[sz] = '\0';
}

// The caller must ensure that s ends with '\0'
void encode(char* s, mpz_t z) {
	mpz_import(z,strlen(s),1,sizeof(char),0,0,s);
}

// ========================================================================== //
//                             CRYPTO PRIMITIVES                              //
// -------------------------------------------------------------------------- //

#ifndef PUB_EXP
#define PUB_EXP 3
#endif

typedef struct {
	mpz_t n; // Modulus
	mpz_t e; // Public Exponent
} public_key;

typedef struct {
	mpz_t n; // Modulus
	mpz_t d; // Private exponent
} private_key;

void encrypt(public_key *pub, mpz_t cleartext, mpz_t ciphertext) {
    

	# TODO

}

void decrypt(private_key *priv, mpz_t ciphertext, mpz_t cleartext) {


	#TODO

}

void generate_keys(int bits, public_key *pub, private_key *priv) {

	// Allocate GMP temporary variables
	mpz_t p, q, n, pm1, qm1, phi, e, d, t;
	mpz_init(p); mpz_init(q); mpz_init(n); mpz_init(pm1); mpz_init(qm1);
	mpz_init(phi); mpz_init(e); mpz_init(d); mpz_init(t);

	// Initialize random generation context
	gmp_randstate_t rs;
	gmp_randinit_default(rs);

	// -------------------------------------------------------------------------
	// Generate two random large prime numbers (p,q) such that:
	//   p != q
	//   log2(p) >= bits/2
	//   log2(q) >= bits/2

	// Generate some random data using the random generation context
	mpz_urandomb(t, rs, bits/2);
	// Set MSB to 1 to ensure the actual size is (bits/2)
	mpz_setbit(t, bits/2-1);
	// Also, set second MSB to 1 to avoid Fermat primes ( 2^(2b) + 1 ), etc...
	mpz_setbit(t, bits/2-2);
	// Pick p prime
	mpz_nextprime(p, t);
	// Pick q prime greater than p
	mpz_nextprime(q, p);

	// -------------------------------------------------------------------------
	// Compute public modulus
	//   n = p * q
	mpz_mul(n, p, q);
	//   phi = (p-1) * (q-1)
	mpz_sub_ui(pm1, p, 1);
	mpz_sub_ui(qm1, q, 1);
	mpz_mul   (phi, pm1, qm1);

	// -------------------------------------------------------------------------
	// Look for a small exponent e coprime with phi  ( gcd(phi,e) == 1 )
	mpz_set_ui(e, PUB_EXP);
	mpz_gcd(t, e, phi);
	while (mpz_cmp_ui(t, 1)) {
		mpz_nextprime(e, e);
		mpz_gcd(t, e, phi);
	}

	// -------------------------------------------------------------------------
	// Determine the private exponent  ( d = e^{-1} mod phi )
	mpz_invert(d, e, phi);

	// -------------------------------------------------------------------------
	// Export data
	mpz_set( pub->n, n);
	mpz_set(priv->n, n);
	mpz_set( pub->e, e);
	mpz_set(priv->d, d);

	// -------------------------------------------------------------------------
	// Free the random generation context
	gmp_randclear(rs);

	// Free GMP temporary variables
	mpz_clear(p); mpz_clear(q); mpz_clear(n); mpz_clear(pm1); mpz_clear(qm1);
	mpz_clear(phi); mpz_clear(e); mpz_clear(d); mpz_clear(t);
}


// ========================================================================== //
//                            PROGRAM ENTRY POINT                             //
// -------------------------------------------------------------------------- //

int main(int argc, char* argv[]) {

	size_t s;
	char msg[MAX_SIZE+1] = {0};

	private_key priv;
        public_key  pub;

	mpz_t msgz, msge, msgd;
	mpz_init(msgz); mpz_init(msge); mpz_init(msgd);
	mpz_init(pub.n); mpz_init(pub.e); mpz_init(priv.n); mpz_init(priv.d);

	printf("Please type a message to encrypt: ");
	fgets(msg, MAX_SIZE, stdin);
	msg[MAX_SIZE] = '\0';
	s = strlen(msg);
	if (msg[s-1]=='\n')  msg[--s]='\0';
        s = MAX_SIZE;
	encode(msg, msgz);
	gmp_printf("\nYou typed in\n\t'%s'\n\tCleartext: 0x%ZX\n", msg, msgz);

	// int i=3; while (i--)
	{
	printf("\nGenerating %zu bits keypair...\n", (s+1)*8);
	generate_keys((s+1)*8, &pub, &priv);

	gmp_printf("\tPublic  modulo  : 0x%ZX\n", pub.n);
	gmp_printf("\tPublic  exponent: 0x%ZX\n", pub.e);
	gmp_printf("\tPrivate exponent: 0x%ZX\n", priv.d);
	}
	//

	printf("\nEncrypting message ");
	encrypt(&pub, msgz, msge);
	gmp_printf("\tCiphertext: 0x%ZX\n", msge);

	printf("\nDecrypting message ");
	decrypt(&priv, msge, msgd);
	gmp_printf("\tCleartext: 0x%ZX\n", msgd);
	char *dec = NULL;
	decode(&dec, msgd);
	printf("\t'%s'\n", dec);

	mpz_clear(msgz); mpz_clear(msge); mpz_clear(msgd);
	mpz_clear(pub.n); mpz_clear(pub.e); mpz_clear(priv.n); mpz_clear(priv.d);

	int ret = strncmp(msg, dec, MAX_SIZE+1);
	if (ret) printf("\nError: the messages differ\n");
	else     printf("\nAll good :)\n");

	free(dec);
	return ret;

}
