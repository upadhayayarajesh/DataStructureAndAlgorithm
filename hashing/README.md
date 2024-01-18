# HASHING

    Key value pair. Each key is unique

## Properties

### Advantages

    Search
    Insert       On average these three operations takes O(1) time complexity.
    Delete

### Disadvantages

    1. Finding closest value
    2. Sorted Data
    3. Prefix Searching

### Application of hashing

    1. Dictionaries
    2. Database Indexing
    3. Cryptography
    4. Caches
    5. Symbol Tables in compilers/ Interpreters
    6. Routers
    7. Getting data from databases

### Techniques of Hashing

#### Direct Address Table

    You used index of an array as a key in the hash table

#### Handling large number(phone number), String, floating point number as key

     Universal hashing function

#### Method to Handle Collision in the hash table

    1. Chaining
    2.Open Addresing
        1. Linear Probling
        2. Quadratic Probling
        3. Double Hashing

### Chaining

    Data structures for storing Chains
        1. Linked List => Search, Insert and delete takes O(l) time where l is length of Linked list  and also not cache friendly.
        2. Dynamic Sized Arrays (Array list)  => Search, Insert and delete takes O(l) time where l is length of Array list and also cache friendly.
        3. Self Balancing BST (AVL tree, Red Black Tree)  => Search, Insert and delete takes O(log(l)) time where l is length of tree but also not cache friendly.

    Performance of Chaining
        m = Number of slots in hash table.
        n = Number of keys to be inserted.
        Load factor (alpha) = n / m
        Expected chain Length = alpha
        Expected time to search = O(1 + alpha)
        Exected time to insert/delete = O(1 + alpha)