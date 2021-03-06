#!/usr/bin/env python

import sys


def main():
    with open(sys.argv[1], 'r') as fi:
        k = int(fi.readline())
        sequence = fi.readline().strip()

    for i in de_bruijn_graph(sequence, k - 1):
        print(i)


def de_bruijn_graph(sequence, k):
    kmers = set(gen_kmers(sequence, k))
    return overlap_graph(kmers)


def gen_kmers(sequence, k):
    for i in range(len(sequence) - k + 1):
        yield sequence[i: i + k]


def overlap_graph(kmers):
    prefix = {}
    for i in kmers:
        p = i[:-1]
        if p in prefix:
            prefix.get(p).append(i)
        else:
            prefix.update({p: [i]})

    for i in kmers:
        s = i[1:]
        if s in prefix:
            k = ','.join(prefix.get(s))
            yield '%s -> %s' % (i, k)


if __name__ == '__main__':
    main()
