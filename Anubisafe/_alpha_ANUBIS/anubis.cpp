#include <iostream>
#include <omp.h>
#include <cstring>
#include "curve.hpp"
#include "anubis_arms.cpp"

#define _DEBUG true


using namespace std; 
int main(int argc, char* argv[]){
	
	unsigned long int key = 0;
      	string fname;
	bool _encrypt = false, _decrypt = false;
	opening();
	if (argc > 4)
		argumentHelper(argc, argv, key, _encrypt, _decrypt, fname);
	else if (argc < 4 && strcmp(argv[argc-1], "-h") == 0)
		documentation();

	return 0;
}


