char *makeUpperCase (char *string)
{
    for (int i = 0; i < strlen(string); i++)
    {
       string[i] = isalpha(string[i]) ? string[i] - 32 : string[i];
    }
    return string;
}
