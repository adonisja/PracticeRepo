// Path: Practice/Heap.cpp

public class MinIntHeap{
    private int capacity = 10;
    private int size = 0;

    int [] items = int new[capacity];

    private int getLeftChildIndex(int parentIndex) { return 2 * parentIndex + 1;} // gets the left child index
    private int getRightChildIndex(int parentIndex) { return 2 * parentIndex + 2;} //  gets the right child index
    private int getParentIndex(int childIndex) { return (childIndex - 1) / 2;} // gets the parent index

    private boolean hasLeftChild(int index) { return getLeftChildIndex(index) < size;} // checks if the left child exists
    private boolean hasRightChild(int index) { return getRightChildIndex(index) < size;} // checks if the right child exists
    private boolean hasParent(int index) { return getParentIndex(index) >= 0;} // checks if the parent exists

    private int leftChild(int index) { return items[getLeftChildIndex(index)];} // gets the left child
    private int rightChild(int index) { return items[getRightChildIndex(index)];} // gets the right child
    private int parent(int index) { return items[getParentIndex(index)];} // gets the parent

    private void swap(int indexOne, int indexTwo) // swaps two elements
    {
        int temp = items[indexOne]; // stores the first element in a temporary variable
        items[indexOne] = items[indexTwo]; // sets the first element to the second element
        items[indexTwo] = temp; //  sets the second element to the temporary variable
    }

    private void ensureExtraCapacity() // ensures that there is enough space in the array
    {
        if(size == capacity) // if the size of the array is equal to the capacity
        {
            items = Arrays.copyOf(items, capacity * 2); // double the size of the array
            capacity *= 2;
        }
    }

    public int peek() // returns the root element
    {
        if(size == 0) throw new IllegalStateException(); // if the size of the array is 0, throw an exception
        int item = intems[0]; // store the root element in a variable
        items[0] = items[size - 1]; // set the root element to the last element in the array
        size--;                 // decrement the size of the array
        heapifyDown();          // move the element down the heap
        return items[0];        // return the root element
    }

    public void add(int item) // adds an element to the heap
    {
        ensureExtraCapacity();   // ensure that there is enough space in the array
        items[size] = item;     // add the element to the array
        size++;                 // increment the size of the array
        heapifyUp();           // move the element up the heap
    }

    public void heapifyUp() // moves the element up the heap
    {
        int index = size - 1;    // set the index to the last element in the array
        while(hasParent(index) && parent(index) > items[index]) // while the parent exists and the parent is greater than the element
        {
            swap(getParentIndex(index), index);     // swap the parent and the element
            index = getParentIndex(index);         // set the index to the parent
        }
    }

    public void heapifyDown() // moves the element down the heap
    {
        int index = 0;  // set the index to the root element
        while(hasLeftChild(index)) // while the left child exists
        {
            int smallerChildIndex = getLeftChildIndex(index);   // set the smaller child index to the left child index
            if(hasRightChild(index) && rightChild(index) < leftChild(index))    // if the right child exists and the right child is less than the left child
            {
                smallerChildIndex = getRightChildIndex(index);     // set the smaller child index to the right child index     
            }

            if(items[index] < items[smallerChildIndex])  // if the element is less than the smaller child
            {
                break;
            }
            else
            {
                swap(index, smallerChildIndex);   // swap the element and the smaller child
            }
            index = smallerChildIndex;  // set the index to the smaller child
        }
    }
}

