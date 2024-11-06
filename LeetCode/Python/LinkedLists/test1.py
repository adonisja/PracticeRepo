def quiz(i):
    if i > 2:
        quiz(i/2)
        quiz(i/2)
    print(f'i = {i}')

def main():
    quiz(5)

if __name__ == '__main__':
    main()