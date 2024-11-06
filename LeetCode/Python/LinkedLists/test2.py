def test_a(n):
    print(f'({n})')
    if n > 0:
        test_a(n-2)

def main():
    test_a(4)

if __name__ == '__main__':
    main()