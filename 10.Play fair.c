#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define SIZE 5

void generateKeyTable(char key[], char table[SIZE][SIZE]) {
    int used[26] = {0}, k = 0;
    for (int i = 0; key[i]; i++) {
        if (key[i] == 'j') key[i] = 'i';
        if (!used[key[i] - 'a']) table[k / SIZE][k % SIZE] = key[i], used[key[i] - 'a'] = 1, k++;
    }
    for (int i = 0; i < 26; i++) if (!used[i] && (i + 'a') != 'j') table[k / SIZE][k % SIZE] = 'a' + i, k++;
}

void processText(char *text, char *output) {
    for (int i = 0, j = 0; text[i]; i++) if (isalpha(text[i])) output[j++] = (text[i] == 'j' ? 'i' : tolower(text[i]));
    for (int i = 0, j = 0; output[i]; i += 2) {
        if (!output[i + 1] || output[i] == output[i + 1]) {
            memmove(output + i + 2, output + i + 1, strlen(output) - i);
            output[i + 1] = 'x';
        }
    }
}

void findPosition(char table[SIZE][SIZE], char ch, int *row, int *col) {
    for (int i = 0; i < SIZE * SIZE; i++) if (table[i / SIZE][i % SIZE] == ch) *row = i / SIZE, *col = i % SIZE;
}

void encrypt(char text[], char table[SIZE][SIZE], char output[]) {
    int row1, col1, row2, col2;
    for (int i = 0; text[i]; i += 2) {
        findPosition(table, text[i], &row1, &col1);
        findPosition(table, text[i + 1], &row2, &col2);
        if (row1 == row2) output[i] = table[row1][(col1 + 1) % SIZE], output[i + 1] = table[row2][(col2 + 1) % SIZE];
        else if (col1 == col2) output[i] = table[(row1 + 1) % SIZE][col1], output[i + 1] = table[(row2 + 1) % SIZE][col2];
        else output[i] = table[row1][col2], output[i + 1] = table[row2][col1];
    }
}

int main() {
    char key[SIZE * SIZE], table[SIZE][SIZE], text[100], processedText[100], encryptedText[100];
printf("tarun(192210690)");
    printf("\nEnter key: ");
    fgets(key, sizeof(key), stdin);
    key[strcspn(key, "\n")] = 0;

    printf("Enter plaintext: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = 0;

    generateKeyTable(key, table);
    processText(text, processedText);
    encrypt(processedText, table, encryptedText);

    printf("Encrypted text: %s\n", encryptedText);
    return 0;
}
