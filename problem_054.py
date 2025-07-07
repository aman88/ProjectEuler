# Date: 2025.07.06
# Answer: 

def process_file(file):
    with open(file) as data:
        lines = data.read().splitlines()
        for line in lines:
            cards = line.split(" ")
            hand1 = cards[:len(cards)//2]
            hand2 = cards[len(cards)//2:]
            print(hand1,hand2)
            return

    #     for cnt, line in enumerate(data):
    #         list_from_file=line.split(" ")
    # print(list_from_file)


if __name__ == "__main__":
    process_file("data/0054_poker.txt")