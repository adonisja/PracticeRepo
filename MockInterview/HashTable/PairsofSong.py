def songPair(time):
    map = {}
    pairs = 0
    for num in time:
        mod = num % 60
        complement = (60 - mod) % 60  # Calculate the complement
        if complement in map:
            pairs += map[complement]
        if mod in map:
            map[mod] += 1
        else:
            map[mod] = 1
    return pairs

def main():
    time = [30, 20, 150, 100, 40]
    print(songPair(time))

if __name__ == '__main__':
    main()