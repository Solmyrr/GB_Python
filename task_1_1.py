duration = int(input("Выведите время в секундах: "))
while duration > 0:
    d = duration // 86400
    h = (duration - (d * 86400)) // 3600
    min = (duration - (d * 86400) - (h * 3600)) // 60
    sec = (duration - (d * 86400) - (h * 3600) - (min * 60))
    print(d, "дн", h, "час", min, 'мин', sec, "сек")
    duration = int(input("Выведите время в секундах: "))