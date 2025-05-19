#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Set


def count_lines_and_chars(file_path: str) -> Tuple[int, int]:
    """
    Подсчитывает количество строк и символов в файле.

    Args:
        file_path: Путь к файлу

    Returns:
        Кортеж (количество_строк, количество_символов)
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
            lines = content.splitlines()
            return len(lines), len(content)
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return 0, 0


def scan_directory(directory: str, extensions: Set[str] = None,
                   ignore_dirs: Set[str] = None) -> Dict[str, Dict[str, int]]:
    """
    Сканирует директорию и подсчитывает статистику для всех файлов.

    Args:
        directory: Корневая директория для сканирования
        extensions: Набор расширений файлов для обработки (например, {'.py', '.js'})
                   Если None, обрабатываются все файлы
        ignore_dirs: Набор имен директорий, которые следует игнорировать

    Returns:
        Словарь статистики по типам файлов
    """
    if ignore_dirs is None:
        ignore_dirs = {'.git', '.svn', '__pycache__', 'node_modules', 'venv', '.venv', 'env'}

    stats = {}
    total_lines = 0
    total_chars = 0
    total_files = 0

    for root, dirs, files in os.walk(directory):
        # Игнорируем указанные директории
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()

            # Если указаны расширения и текущее расширение не в списке - пропускаем
            if extensions and file_ext not in extensions:
                continue

            lines, chars = count_lines_and_chars(file_path)

            # Добавляем статистику по расширению
            if file_ext not in stats:
                stats[file_ext] = {
                    'lines': 0,
                    'chars': 0,
                    'files': 0
                }

            stats[file_ext]['lines'] += lines
            stats[file_ext]['chars'] += chars
            stats[file_ext]['files'] += 1

            total_lines += lines
            total_chars += chars
            total_files += 1

    # Добавляем суммарную статистику
    stats['ВСЕГО'] = {
        'lines': total_lines,
        'chars': total_chars,
        'files': total_files
    }

    return stats


def format_stats(stats: Dict[str, Dict[str, int]]) -> str:
    """
    Форматирует статистику для вывода в консоль.

    Args:
        stats: Словарь статистики

    Returns:
        Отформатированная строка статистики
    """
    result = "\nСтатистика по файлам проекта:\n"
    result += "-" * 60 + "\n"
    result += f"{'Тип файла':<15} {'Файлов':<10} {'Строк':<10} {'Символов':<15}\n"
    result += "-" * 60 + "\n"

    # Сначала выводим статистику по расширениям
    for ext, data in sorted(stats.items()):
        if ext != 'ВСЕГО':
            result += f"{ext or 'БЕЗ РАСШ.':<15} {data['files']:<10} {data['lines']:<10} {data['chars']:<15}\n"

    # Затем выводим общую статистику
    result += "-" * 60 + "\n"
    result += f"{'ВСЕГО':<15} {stats['ВСЕГО']['files']:<10} {stats['ВСЕГО']['lines']:<10} {stats['ВСЕГО']['chars']:<15}\n"

    return result


def main():
    """
    Основная функция программы.
    Разбирает аргументы командной строки и выполняет подсчет статистики.
    """
    parser = argparse.ArgumentParser(description='Подсчет строк кода и символов в проекте')
    parser.add_argument('directory', type=str, nargs='?', default='.',
                        help='Корневая директория проекта (по умолчанию: текущая директория)')
    parser.add_argument('-e', '--extensions', type=str, nargs='+',
                        help='Расширения файлов для обработки (например: .py .js .html)')
    parser.add_argument('-i', '--ignore', type=str, nargs='+',
                        help='Дополнительные директории для игнорирования')

    args = parser.parse_args()

    directory = args.directory
    extensions = set(args.extensions) if args.extensions else None

    ignore_dirs = {'.git', '.svn', '__pycache__', 'node_modules', 'venv', '.venv', 'env'}
    if args.ignore:
        ignore_dirs.update(args.ignore)

    print(f"Сканирование директории: {os.path.abspath(directory)}")
    if extensions:
        print(f"Обрабатываемые расширения: {', '.join(extensions)}")

    stats = scan_directory(directory, extensions, ignore_dirs)
    print(format_stats(stats))


if __name__ == "__main__":
    main() 