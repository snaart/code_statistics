# Code Statistics

Инструмент командной строки для подсчета статистики кода в проектах.

## Возможности

- Подсчет количества строк и символов в файлах проекта
- Группировка статистики по типам файлов
- Фильтрация по расширениям файлов
- Игнорирование указанных директорий

## Установка

```bash
pip install --index-url https://test.pypi.org/simple/ code-statistics
```

## Использование

### Командная строка

```bash
# Базовое использование (сканирование текущей директории)
code-stats

# Сканирование указанной директории
code-stats /путь/к/проекту

# Сканирование только файлов с определенными расширениями
code-stats -e .py .js .html

# Игнорирование дополнительных директорий
code-stats -i build dist
```

### Использование как библиотеки

```python
from code_statistics import scan_directory, format_stats

# Сканирование директории
stats = scan_directory("./проект", extensions={".py", ".js"})

# Вывод статистики
print(format_stats(stats))
```

## Разработка

```bash
# Клонирование репозитория
git clone https://github.com/nikitastepanov/code-statistics.git
cd code-statistics

# Установка зависимостей для разработки
pip install -e .
```

## Лицензия

MIT 