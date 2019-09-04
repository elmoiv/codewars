def decodeMorse(morse_code):
    z = [i.split() for i in morse_code.split('   ') if i != '']
    return ''.join([''.join([MORSE_CODE[i] for i in z[sub]]) + ' ' * (sub != len(z) - 1) for sub in range(len(z))])
