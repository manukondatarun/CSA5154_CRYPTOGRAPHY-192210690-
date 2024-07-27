#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void fill_matrix_encrypt(char *text, char **matrix, int num_rows, int num_cols) {
    int len = strlen(text);
    for (int i = 0; i < len; i++) {
        int row = i / num_cols;
        int col = i % num_cols;
        matrix[row][col] = text[i];
    }
}

void read_matrix_encrypt(char **matrix, char *encrypted_text, int num_rows, int num_cols, int *sorted_key_indices) {
    int k = 0;
    for (int col = 0; col < num_cols; col++) {
        int sorted_col = sorted_key_indices[col];
        for (int row = 0; row < num_rows; row++) {
            if (matrix[row][sorted_col] != '\0') {
                encrypted_text[k++] = matrix[row][sorted_col];
            }
        }
    }
    encrypted_text[k] = '\0';
}

void columnar_transposition_encrypt(char *text, char *key, char *encrypted_text) {
    int len = strlen(text);
    int num_cols = strlen(key);
    int num_rows = (len + num_cols - 1) / num_cols;

    // Create and initialize the matrix
    char **matrix = (char **)malloc(num_rows * sizeof(char *));
    for (int i = 0; i < num_rows; i++) {
        matrix[i] = (char *)malloc(num_cols * sizeof(char));
        memset(matrix[i], '\0', num_cols);
    }

    // Fill the matrix with the text
    fill_matrix_encrypt(text, matrix, num_rows, num_cols);

    // Generate sorted key indices
    int *sorted_key_indices = (int *)malloc(num_cols * sizeof(int));
    for (int i = 0; i < num_cols; i++) {
        sorted_key_indices[i] = i;
    }
    for (int i = 0; i < num_cols - 1; i++) {
        for (int j = i + 1; j < num_cols; j++) {
            if (toupper(key[sorted_key_indices[i]]) > toupper(key[sorted_key_indices[j]])) {
                int temp = sorted_key_indices[i];
                sorted_key_indices[i] = sorted_key_indices[j];
                sorted_key_indices[j] = temp;
            }
        }
    }

    // Read the matrix columns based on the key
    read_matrix_encrypt(matrix, encrypted_text, num_rows, num_cols, sorted_key_indices);

    // Free the matrix memory
    for (int i = 0; i < num_rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
    free(sorted_key_indices);
}

void fill_matrix_decrypt(char *ciphertext, char **matrix, int num_rows, int num_cols, int num_empty_cells, int *sorted_key_indices) {
    int idx = 0;
    for (int i = 0; i < num_cols; i++) {
        int col = sorted_key_indices[i];
        for (int row = 0; row < num_rows; row++) {
            if (!(row == num_rows - 1 && col >= num_cols - num_empty_cells)) {
                matrix[row][col] = ciphertext[idx++];
            }
        }
    }
}

void read_matrix_decrypt(char **matrix, char *decrypted_text, int num_rows, int num_cols) {
    int k = 0;
    for (int row = 0; row < num_rows; row++) {
        for (int col = 0; col < num_cols; col++) {
            if (matrix[row][col] != '\0') {
                decrypted_text[k++] = matrix[row][col];
            }
        }
    }
    decrypted_text[k] = '\0';
}

void columnar_transposition_decrypt(char *ciphertext, char *key, char *decrypted_text) {
    int len = strlen(ciphertext);
    int num_cols = strlen(key);
    int num_rows = (len + num_cols - 1) / num_cols;
    int num_empty_cells = num_cols * num_rows - len;

    // Create and initialize the matrix
    char **matrix = (char **)malloc(num_rows * sizeof(char *));
    for (int i = 0; i < num_rows; i++) {
        matrix[i] = (char *)malloc(num_cols * sizeof(char));
        memset(matrix[i], '\0', num_cols);
    }

    // Generate sorted key indices
    int *sorted_key_indices = (int *)malloc(num_cols * sizeof(int));
    for (int i = 0; i < num_cols; i++) {
        sorted_key_indices[i] = i;
    }
    for (int i = 0; i < num_cols - 1; i++) {
        for (int j = i + 1; j < num_cols; j++) {
            if (toupper(key[sorted_key_indices[i]]) > toupper(key[sorted_key_indices[j]])) {
                int temp = sorted_key_indices[i];
                sorted_key_indices[i] = sorted_key_indices[j];
                sorted_key_indices[j] = temp;
            }
        }
    }

    // Rebuild the matrix
    fill_matrix_decrypt(ciphertext, matrix, num_rows, num_cols, num_empty_cells, sorted_key_indices);

    // Read the matrix rows to get the plaintext
    read_matrix_decrypt(matrix, decrypted_text, num_rows, num_cols);

    // Free the matrix memory
    for (int i = 0; i < num_rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
    free(sorted_key_indices);
}

int main() {
    printf("Tarun(192210690)\n");

    char plain_text[] = "HELLOFROMPYTHON";
    char key[] = "KEY";
    char encrypted[100];
    char decrypted[100];

    columnar_transposition_encrypt(plain_text, key, encrypted);
    printf("Encrypted: %s\n", encrypted);

    columnar_transposition_decrypt(encrypted, key, decrypted);
    printf("Decrypted: %s\n", decrypted);

    return 0;
}
