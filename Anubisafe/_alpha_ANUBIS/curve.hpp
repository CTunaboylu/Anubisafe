#ifndef _HEAD_OF_ANUBIS
#define _HEAD_OF_ANUBIS

#include <omp.h>
typedef unsigned long long ullong;
/* 
#Why curves? : a 256-bit elliptic curve private key is as secure as a 3072-bit RSA private key
# curve anatomy :  y ** 2 = x ** 3 + ax +b AND 4a³+27b² ≠ 0 to avoid singular points.
# hashing the public key
#Caution! : Minimize if else statements -> vulnarability like RSA via Branch Prediction Attack - Intel does not handle it on its processors   
*/
class Curve {
// default curve of type secp256k1 : used in Bitcoin, Etherium y² mod p = (x³+7) mod p
// base point addition P+P+P ... 
// secp256k1 base point: 
// x = 55066263022277343669578718895168534326250603453777594175500187360389116729240
// y = 32670510020758816978083085130507043184471273380659243275938904335757337482424
// STEPS for a point x.P where x is a random 256-bit integer - let's call the result X 
// // -> Calculate 2⁰•P, 2¹•P, 2²•P, 2³•P, 2⁴•P, 2⁵•P, 2⁶•P, … , 2²⁵⁵•P with 255 point additions in total. 
// -> Then find the binary expansion of x. ( at most 256 elements ranging from  2⁰ to 2²⁵⁵ . Computation of the x.P will take at most 255 point additions. Till now at most 510 point additions will be performed. 	
// On average, x will be somewhere between 0 and 2²⁵⁶-1, about 2¹²⁸. Thus, for an attacker it will take on average 2¹²⁸ point addition operations to determine x no matter the approach ( adding P to itself until obtaining X or substracting P from X until obtaining P again). Another strategy: What if the attacker starts in the middle? He can calculate 2¹²⁸•P in 510 steps or less after all. On average, x is no closer to 2¹²⁸ than it is to 0 or 2²⁵⁶-1, because x is random, so it doesn’t matter where the attacker starts —he will still have to perform 2¹²⁸ point addition operations on average.
// Fun fact: Even if your computer could do one trillion point addition operations per second and you had been running your computer since the beginning of the universe, you would’ve only done 2⁹⁸ point addition operations by now. 2⁹⁸/2¹²⁸ =1/1073741824.
// So x : private key , X : public key
private:
// domain parameters 
int a, b, p;

/* Elliptic Curve functions
 *
 */
bool avoid_singularity(int&, int&) const;


};
#endif
