def move_ten(st):
    st.replace('z', '@')
    s = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'klmnopqrstuvwxyzabcdefghij')
    st = st.translate(s)
    return st.replace('@','a')
