#include <cstdlib>
#include <unistd.h>

int main(int argc, const char* argv[])
{
    setuid(0);
    system("systemctl hibernate");
    return 0;
}
