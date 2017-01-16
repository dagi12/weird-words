# -*- coding: utf-8 -*-


def open_polimorf():
    lines = [line.rstrip('\n') for line in open('pol-min.txt')]
    return lines


def open_corpus():
    with open('kor-min.txt', 'r') as f:
        lines = []
        for line in f:
            lines.extend(line.rstrip('\n').split(','))

    corpus = trim_corpus(lines)
    return corpus


def trim_corpus(corpus):
    new_corpus = []

    for cor_word in corpus:
        cor_word = cor_word.lstrip()
        new_corpus.append(cor_word)

    return new_corpus


def compare(pol, cor):
    not_in_corp = []
    in_corp = []

    with open('result.txt', 'a') as f:
        for word in pol:
            if word in cor:
                in_corp.append(word)
            else:
                print("Słowa z korpusu nie znajdujące się w polimorfie: ", word)
                not_in_corp.append(word)
                f.write(word + '\n')

    return not_in_corp


def save_to_file(item_list):
    with open('result.txt', 'a') as f:
        for item in item_list:
            word = item.encode('utf8') + '\n'
            f.write(word)


def main():
    polimorf = open_polimorf()
    corpus = open_corpus()
    compare(corpus, polimorf)


if __name__ == '__main__':
    main()
