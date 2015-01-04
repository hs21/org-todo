#!/bin/python3
import Orgnode
import sys
import os

##
## Locate correct TODO file
##
def locate_todofile():
    return "%s/.org" % os.getcwd()
    ## Set global variable pointing to correct todofile

def print_chars_lvl(lvl, char):
    while lvl > 0:
        print(char, end="")
        lvl = lvl - 1

def export(nodelist):
    for node in nodelist:
        print_chars_lvl(node.level, '*')
        print (" " + "[" + node.Priority() + "] " + node.Todo() + " " + node.Heading())
        print (node.Body())


def todo_init(todofile):
    if os.path.isfile(todofile):
        print("File exists")
    else:
        print("File does not exist")

def todo_list(nodelist):
    id = 1
    for node in nodelist:
        print_chars_lvl(node.level - 1, '\t')
        print ("[" + str(id) + "] " + node.Heading())
        id = id + 1

def todo_add(nodelist):
    print("--")
    todo_list(nodelist)

    #    node.Heading= input('Nest_under: ')
    # index = input('Index: ')
    # headline = input('Headline: ')
    # body = input('Body: ')
    # level = input('Level: ')

    index = 6
    headline = "hello"
    body = "world"
    level = "**"
    priority = "A"
    todo = "TODO"

    node = Orgnode.Orgnode(level, headline, body, '', '')
    node.todo = todo
    node.prty = priority

    nodelist.insert(int(index), node)
    todo_list(nodelist)
    export(nodelist)
##
## main()
##

orgfile = "./myorg.org"
if sys.argv[1] == "init":
    orgfile = "%s/.org" % os.getcwd()
    todo_init(orgfile)
    exit(0)

todofile = locate_todofile()
nodelist = Orgnode.makelist(orgfile)

if sys.argv[1] == "list":
    todo_list(nodelist)
if sys.argv[1] == "add":
    todo_add(nodelist)
else:
    print(sys.argv[1] + ": Unsupported option.")

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


# dump(nodelist)
# export(nodelist)
# node1 = Orgnode.Orgnode("*","Item99","Item99-Body","","")

