# this file for help user Tool
from core.color import colorize

def help():
    
    print(f"""
    {colorize.RED}clear{colorize.WHITE}: clear all commands in terminal
    {colorize.RED}whoami{colorize.WHITE}: whoami :)
    {colorize.RED}banner{colorize.WHITE}: print banner ..
    {colorize.RED}help{colorize.WHITE}: print this list
    {colorize.RED}exit{colorize.WHITE}: exit from ENCRYPted
    {colorize.RED}all{colorize.WHITE}: test on all this list
    {colorize.RED}md5{colorize.WHITE}: hash md5
    {colorize.RED}sha1{colorize.WHITE}: hash sha1
    {colorize.RED}sha256{colorize.WHITE}: hash sha256
    {colorize.RED}sha512{colorize.WHITE}: hash sha512
    {colorize.RED}sha224{colorize.WHITE}: hash sha224
    {colorize.RED}sha384{colorize.WHITE}: hash sha384
    {colorize.RED}sha3_512{colorize.WHITE}: hash sha3_512
    {colorize.RED}sha3_384{colorize.WHITE}: hash sha3_384
    """)       