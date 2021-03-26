from chaining_hash_node import Chaining_Hash_Node

class Chaining_Hash_Set():

    def __init__(self, capacity = 0):
        self.hash_table = [None] * capacity
        self.table_size = 0
        self.array=[]
        self.lenght=capacity

    def get_hash_code(self, key, hash_table_length):
        """Hash function that calculates a hash code for a given key using the modulo division.
        @param key:
        		Key for which a hash code shall be calculated according to the length of the hash table.
        @param hash_table_length:
        		Length of the hash table.
        @return:
        		The calculated hash code for the given key.
        """
        has = key%hash_table_length
        return has



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

    def get_table_size(self):
        """returns the number of stored keys (keys must be unique!).
    	 """
        return self.table_size


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
            has = self.get_hash_code(key, self.lenght)
            if self.hash_table[has]==None:
                self.table_size+=1
                self.hash_table[has]= Chaining_Hash_Node(key,data)
            else:
                self.table_size+=1
                self.hash_table[has].next = Chaining_Hash_Node(key,data)
            return True
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
        has = self.get_hash_code(key,self.lenght)
        if key==None:
            raise ValueError
        if self.hash_table[has].key == key:
            return True
        done = self.hash_table[has].next
        while done != None:
            if done.key == key:
                return True
            done = self.hash_table[has].next
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
        has = self.get_hash_code(key,self.lenght)
        if self.hash_table[has].key == key:
            self.hash_table[has].key = None
            self.table_size = self.table_size -1
            return True
        done = self.hash_table[has].next
        while done != None:
            if done.key == key:
                done.key = None
                self.table_size = self.table_size -1
                return True
            done = self.hash_table[has].next
        return False

    def clear(self):
        """Removes all stored elements from the hash table by setting all nodes to None.
        """
        self.table_size = 0
        for i in range(0,self.lenght):
            #print(self.hash_table[i])
            self.hash_table[i]=None
        #return self.hash_table

