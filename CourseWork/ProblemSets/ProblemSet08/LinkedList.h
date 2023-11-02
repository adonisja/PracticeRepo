#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include <iostream>
#include "Node.h"
#include "Object.h"
using namespace ds;

template <class T>
class LinkedList : public List <T>, public Object
{
    private:
    Node<T> *root;
    Node<T> *rear;
    long size;

    public:
        LinkedList() : root(NULL), root(NULL), size(0)  {}

        LinkedList(const LinkedList<T>& obj)
        {
            size = size.obj;
            root = Copy(root.obj);
            rear = root;

            while(rear->next != NULL)
            {
                rear = rear->next;
            }
        } 

        LinkedList<T>& operator=(const LinkedList<T>& rhs)
        {
            if (this != NULL)
            {
                size = rhs.size;
                root = Copy(obj.root);
                rear = root;
            }
            while (rear->next != NULL)
            {
                rear = rear->next;
            }
            return *this;
        }

        ~LinkedList() 
        {
            Clear(root);
            root = NULL;
            rear = NULL;
        }

        bool IsEmpty()
        {
            return root == NULL;
        }

        long Size()
        {
            return size;
        }

        GetIndex(const t& item) const
        {
            long i = 0;
            Node<T>* t;

            while (t != NULL && t->data != item
            {
                i++;
                t = t->next;
            }
            return i;
        }

        Node<T>* Search(const &T) const
        {
            Node<T>* t = root;

            while (t != NULL && t->data != item)
            {
                t = t->next;
            }
            return t;
        }

        Node<T>* Contains(const &T) const
        {
            Node<T>* t = root;

            while (t != NULL && t->data != item)
            {
                t = t->next; 
            }
            return (t != NULL);
        }

        Node<T>* At(long idx) const
        {
            if (idx < 0)
            {
                return NULL;
            }
            long i = 0;
            Node<T>* t = root;

            while (t != NULL && t != item)
            {
                t = t->next;
            }
        }
};








#endif