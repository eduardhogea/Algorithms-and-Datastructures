from open_hash_node import Open_Hash_Node

class Double_Hash_Set():

    def __init__(self, capacity = 0):
        self.hash_table = [None] * capacity
        self.table_size = 0
        self.lenght=capacity
        self.array = []
    def get_hash_table(self):
        """(Required for testing only)
        @return the hash table.
        """
        return self.hash_table

    def set_hash_table(self, table, size):
        """(Required for testing only) Set a given hash table which shall be used.
        @param table:
        		Given hash table which shall be used.
        @param size:
        		Number of already stored keys in the given table.
        """
        self.hash_table = table
        self.table_size = size
        self.lenght = len(self.hash_table)

    def get_table_size(self):
        """returns the number of stored keys (keys must be unique!).
    	 """
        return self.table_size

    def get_hash_code_2(self, key, hash_table_length):
        """Hash function 2 for double hashing, that calculates a key specific offset.
        @param key:
        		Key for which a hash code shall be calculated according to the length of the hash table.
        @param hash_table_length:
        		Length of the hash table.
        @return:
        		The calculated hash code for the given key.
        """
        h1=key%hash_table_length
        h2=0
        if hash_table_length-1!=0:
            h2=1+(key%(hash_table_length-1))
        #h3=(h1+h2)%hash_table_length
        return h2

    def insert(self, key, data):
        """Inserts a key and returns true if it was successful. If there is already an entry with the
          same key or the hash table is full, the new key will not be inserted and false is returned.

         @param key:
         		The key which shall be stored in the hash table.
         @param data:
         		Any data object that shall be stored together with a key in the hash table.
         @return:
         		true if key could be inserted, or false if the key is already in the hash table.
         @throws:
         		a ValueError exception if any of the input parameters is None.
         """
        if key == None or data == None:
            raise ValueError
        if key not in self.array:
            self.array.append(key)
            h1 = key % self.lenght
            h2 = self.get_hash_code_2(key, self.lenght)
            h3 = (h1 + h2) % self.lenght
            if self.hash_table[h1]==None:
                self.table_size += 1
                self.hash_table[h1]=Open_Hash_Node(key,data)
                return True
            elif self.hash_table[h2]==None:
                self.table_size += 1
                self.hash_table[h2] = Open_Hash_Node(key, data)
                return True
            else:
                while h3 != 0:  
                    if self.hash_table[h3] == None:
                        self.table_size += 1
                        self.hash_table[h3] = Open_Hash_Node(key, data)
                        return True
                    h3 = (h3 + h2) % self.lenght
        else:
            return False

    def contains(self, key):
        """Searches for a given key in the hash table.
         @param key:
         	    The key to be searched in the hash table.
         @return:
         	    true if the key is already stored, otherwise false.
         @throws:
         	    a ValueError exception if the key is None.
         """

        if key == None:
            raise ValueError
        for i in range(0,self.lenght):
            if self.hash_table[i]!=None:
                if self.hash_table[i].key==key:
                    return True
        return False

    def remove(self, key):
        """Removes the key from the hash table and returns true on success, false otherwise.
        @param key:
        		The key to be removed from the hash table.
        @return:
        		true if the key was found and removed, false otherwise.
        @throws:
         	a ValueError exception if the key is None.
        """
        if key==None:
            raise ValueError
        h1 = key % self.lenght
        h2 = self.get_hash_code_2(key, self.lenght)
        h3 = (h1 + h2) % self.lenght
        if self.hash_table[h1].key == key:
            self.hash_table[h1].key = None
            self.table_size = self.table_size -1
            return True
        if self.hash_table[h2].key == key:
            self.hash_table[h2].key = None
            self.table_size = self.table_size -1
            return True
        while h3!=0: #loop?
            if self.hash_table[h3].key == key:
                self.hash_table[h3].key = None
                self.table_size = self.table_size - 1
                return True
            h3=(h3+h2)%self.lenght
        return False


    def clear(self):
        """Removes all stored elements from the hash table by setting all nodes to None.
        """
        self.table_size = 0
        for i in range(0, self.lenght):
            # print(self.hash_table[i])
            self.hash_table[i] = None
        # return self.hash_table
