#!/bin/python3
import Orgnode
import os

##
## Locate correct TODO file
##
def locate_todofile():
    print (os.getcwd())
    ## Set global variable pointing to correct todofile

def print_chars_lvl(lvl, char):
    while lvl > 0:
        print(char, end="")
        lvl = lvl - 1

def dump(nodelist):
    id = 1
    for node in nodelist:
        print_chars_lvl(node.level - 1, '\t')
        print ("[" + str(id) + "] " + node.Heading())
        id = id + 1

def export(nodelist):
    for node in nodelist:
        print_chars_lvl(node.level, '*')
        print (" " + "[" + node.Priority() + "] " + node.Todo() + " " + node.Heading())
        print (node.Body())

##
## main()
##
todofile = locate_todofile()

##
## Parse commandline args and call appropriate functions
## todo_init()
#### create .org file in PWD
## todo_add()
#### Add a new TODO item, take location marker as input
## todo_rem()
#### Remove a TODO item, take location marker as input
#### Remove all todos nested
## todo_list()
#### List all TODOs. By default, only display headings.
#### If an argument asks to display body too, then do it!
## todo_grep()
#### Search. display matching items.
##

orgfile = "./myorg.org"
nodelist = Orgnode.makelist(orgfile)

dump(nodelist)
export(nodelist)
node1 = Orgnode.Orgnode("*","Item99","Item99-Body","","")

