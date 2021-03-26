#initializing the arrays
lfsr1=[0]*19
lfsr2=[0]*22
lfsr3=[0]*23
for i in range(0,18):
    lfsr1[i]=18-i
for i in range(0,21):
    lfsr2[i]=21-i
for i in range(0,22):
    lfsr3[i]=22-i

class Lfsr():

    
    def __init__(self):
        """default constructor"""

    def a5_rand(self):
        """Method "a5_rand" to calculate and return a random number according to the requested algorithm
        :return int
        """
        #saving the first values of the arrays
        r1p=lfsr1[0]
        r2p=lfsr2[0]
        r3p=lfsr3[0]
        
        r1=((lfsr1[0]^lfsr1[1])^lfsr1[2])^lfsr1[5] #calculating the random number for the first array
        for i in range(0,18):
            lfsr1[i]=lfsr1[i+1] #shifting
        lfsr1[18]=r1
        
        r2=lfsr2[0]^lfsr2[2] #calculating the random number for the second array
        for i in range(0,21):
            lfsr2[i]=lfsr2[i+1] #shifting
        lfsr2[21]=r2

        r3=((lfsr3[0]^lfsr3[1])^lfsr3[7])^lfsr3[15] #calculating the random number for the third array
        for i in range(0,22):
            lfsr3[i]=lfsr3[i+1] #shifting
        lfsr3[22]=r3

        return r1p^r2p^r3p
        
    def get_lfsr1(self):
        """Method "get_lfsr1" to return the content of the LFSR1 as an integer array
        :return int array
        """
        return lfsr1
        
        

        
        
        
    def get_lfsr2(self):
        """Method "get_lfsr2" to return the content of the LFSR2 as an integer array
        :return int array
        """
        return lfsr2

    def get_lfsr3(self):
        """Method "get_lfsr3" to return the content of the LFSR3 as an integer array
        :return int array
        """
        return lfsr3
