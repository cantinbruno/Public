#include <openssl/evp.h>
#include <openssl/err.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
int main(int argc, char *argv[]){ 

// Initialiser les algorithmes
ERR_load_crypto_strings();
OpenSSL_add_all_algorithms(); 

// Récupérer la clé et les noms de fichier
unsigned char *cle = (unsigned char *)argv[1];
int input= open(argv[2], O_RDONLY);
int output= open(argv[3], O_WRONLY | O_CREAT | O_TRUNC, 0644);

// Initialiser le chiffrement
EVP_CIPHER_CTX *ctx;
ctx = EVP_CIPHER_CTX_new();
EVP_EncryptInit(ctx, EVP_aes_256_cbc(), cle, NULL);
 
// Chiffrer le fichier
unsigned char buf[1024];
int lu;
while ((lu = read(input, buf, sizeof(buf))) > 0) {
int ecrit;
EVP_EncryptUpdate(ctx, buf, &ecrit, buf, lu);
write(output, buf, ecrit);}

// Finaliser le chiffrement
int ecit;
EVP_EncryptFinal(ctx, buf, &ecrit);
write(output, buf, ecrit);

// Nettoyer et libérer la mémoire
EVP_CIPHER_CTX_free(ctx);
close(input);
close(output);
EVP_cleanup();
ERR_free_strings();

return 0;
}
