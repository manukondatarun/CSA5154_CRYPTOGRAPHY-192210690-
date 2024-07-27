#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void rail_fence_encrypt(char *text, int key, char *encrypted) {
    int len = strlen(text);
    char rail[key][len];

    // Initialize the rail matrix with new line characters
    for (int i = 0; i < key; i++)
        for (int j = 0; j < len; j++)
            rail[i][j] = '\n';

    // To find the direction
    int dir_down = 0;
    int row = 0, col = 0;

    for (int i = 0; i < len; i++) {
        // Reverse the direction if we've just filled the top or bottom rail
        if (row == 0 || row == key - 1)
            dir_down = !dir_down;

        // Fill the corresponding alphabet
        rail[row][col++] = text[i];

        // Find the next row using direction flag
        if (dir_down)
            row++;
        else
            row--;
    }

    // Now we can construct the cipher using the rail matrix
    int k = 0;
    for (int i = 0; i < key; i++)
        for (int j = 0; j < len; j++)
            if (rail[i][j] != '\n')
                encrypted[k++] = rail[i][j];
    encrypted[k] = '\0';
}

void rail_fence_decrypt(char *cipher, int key, char *decrypted) {
    int len = strlen(cipher);
    char rail[key][len];

    // Initialize the rail matrix with new line characters
    for (int i = 0; i < key; i++)
        for (int j = 0; j < len; j++)
            rail[i][j] = '\n';

    // To find the direction
    int dir_down = 0;
    int row = 0, col = 0;

    // Mark the places with '*'
    for (int i = 0; i < len; i++) {
        if (row == 0)
            dir_down = 1;
        if (row == key - 1)
            dir_down = 0;

        // Place the marker
        rail[row][col++] = '*';

        // Find the next row using direction flag
        if (dir_down)
            row++;
        else
            row--;
    }

    // Now we can construct the rail matrix
    int index = 0;
    for (int i = 0; i < key; i++)
        for (int j = 0; j < len; j++)
            if (rail[i][j] == '*' && index < len)
                rail[i][j] = cipher[index++];

    // Read the matrix in a zig-zag manner to get the plaintext
    int k = 0;
    dir_down = 0;
    row = 0, col = 0;

    for (int i = 0; i < len; i++) {
        if (row == 0)
            dir_down = 1;
        if (row == key - 1)
            dir_down = 0;

        if (rail[row][col] != '*')
            decrypted[k++] = rail[row][col++];
        
        if (dir_down)
            row++;
        else
            row--;
    }
    decrypted[k] = '\0';
}

int main() {
    printf("Tarun(192210690)\n");

    char plain_text[] = "HELLO";
    int key = 3;
    char encrypted[100];
    char decrypted[100];

    rail_fence_encrypt(plain_text, key, encrypted);
    printf("Encrypted: %s\n", encrypted);

    rail_fence_decrypt(encrypted, key, decrypted);
    printf("Decrypted: %s\n", decrypted);

    return 0;
}
