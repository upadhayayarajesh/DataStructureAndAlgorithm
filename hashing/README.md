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
        1. Linear Probling  => Linearly search for next empty slot when there is collision
        2. Quadratic Probling => Quadraticly search for next empty slot when collision
        3. Double Hashing => Do hashing until you find the next empty slot when collision

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

### Open Addressing

    1. Linear Probling
    Requirement
        Number of slots in Hash Table >= Number of keys to be inserted.
    Advantage
        Cache Frienly
    Disadvantages
        Insert and Search may take O(N) time i.e. it forms a cluster
            In order to solve it uses Quadratic probing.
            There are other problem with quadratic probling like failed to find the 
            Empty slot even there are empty slot present in the table, another issue 
            Secondary cluster is formed in the hashing.
            so, Double hashing is another approach to solve them
    2. Double Hashing
        Define the hasing function such a way you add a offset to it and then, it return other slot
        If slot empty inset it other wise again do hasing untill you find the next empty slot.

### Comparing Open Addressing and Chaining

| S.N. | Chaining                        | Open Addressing                                                              |
|------|---------------------------------|------------------------------------------------------------------------------|
| 1.   | Hash Table never Fills          | Table may become full and resizing becomes mandatory                         |
| 2.   | Less sensitive to Hash Function | Extra case required for clustering                                           |
| 3.   | Poor Cache Performance          | Cache Friendly                                                               |
| 4.   | Extra space for links           | Extra space might be needed to achieve <br/> same performance as of chaining |

