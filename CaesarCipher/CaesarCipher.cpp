#include <iostream>
#include <string>
using namespace std;

// Brief summary of the file contents/structure:
// This program demonstrates encryption and decryption of a string using the Caesar cipher method. It takes an input string
// and an offset key, encrypts the string by shifting each character by the offset amount, decrypts it back to the original input,
// and finally outputs the reversed original input string.

// Function to encrypt the string
string encrypt(string input, int offset) {
    string encrypted = "";
    for (char& c : input) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            encrypted += static_cast<char>((c - base + offset) % 26 + base);
        } else {
            encrypted += c;
        }
    }
    return encrypted;
}

// Function to decrypt the string
string decrypt(string input, int offset) {
    return encrypt(input, 26 - offset);
}

int main() {
    // Take input string
    string input;
    cout << "Enter a string: ";
    getline(cin, input);

    // Take offset key
    int offset;
    cout << "Enter an offset key (integer): ";
    cin >> offset;

    // Encrypt the string
    string encrypted = encrypt(input, offset);
    cout << "Encrypted string: " << encrypted << endl;

    // Decrypt the string
    string decrypted = decrypt(encrypted, offset);
    cout << "Decrypted string: " << decrypted << endl;

    // Reverse the original input using pointer arrays
    char* inputPtr = &input[0];
    char* reversed = new char[input.length() + 1];
    char* reversedPtr = reversed + input.length();

    *reversedPtr = '\0';
    while (*inputPtr != '\0') {
        *(--reversedPtr) = *(inputPtr++);
    }

    cout << "Reversed original input: " << reversed << endl;

    // Clean up allocated memory
    delete[] reversed;

    return 0;
}
