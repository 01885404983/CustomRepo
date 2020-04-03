#include <string>
#include <cstdlib>
#include <unistd.h>

int main(int argc, const char* argv[])
{
    std::string command = "python /usr/bin/blight.py ";
    for (int i = 1; i < argc; ++i) {
        command += argv[i];
        command += " ";
    }
    setuid(0);
    system(command.c_str());
    return 0;
}