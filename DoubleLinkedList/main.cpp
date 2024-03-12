#include "DoubleLinkedList.h"
#include <iostream>

DoubleLinkedList::DoubleLinkedList() {
    head = nullptr;
    tail = nullptr;
    count = 0;
}

DoubleLinkedList::~DoubleLinkedList() {
    Node* current = head;
    while (current != nullptr) {
        Node* next = current->next;
        delete current;
        current = next;
    }
}

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
    }

    count += absorbedList->count;

    absorbedList->head = nullptr;
    absorbedList->tail = nullptr;
    absorbedList->count = 0;
}

void DoubleLinkedList::remove(int value) {
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
                current->next->prev = current->prev;
            }
            delete current;
            count--;
            return;
        }
        current = current->next;
    }
}

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

int DoubleLinkedList::getCount() const {
    return count;
}

void DoubleLinkedList::display(bool reverse) const {
    Node* current = reverse ? tail : head;
    while (current != nullptr) {
        std::cout << current->data << " ";
        current = reverse ? current->prev : current->next;
    }
    std::cout << std::endl;
}
