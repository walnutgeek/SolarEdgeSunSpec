
def dump_name(n):
    from os.path import join, dirname
    path = join(dirname(__file__), n)
    return path


def sample(n):
    return open(dump_name(n),'rb').read()


def dump(n,buff):
    import se_ss
    buff=bytearray(buff)
    se_ss.entries_by_name['C_SerialNumber'].replace(buff, b'F1234567')
    return open(dump_name(n), 'wb').write(buff)


def sanitize(n):
    dump(n, sample(n))


