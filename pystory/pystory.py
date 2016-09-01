# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""Pystory 

Note: Not all commands are implemented yet.

Example usage:

    DEFAULT:

    $ pystory
        - prints history as if it's normal history (cmd_num, cmd)

    FLAGS:

        -v --verbose
           include dates, path of execution, etc.

    COMMANDS

        IMPLEMENTED

        $ pystory 50
            print 50 last entries, compressed
        
        $ pystory find <term>
            show all entries matching the term (<term> in cmd)

        NOT IMPLEMENTED

        $ pystory all
            print all entries uncompressed

        $ pystory clean
            remove strange entries in .pystory file, with "Are you sure? y/n prompt"

        $ pystory remove
            empty the .pystory file

        $ pystory rank
            show ranked list of most used commands - from low to high

        $ pystory rank r/reversed
            show ranked list of commands - high to low

        $ pystory rank 10
            show 10 most used commands
"""
import argparse
import os
import sys
import warnings

from collections import Counter, defaultdict, OrderedDict


ALLOWED_COMMANDS = ('find', 'last', 'clean', 'all', 'remove')
REQUIRES_PARAMS = ('find', 'last')


def is_int(var):
    try:
        int(var)
        return True
    except ValueError:
        return False


def parse_pystory():
    env_path = get_env_path()
    pystory_filename = os.path.join(env_path, '.pystory')
    pysts = []
    with open(pystory_filename) as fh:
        for line in fh:
            splits = line.split()
            if len(splits) <= 3:
                continue

            (time, path, cmd_num, *cmd) = splits
            cmd = " ".join(cmd)
            pysts.append((time, path, cmd_num, cmd))

    return pysts


def compress_pysts(pysts, reverse=False):
    """ Returns list of commands with counts, only last entry.

    Sort on history
    """

    count = defaultdict(int)
    last_entry = OrderedDict()

    for pyst in reversed(pysts):
        cmd = pyst[3]
        count[cmd] += 1
        if cmd not in last_entry:
            last_entry[cmd] = pyst  

    return last_entry, count


def print_info(skip=False, compressed=True):
    if not skip:
        print("Showing compressed history of your actions (see full history with `pystory all`)")            
        print("\nRun command by typing `!num` where num is the number in Hist column")

    if compressed:
        columns = ['Hist', 'Count', 'Command']
    else:
        columns = ['Hist', 'Command']
    
    print("\t".join(columns))


def print_compressed_pystory(pysts):

    last_entry, count = compress_pysts(pysts)

    print_info(skip=True)

    for cmd, pyst in reversed(last_entry.items()):
        count_str = "{0}.".format(count[cmd])
        line = [pyst[2], count_str, pyst[3]]
        print("\t".join(line))


def get_env_path():

    env_path = os.getenv('VIRTUAL_ENV', None)
    prompt_command = os.getenv('PROMPT_COMMAND', None)
    disable_pystory = os.getenv('DISABLE_PYSTORY', None)

    if disable_pystory:
        sys.exit(0)

    if not env_path:
        sys.exit(0)

    if not prompt_command:
        warnings.warn("PROMPT_COMMAND environment variable not set. pystory won't work without it!")
        print("Disable this message by writing `$ export DISABLE_PYSTORY=1`")
        sys.exit(1)

    return env_path    


def get_command(args):

    command, params = args.command[0], "".join(args.command[1:])

    if is_int(command):
        command, params = 'last', int(command)

    elif command in REQUIRES_PARAMS and params is None:
        sys.exit("Command `%s` expected at least one argument" % command)

    elif command.strip() not in ALLOWED_COMMANDS:
        msg_var = "\n".join(['\t%s' % cmd for cmd in ALLOWED_COMMANDS])
        sys.exit("Given command is not allowed, allowed are: \n%s" % msg_var)

    return command, params


def filter_pysts(pysts, term):
    ret_pysts = []
    for pyst in pysts:
        if term.lower() in pyst[3].lower():
            ret_pysts.append(pyst)

    return ret_pysts


def run_command(pysts, command, params):

    if command == 'find':
        pysts = filter_pysts(pysts, params)
        if pysts:
            print("Commands matching `%s`:" % params)
            print_compressed_pystory(pysts)
        else:
            print("Found no commands matching `%s`:" % params)
        return

    if command == 'last':
        if is_int(params) and params == 0:
            print_compressed_pystory(pysts)
        elif is_int(params):
            # This number should probably be handled after the compression..
            print_compressed_pystory(pysts[-params:])


def get_parser():
    parser = argparse.ArgumentParser(description='Pystory ur lyfe.')
    parser.add_argument('-v', '--verbose')
    parser.add_argument('command', metavar='N', nargs='*', default=[0])

    return parser


def run_pystory(args=None):

    parser = get_parser()
    args = parser.parse_args(args)

    pysts = parse_pystory()

    command, params = get_command(args)
    run_command(pysts, command, params)
