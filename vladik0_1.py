from multiprocessing import Process
from RandomWordGenerator import RandomWord
import multiprocessing
import random
from typing import List
import os 

def chponk_tatar():
    file_name = str(os.getpid()) + '.txt'
    bornana(file_name)
    yaclichko(file_name)

def bornana(file_name):
    rw = RandomWord(constant_word_size = False)
    with open(file_name, 'w+') as file:
        a = random.randint(100, 5000)
        for i in range(a):
            file.write(rw.generate() + '\n')

def yaclichko(file_name):
    with open(file_name, 'r') as file:
        a, b, c, d = logic(file)
         
        print_info(file_name, a, b, c, d)


def print_info(file_name, a, b, c, d):
    res = f"""
File: {file_name}
Symbols: {a}
Biggest word: {b}
Smallest word: {c}
Average word: {a // d}
"""
    print(res)

def prikol(line):
    line.strip()
    return len(line)


def vova(line):
    maxim = 0
    massive_cock = line.split('\n')
    for word in massive_cock:
        if (len(word) > maxim):
            maxim = len(word)
    return maxim

def min_vova(line):
    minin = 10
    massive_cock = line.split('\n')
    for word in massive_cock:
        if (len(word) < minin):
            minin = len(word)
    return minin

def word_count(line):
    word_in_line = line.split('\n')
    return len(word_in_line)
    

def logic(file):
    count_sym = 0
    supra = 0
    lil = 10
    boobs = 0
    boobs2 = 1
    word_cou = 0
    for line in file:
        count_sym += prikol(line)
        boobs = vova(line)
        if boobs > supra:
            supra = boobs
            boobs = 0
        boobs = min_vova(line)
        if boobs < lil:
            lil = boobs2
            boobs2 = 1
        word_cou += word_count(line)
    
    
    return count_sym, supra, lil, word_cou
            

if __name__ == '__main__':
    list_pr :List[Process] = []
    cpu_cht = multiprocessing.cpu_count() // 2
    for i in range(cpu_cht):
        proc = Process(target=chponk_tatar)
        list_pr.append(proc)
        list_pr[i].start()

    for i in range(cpu_cht):
        list_pr[i].join()


    
