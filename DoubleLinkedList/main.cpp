#include "DoubleLinkedList.h"
#include <iostream>

/* 
 * This program demonstrates the usage of the DoubleLinkedList class by creating two lists,
 * inserting elements into them, merging one list into the other, and then displaying the merged list.
 */

int main() {
    // Create two instances of DoubleLinkedList
    DoubleLinkedList list1;
    list1.insert(5);
    list1.insert(10);
    list1.insert(15);

    DoubleLinkedList list2;
    list2.insert(3);
    list2.insert(6);
    list2.insert(9);

    // Merge list2 into list1
    list1.merge(&list2);

    // Display the merged list
    std::cout << "Merged list: ";
    list1.display();

    return 0;
}
