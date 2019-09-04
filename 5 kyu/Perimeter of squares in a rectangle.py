def perimeter(n):
    st = [0, 1]
    for i in range(n):
        st.append(sum(st[i:i + 2]))
    return 4 * sum(st)