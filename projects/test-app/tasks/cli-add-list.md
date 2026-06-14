---
id: 2
project: "[[test-app/test-app]]"
status: todo
tags: [task]
created: 2026-06-14
created_at: 2026-06-14T00:00:00
updated: 2026-06-14
closed_at:
sp: 3
rice_reach: 8
rice_impact: 4
rice_confidence: 90
rice_effort: 0.6
summary: "CLI: команды add и list"
roles: [reviewer]
model_tier: middle
---

## Что нужно сделать
Реализовать CLI на Python с командами `add <текст>` (добавить задачу) и `list` (показать все задачи). Хранение — в памяти, без персистенции пока.

## Почему важно
Это ядро приложения — без добавления и отображения ничего не работает.

## Критерии готовности (DoD)
- [ ] Команда `add "Купить молоко"` добавляет задачу
- [ ] Команда `list` выводит все задачи с номерами
- [ ] Скрипт запускается: `python todo.py add "тест"` и `python todo.py list`

## Пререквизиты
нет

## Вопросы
нет

## Заметки
Первая задача проекта. argparse или click — на усмотрение.
