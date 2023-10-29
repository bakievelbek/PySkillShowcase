"""

---

### Hash Table Explanation

**Concept**: A hash table is used to store key-value pairs. The main idea behind a hash table is to use a hash function
to convert a key into an index of an array (or a "bucket"). By doing this, we can quickly locate the value associated
with a given key.

**Components**:
1. **Keys**: These are unique identifiers for the data you wish to store.
2. **Values**: The data you wish to store, associated with a key.
3. **Hash Function**: Converts the key into an array index.
4. **Buckets/Slots**: The array positions where data gets stored.

**Steps**:
1. **Insertion**:
    - Take a key and pass it through the hash function.
    - The hash function provides an index for where to store the associated value in the array/bucket.

2. **Retrieval**:
    - Again, pass the key through the hash function to get the array index.
    - Access the array at that index to get the associated value.

3. **Collision Resolution**: Sometimes, two keys might hash to the same index. This is called a collision. There are
 several strategies to handle collisions:
    - **Chaining**: Store a linked list at each array position. If a collision occurs, just add the key-value pair to
    the end of the list.
    - **Open Addressing**: If a collision occurs, find the next open slot in the array to store the value.

**Advantages**:
- Allows for average-case constant-time O(1) insertions, deletions, and retrievals.

**Limitations**:
- Poor choice of hash function or table size can lead to many collisions, making operations slower.
- They don't maintain any order of the key-value pairs.

---

"""


class HashTable:
    def __init__(self, size=10):
        self.size = size
        # Initialize empty buckets
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """Compute an index in the range [0, size - 1]"""
        hash_ = hash(key) % self.size
        return hash_

    def set(self, key, value):
        """Insert or update the key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Key found, update its value
                bucket[i] = (key, value)
                return
        # Key not found, append to the bucket
        bucket.append((key, value))

    def get(self, key):
        """Retrieve the value associated with the key"""
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        """Remove the key and its associated value"""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
        raise KeyError(f"Key {key} not found")

    def __str__(self):
        """String representation of the hash table"""
        return str(self.table)


# Example Usage:
ht = HashTable()

# Insert key-value pairs
ht.set("name", "John")
ht.set("age", 25)
ht.set("city", "New York")

print(ht)  # Prints the current hash table

# Retrieve values
print(ht.get("name"))  # Expected: John

# Update a key-value pair
ht.set("name", "Mike")
print(ht.get("name"))  # Expected: Mike

# Remove a key
ht.remove("city")
print(ht)  # city key-value pair should be gone
