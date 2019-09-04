unsigned int countBits(unsigned long long n){
    size_t count = 0;
    for (; n; n >>= 1) if ( n & 1 ) count++;
    return count;
}
