#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Разработайте аналог утилиты tree в Linux. Используйте возможности модуля argparse для
управления отображением дерева каталогов файловой системы. Добавьте дополнительные
уникальные возможности в данный программный продукт.
"""

import argparse
import pathlib
import collections
from colorama import Fore, Style
from datetime import datetime


def tree(directory):
    print(Fore.RED + f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = ' ' * depth
        print(Fore.BLUE + f'{spacer} ++ \033 {path.name}')
    print(Style.RESET_ALL)


def main(command_line=None):

    # Создать основной парсер командной строки.

    parser = argparse.ArgumentParser()
    parser.add_argument('tree', action="store", help='Main command')
    parser.add_argument('-c', '--command', action="store", help='additional command')
    parser.add_argument('-t', '--type', action="store", help='search type of file')
    args = parser.parse_args()
    if args.command == "curr":
        print(tree(pathlib.Path.cwd()))
    if args.command == "home":
        print(tree(pathlib.Path.home()))
    if args.command == "count":
        print(collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir()))
    if args.command == "type":
        print(collections.Counter(p.suffix for p in pathlib.Path.cwd().glob(f'*.{args.type}*')))
    if args.command == "last":
        time, file_path = max((f.stat().st_mtime, f) for f in pathlib.Path.cwd().iterdir())
        print(datetime.fromtimestamp(time), file_path)


if __name__ == '__main__':
    main()
