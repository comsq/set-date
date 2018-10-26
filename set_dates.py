#!/usr/bin/env python3
"""Скрипт для подмены даты изменения скриншота."""

import os
import re
import subprocess


DATETIME_PATTERN = re.compile(r'.*?(\d{4}).(\d{2}).(\d{2}).(\d{2}).(\d{2}).(\d{2})\.png$')


def get_date_time(filename):
    """Получение компонент даты по регулярному выражению."""
    match = DATETIME_PATTERN.search(filename)

    return match[1], match[2], match[3], match[4], match[5], match[6]


def main():
    """Получение скриншотов из текущей директории, подмена даты модификации."""
    for filename in os.listdir():
        if filename.endswith('.png'):
            year, month, day, hour, minute, second = get_date_time(filename)

            cmd = f'touch -t {year}{month}{day}{hour}{minute}.{second}'

            subprocess_parts = cmd.split()
            subprocess_parts.append(filename)
            subprocess.Popen(subprocess_parts, stdout=subprocess.PIPE).communicate()


if __name__ == '__main__':
    main()
