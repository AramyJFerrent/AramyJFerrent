#include "DoubleLinkedList.h"
#include <iostream>

/* 
 * This file contains the implementation of the functions declared in DoubleLinkedList.h. 
 * It defines the behavior of the DoubleLinkedList class, including inserting, merging, removing elements,
 * accessing elements by index, and displaying the list contents.
 */

// Constructor
DoubleLinkedList::DoubleLinkedList() {
    head = nullptr;
    tail = nullptr;
    count = 0;
}

// Destructor
DoubleLinkedList::~DoubleLinkedList() {
    Node* current = head;
    while (current != nullptr) {
        Node* next = current->next;
        delete current;
        current = next;
    }
}

// Insert a value into the linked list
void DoubleLinkedList::insert(int value) {
    Node* newNode = new Node{ value, nullptr, nullptr };

    if (!head) {
        head = newNode;
        tail = newNode;
    }
    else if (value <= head->data) {
        newNode->next = head;
        head->prev = newNode;
        head = newNode;
    }
    else if (value >= tail->data) {
        newNode->prev = tail;
        tail->next = newNode;
        tail = newNode;
    }
    else {
        Node* current = head;
        while (current->next != nullptr && current->next->data <= value) {
            current = current->next;
        }
        newNode->next = current->next;
        current->next->prev = newNode;
        current->next = newNode;
        newNode->prev = current;
    }

    count++;
}

// Merge another linked list into this one
void DoubleLinkedList::merge(DoubleLinkedList* absorbedList) {
    if (absorbedList == nullptr || absorbedList->head == nullptr) {
        return;
    }

    if (head == nullptr) {
        head = absorbedList->head;
        tail = absorbedList->tail;
    }
    else {
        tail->next = absorbedList->head;
        absorbedList->head->prev = tail;
        tail = absorbedList->tail;
        absorbedList->head->prev = tail; // Update prev pointer of absorbedList's head
    }

    count += absorbedList->count;

    absorbedList->head = nullptr;
    absorbedList->tail = nullptr;
    absorbedList->count = 0;
}

// Remove a value from the linked list
void DoubleLinkedList::remove(int value) {
    if (head == nullptr) {
        return; // List is empty
    }

    Node* current = head;

    while (current != nullptr) {
        if (current->data == value) {
            if (current == head) {
                head = current->next;
                if (head != nullptr) {
                    head->prev = nullptr;
                }
            }
            else if (current == tail) {
                tail = current->prev;
                tail->next = nullptr;
            }
            else {
                current->prev->next = current->next;
                if (current->next != nullptr) {
                    current->next->prev = current->prev;
                }
            }
            delete current;
            count--;
            return;
        }
        current = current->next;
    }
}

// Get the value at the given index
const int& DoubleLinkedList::operator[](int index) const {
    if (index < 0 || index >= count) {
        throw IndexOutOfBoundsException();
    }

    Node* current = head;
    for (int i = 0; i < index; i++) {
        current = current->next;
    }

    return current->data;
}

// Get the count of elements in the linked list
int DoubleLinkedList::getCount() const {
    return count;
}

// Display the linked list (reverse if specified)
void DoubleLinkedList::display(bool reverse) const {
    Node* current = reverse ? tail : head;
    while (current != nullptr) {
        std::cout << current->data << " ";
        current = reverse ? current->prev : current->next;
    }
    std::cout << std::endl;
}

