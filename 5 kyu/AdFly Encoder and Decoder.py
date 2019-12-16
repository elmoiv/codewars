def adFly_decoder(sc):
    try:
        url = (sc[::2] + sc[::-2]).decode('base64').split('?u=')[1].decode('base64')
    except:
        return 'Invalid'
    return url

def adFly_encoder(url):
    f = ('11https://adf.ly/go.php?u=' + url.encode('base64')).encode('base64')[:-1]
    return ''.join(map(''.join, zip(f[:len(f) // 2], f[len(f) // 2:][::-1])))
