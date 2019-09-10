#ifndef _ANUBIS_ARMS
#define _ANUBIS_ARMS
#include <iostream>
#include <omp.h>
#include <cstring>

using namespace std; 
// elongate the key with key + hash(key) - salting 
// Find primes efficiently 
// Scramble the default key and use the pathway as a key too. 8 digits = 73642851 for ex : the places that the nth digit will be put. The first character will determine the salting => put the salt in that place <first-part>+salt+<second-part>
// Add search the file component 
// Add local passwords - encrypted for default mode	


// Get the OS 
// __APPLE__ && __MACH__ for MacOS 
// __unix__ || __unix
// _WIN16 || _WIN32 || _WIN64 || __WIN32__ || __TOS_WIN__ || __WINDOWS__ 

// Add the MAC address to the decrypted file to know who tried to open it 
void opening(){
cout<<"----------------------------------------------------------------------------------------------------------------------------------------------------------------------"<<endl;
cout<<"-----------------------------------------------------------------------ANUBIS-----------------------------------------------------------------------------------------"<<endl;
cout<<"----------------------------------------------------------------------------------------------------------------------------------------------------------------------"<<endl;
}
void documentation(){
	opening();
	cout<<"If a key is not provided while encrypting and decrypting, Anubis will work in local mode by default. In this case, every encryption is local computer specific, only the used computer can decrypt the files.For this option the default syntax is as follows:"<<endl;
        cout<<"-f <filepath/filename>  : if in the same directory, no need to specify the path."<<endl;
	cout<<"-d <key> <filename> : to decrypt the file with the key\n";
	cout<<"-e <key> <filename> to encrypt the file with the given key. In this case Anubis will provide you with 2 extra integers which you have to keep secret, you will only need to enter them manually while decrypting if you are not using the default computer that you have used to encrypt the file in first place.\n";
	cout<<"-dl : use this while encrypting if you don't want the local computer privileges. In this case you will have to enter 2 keys that Anubis provided you with your own key to decrypt the  file regardless of the computer being used."<<endl;
	cout<<" -ec : elliptic curve "<<endl;
	cout<<"-h : to get help \n";
	cout<<"-local : If you add this to -e option, the file can only be decrpyted in the local machine that is been used to encrypt the file \n";
	cout <<"-who : to see who have been attempted/succeeded to decrypt the file"<<endl;
	cout<<" For security, if attempted to decrypt the file 3 times in a row with inappropriate conditions according to the encryption standarts, the file will be digested irreversibly to protect the content."<<endl;

	return;
}
void wrongCmdCombination(){
	cout <<"Wrong command combination..."<<endl;
       	documentation();
	return;
}
void argumentHelper(int argc, char** argv,unsigned long int &k, bool &e, bool &d, string &fname){
	for(int i=0; i<argc; i++)
		if(strcmp(argv[i], "-k") == 0) k = (unsigned long int)*argv[++i];
		else if (strcmp(argv[i], "-e") == 0) e = true;
		else if (strcmp(argv[i], "-d")== 0) d = true;
		else if (strcmp(argv[i], "-f") == 0) fname = *argv[++i];
	if(e && d) 
		wrongCmdCombination();
	
	return;
}
#endif
