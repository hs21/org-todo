#!/bin/python3
import Orgnode
import sys
import os

ORG_FILENAME=".org"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def print_priority(node, fd):
    if node.Priority() != "":
        print ("[#" + node.Priority() + "] ", end="", file=fd)

def print_todo(node):
    print_chars_lvl(node.level - 1, '  ', sys.stdout)
    if node.Todo() == "TODO":
        print(" " + bcolors.FAIL + "( TODO ) " + "[" + node.Priority() + "] " \
              + bcolors.ENDC + node.Heading().lstrip(), end="")
        if len(node.Body().lstrip().rstrip()) > 0:
            print(" (" + node.Body().lstrip().rstrip() + ")", end="")
        if len(str(node.Deadline()).lstrip().rstrip()) > 0:
            print(bcolors.OKBLUE + " :" + str(node.Deadline()).lstrip().rstrip() +
                  ":" + bcolors.ENDC, end="")
    else:
        print(" " + bcolors.OKGREEN + "( DONE ) " + bcolors.ENDC + \
              node.Heading().lstrip(), end="")
        if len(node.Body().lstrip().rstrip()) > 0:
            print(" (" + node.Body().lstrip().rstrip() + ")", end="")
    print("")

##
## Locate correct TODO file
##
def locate_todofile():
    return "%s/%s" % (os.getcwd(), ORG_FILENAME)
    ## Set global variable pointing to correct todofile

def print_chars_lvl(lvl, char, fd):
    while lvl > 0:
        print(char, end="", file=fd)
        lvl = lvl - 1

def export(nodelist, fd):
    for node in nodelist:
        print_chars_lvl(node.level, '*', fd)
        print(" " + node.Todo() + " ", end="", file=fd)
        print_priority(node, fd)
        print (" " + node.Heading(), file=fd)
        print_chars_lvl(node.level + 1, ' ', fd)
        print (node.Body(), file=fd)


def todo_init(todofile):
    if os.path.isfile(todofile):
        print("File exists")
    else:
        print("File does not exist")

def todo_list(nodelist):
    id = 1
    for node in nodelist:
        # print_chars_lvl(node.level - 1, '\t', sys.stdout)
        # print ("[" + str(id) + "] " + node.headline)
        print_todo(node)
        id = id + 1

def todo_add(nodelist):
    print("--")
    todo_list(nodelist)

    index = int(input('Index: '))
    headline = input('Headline: ')
    body = input('Body: ')
    level = input('Level: ')
    priority = input('Priority: ')
    todo = input('TODO: ')

    node = Orgnode.Orgnode(level, headline, body, '', '')
    node.todo = todo
    node.prty = priority


    nodelist.insert(int(index), node)
    todo_list(nodelist)

def todo_rem(nodelist):
    todo_list(nodelist)
    index = int(input('Index: '))
    nodelist.splice(index, 1)
##
## main()
##

orgfile = "./myorg.org"
if sys.argv[1] == "init":
    orgfile = "%s/%s" % (os.getcwd(), ORG_FILENAME)
    todo_init(orgfile)
    exit(0)

todofile = locate_todofile()
nodelist = Orgnode.makelist(todofile)

if sys.argv[1] == "list":
    todo_list(nodelist)
    exit(0)

if sys.argv[1] == "add":
    todo_add(nodelist)
elif sys.argv[1] == "rem":
    todo_rem(nodelist)
else:
    print(sys.argv[1] + ": Unsupported option.")
    exit(1)

fd = open(todofile, "w")
export(nodelist, fd)

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

