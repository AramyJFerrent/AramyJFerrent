#ifndef DOUBLELINKEDLIST_H
#define DOUBLELINKEDLIST_H

/* 
 * Name: [Your Name]
 * Course and Section: [Your Course and Section Number]
 * Project Number: [Your Project Number]
 * Brief Summary: This header file defines the DoubleLinkedList class, which represents a doubly linked list. 
 * The class includes functions for inserting, merging, and removing elements, as well as accessing elements by index
 * and displaying the list contents.
 */

class DoubleLinkedList {
private:
    struct Node {
        int data;
        Node* next;
        Node* prev;
    };

    Node* head;     // Pointer to the first node in the list
    Node* tail;     // Pointer to the last node in the list
    int count;      // Number of elements in the list

public:
    // Constructor
    DoubleLinkedList();

    // Destructor
    ~DoubleLinkedList();

    // Insert a new element into the list
    void insert(int value);

    // Merge another list into this list
    void merge(DoubleLinkedList* absorbedList);

    // Remove an element from the list
    void remove(int value);

    // Overloaded [] operator to access elements by index
    const int& operator[](int index) const;

    // Get the number of elements in the list
    int getCount() const;

    // Display the list contents
    void display(bool reverse = false) const;
};

// Exception class for index out of bounds
class IndexOutOfBoundsException {};

#endif
