def compare(a, b):
    if len(a) > len(b) or len(a) == len(b):
        if a.count(b) > 0:
            start_idx = a.index(b)
            end_idx = start_idx + len(b)
            hasil = a[start_idx : end_idx]
    elif len(a) < len(b):
        if (b.count(a)) > 0:
            start_idx = b.index(a)
            end_idx = start_idx + len(a)
            hasil = b[start_idx : end_idx]
    return hasil

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA