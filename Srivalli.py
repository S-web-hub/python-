import time

def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

def print_lyrics():
    lyrics = [
        "Nazre milte hi Nazron se nazorn ko churai",
        "kasi ia hai teri tu palko ko jhukai",
        "Rab jo pusida ha usko nihare tu,or jo garbida hain usko tale tu",
        "Teri Jhalak a sarfi Srivalli, Naina madak a barfi",
        "Teri Jhalak a sarfi Srivalli,Batain kare jo Harfi ",
        ]

    delays = [2.0, 1.8, 2.1, 2.4, 1.7, 2.0, 2.0, 1.7, 2.3]

    print("\n🎵 Now Playing - Srivalli ❤️\n")
    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

if __name__ == "__main__":
    print_lyrics()
    time.sleep(0.02)
