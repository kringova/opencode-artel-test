#!/usr/bin/env python3
import argparse
import sys

tasks = []

def cmd_add(args):
    text = " ".join(args.text)
    tasks.append({"id": len(tasks) + 1, "text": text, "done": False})
    print(f"Добавлено: {text}")

def cmd_list(args):
    if not tasks:
        print("Список пуст.")
        return
    for t in tasks:
        status = "✓" if t["done"] else " "
        print(f"  [{status}] {t['id']}. {t['text']}")

def main():
    parser = argparse.ArgumentParser(description="TODO — простой список дел")
    sub = parser.add_subparsers(dest="command")

    add_p = sub.add_parser("add", help="Добавить задачу")
    add_p.add_argument("text", nargs="+", help="Текст задачи")

    sub.add_parser("list", help="Показать все задачи")

    args = parser.parse_args()

    if args.command == "add":
        cmd_add(args)
    elif args.command == "list":
        cmd_list(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
