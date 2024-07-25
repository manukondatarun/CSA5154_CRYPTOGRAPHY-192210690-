#include<stdio.h>
#include<string.h>
#include<ctype.h>
void encrypt(char*plaintext,const char*key) 
{
    char ciphertext[strlen(plaintext)+1];
    int i;
    for (i=0;plaintext[i]!='\0';i++) 
	{
        char ch = plaintext[i];
        if (isupper(ch)) 
		{
            ciphertext[i]=key[ch-'A'];
        }
        else if (islower(ch)) 
		{
            ciphertext[i]=tolower(key[ch-'a']);
        }
        else 
		{
            ciphertext[i]=ch;
        }
    }
    ciphertext[i]='\0'; 
    printf("Encrypted string:%s\n",ciphertext);
}
int main() 
{
    char plaintext[100];
    char key[27];
    printf("tarun(192210690)");
    printf("\nEnter a string:");
    fgets(plaintext,sizeof(plaintext),stdin);
    plaintext[strcspn(plaintext,"\n")]='\0';
    printf("Enter the 26-character substitution key: ");
    fgets(key,sizeof(key),stdin);
    key[strcspn(key,"\n")]='\0';
    if (strlen(key)!=26) 
	{
        printf("Invalid key\n");
        return 1;
    }
    encrypt(plaintext, key);
    return 0;
}
