#ifndef DOUBLELINKEDLIST_H
#define DOUBLELINKEDLIST_H

class DoubleLinkedList {
private:
    struct Node {
        int data;
        Node* next;
        Node* prev;
    };

    Node* head;
    Node* tail;
    int count;

public:
    DoubleLinkedList();
    ~DoubleLinkedList();
    void insert(int value);
    void merge(DoubleLinkedList* absorbedList);
    void remove(int value);
    const int& operator[](int index) const;
    int getCount() const;
    void display(bool reverse = false) const;
};

class IndexOutOfBoundsException {};

#endif
