#include <stddef.h>

size_t countBits(unsigned value)
{
    int sum = 0;
    for (unsigned i = 1 << 31; i > 0; i = i / 2)
    {
        if (value & i){sum++;}
    }
    return sum;
}
