# Librarys
import os
from hashlib import *
from typing import KeysView
from core.commands import *
from modules.hash import Hash
from core.banner import banner
from core.color import colorize
from core.help_user import help
from core.clear import clear
from tabulate import tabulate

# use os system
# for clear terminal
os.system('clear')

# banner
banner()

# Loop while
while True:
    try:
        # Input 
        cmd = input(f"{colorize.RED}Cryptic >>{colorize.WHITE} ")

        # COMMANDS
        if cmd.split()[0] == "clear":
            os.system('clear')
        
        elif cmd.split()[0] == "whoami":
            print(f"[{colorize.RED}+{colorize.WHITE}] made by glitch")

        elif cmd.split()[0] == "banner":
            banner()

        elif cmd.split()[0] == "help":
            help()

        elif cmd.split()[0] == "exit":
            exit()

        # hash

        # MD5
        elif cmd.split()[0] == "md5":
            try:
                hash_md5 = cmd.split()[1]
                Hash = Hash(hash_md5)
                Hash.getWord()
                print(f"[{colorize.RED}~{colorize.WHITE}] MD5: {Hash.md5}")
                break
            except:
                print(f"{colorize.RED}using:{colorize.WHITE} md5 <your words>")
                print(f"{colorize.RED}Example:{colorize.WHITE} md5 Hello")

        
        # Sha1
        elif cmd.split()[0] == "sha1":
            try:
                hash_sha1 = cmd.split()[1]
                Hash = Hash(hash_sha1)
                Hash.getWord()
                print(f"[{colorize.RED}~{colorize.WHITE}] Sha1: {Hash.sha1}")
                break
            except:
                print(f"{colorize.RED}using:{colorize.WHITE} sha1 <your words>")
                print(f"{colorize.RED}using:{colorize.WHITE} sha1 Hello")

        # Sha256
        elif cmd.split()[0] == "sha256":
            try:
                hash_sha256 = cmd.split()[1]
                Hash = Hash(hash_sha256)
                Hash.getWord()
                print(f"[{colorize.RED}~{colorize.WHITE}] Sha256: {Hash.sha256}")
                break
            except:
                print(f"{colorize.RED}using:{colorize.WHITE} sha256 <your words>")
                print(f"{colorize.RED}using:{colorize.WHITE} sha256 Hello")

        # Sha512
        elif cmd.split()[0] == "sha512":
            try:
                hash_sha512 = cmd.split()[1]
                Hash = Hash(hash_sha512)
                Hash.getWord()
                print(f"[{colorize.RED}~{colorize.WHITE}] Sha512: {Hash.sha512}")
                break
            except:
                print(f"{colorize.RED}using:{colorize.WHITE} sha512 <your words>")
                print(f"{colorize.RED}using:{colorize.WHITE} sha512 Hello")

        # Sha224
        elif cmd.split()[0] == "sha224":
            try:
                hash_sha224 = cmd.split()[1]
                Hash = Hash(hash_sha224)
                Hash.getWord()
                print(f"[{colorize.RED}~{colorize.WHITE}] Sha224: {Hash.sha224}")
                break
            except:
                print(f"{colorize.RED}using:{colorize.WHITE} sha224 <your words>")
                print(f"{colorize.RED}using:{colorize.WHITE} sha224 Hello")


        # Sha384
        elif cmd.split()[0] == "sha384":
            hash_sha384 = cmd.split()[1]
            Hash = Hash(hash_sha384)
            Hash.getWord()
            print(f"[{colorize.RED}~{colorize.WHITE}] Sha384: {Hash.sha384}")
            break

        # Sha3_512
        elif cmd.split()[0] == "sha3_512":
            try:
                hash_sha3_512 = cmd.split()[1]
                Hash = Hash(hash_sha3_512)
                Hash.getWord()
                print(f"[{colorize.RED}~{colorize.WHITE}] Sha3_512: {Hash.sha3_512}")
                break
            except:
                print(f"{colorize.RED}using:{colorize.WHITE} sha3_512 <your words>")
                print(f"{colorize.RED}using:{colorize.WHITE} sha3_512 Hello")

        # Sha3_384
        elif cmd.split()[0] == "sha3_384":
            try:
                hash_sha3_384 = cmd.split()[1]
                Hash = Hash(hash_sha3_384)
                Hash.getWord()
                print(f"[{colorize.RED}~{colorize.WHITE}] Sha3_384: {Hash.sha3_384}")
                break
            except:
                print(f"{colorize.RED}using:{colorize.WHITE} sha3_384 <your words>")
                print(f"{colorize.RED}using:{colorize.WHITE} sha3_384 Hello")

        # all Hash
        elif cmd.split()[0] == "all":
            try:
                hash_all = cmd.split()[1]
                Hash = Hash(hash_all)
                Hash.Tabules()
                print(tabulate(Hash.Data, tablefmt="fancy_grid"))
                break
            except:
                print(f"{colorize.RED}using:{colorize.WHITE} all <your words>")
                print(f"{colorize.RED}using:{colorize.WHITE} all Hello")

        if cmd.split()[0] not in commands:
            print(f"please use {colorize.RED}help{colorize.WHITE} command :)")
    except KeyboardInterrupt:
        print("you have some error")
