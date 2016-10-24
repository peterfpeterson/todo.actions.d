#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)

import datetime
import sys
from subprocess import Popen


def getTag(tag, text):
    if not tag in text:
        return ("", "")
    index = text.find(tag)
    full = text[index:].split()[0].strip()
    short = ':'.join(full.split(':')[1:])
    return (full, short)


def getNewDate(text, repeat, relative):
    if repeat == 0:
        return ("", "")

    today = datetime.date.today()

    # strip out the date from the task - if there is one
    tag = 't:'
    (fulldate, date) = getTag(tag, newtask)
    if len(fulldate) <= 0:  # try another tag
        tag = 'due:'
        (fulldate, date) = getTag(tag, newtask)

    # convert it into a date object
    if relative or len(date) <= 0:
        date = today
    else:
        date = [int(i) for i in date.split("-")]
        date = datetime.date(*date)

    # get the new date - first arg is days
    date += datetime.timedelta(repeat)

    # format things up
    return (fulldate, tag + str(date))


def execTodo(todo_full_sh, args):
    cmd = [todo_full_sh]
    cmd.extend(args)
    proc = Popen(cmd)
    result = proc.wait()
    if result:
        sys.exit(result)

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 4 and argc != 5:
        print("Usage: repeat ITEM DAYS")
        sys.exit(1)

    # get the configuration - wait on repeat
    todo_cmd = sys.argv[1]
    filename = sys.argv[2]
    item_num = int(sys.argv[3]) - 1  # python counts from zero

    # read in the tasks
    handle = file(filename, 'r')
    tasks = handle.readlines()
    handle.close()

    # make sure the task exists
    if len(tasks) < item_num:
        print("Not enough tasks in file '%s' (found %d)" % (filename, len(tasks)))
        sys.exit(1)

    # newtask starts out as the old one
    newtask = tasks[item_num].strip()

    # figure out the repeat parameter
    if argc == 5:
        repeat = sys.argv[4]
    else:
        (temp, repeat) = getTag("r:", newtask)
    relative = True
    if len(repeat) > 0:
        if repeat.startswith('+'):
            relative = False
            repeat = repeat[1:]
        repeat = int(repeat)
    else:
        repeat = 0

    # get the date and set it to new value
    (olddate, newdate) = getNewDate(newtask, repeat, relative)
    if len(olddate) > 0:
        newtask = newtask.replace(olddate, newdate)
    elif len(newdate) > 0:
        newtask = newtask + " " + newdate
    else:
        pass  # just renter the task

    # do the work
    execTodo(todo_cmd, ['do', str(item_num + 1)])
    execTodo(todo_cmd, ['add', newtask])
