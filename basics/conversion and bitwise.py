# functions of decimal conversions  they expect a decimal value as parameter
bin()
oct()
hex()
#there is no functio to convert other values into decimal just type the value with their prifix to convert
x=0b11001       #binary to decimal
x=0o11001       #ocatal to decimal
x=0x11001       #hexa to decimal


#bitwise operator[they perform operations on binary code of your value]

    #1. complement = ~(tilde) it takes a tow complement on the given value
        x=~8  #the value of ~8 is -9
        x=~21   #the value of ~21 is -22

    #2. AND = & , OR = | ,NOT = !,XOR = ^

        a=7&10  #2      #0111 * 1010 =0010
        b=7|10  #15     #0111 + 1010 =1111
        c=7^10  #13     # 0 XOR 0 = 0, 0 XOR 1 = 1, 1 XOR 0 = 1, 1 XOR 1 = 0.so 0111 XOR 1010 = 1101



    #3. left shift = << and right shift = >>        (here the value at left is the value to be shifted and right is the no of shift)

        10 << 2 #it shifts the binary of 10 (2 steps left) binary of 10 =1010 if we shift them left it gives 101000 which is 40

        10 >> 2 #it shifts the binary if 10 (2 steps right) binary of 10=1010 if we shift them right i gives 0010 which is 2

