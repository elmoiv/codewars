unsigned __int128 factorial(unsigned n)
{
    if (n < 2) return 1;
    return n * factorial(n - 1);
}
