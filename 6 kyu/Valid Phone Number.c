#include <stdbool.h>

bool valid_phone_number(const char* n) {
    if (n[0] + n[4] + n[5] + n[9] + strlen(n) == 172)
    {
        int c = 0;
        for (int i = 0; i < strlen(n); i++) c = (isdigit(n[i])) ? c + 1 : c;
        if (c == 10) return true;
    }
    return false;
}
