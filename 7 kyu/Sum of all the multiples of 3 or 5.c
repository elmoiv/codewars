int findSum(int n)
{
    int sum = 0;
    for (int i = 0; i <= n; i++) sum = (!(i % 3) || !(i % 5)) ? sum + i : sum ;
    return sum;
}
