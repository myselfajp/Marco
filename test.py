a = [2, 3, 4, 54, 22, 6, 3, 57, 23, 8, 9, 13, 23, 34, 45, 56]
total_lists = 18  # تعداد لیست‌ها
chunk_size = len(a) // total_lists  # اندازه هر لیست کوچکتر

# محاسبه تعداد عناصر لیست آخر
remainder = len(a) % total_lists

# تقسیم لیست اصلی به 15 لیست کوچکتر
lists = []
start = 0
for i in range(total_lists):
    end = start + chunk_size + (1 if i < remainder else 0)
    lists.append(a[start:end])
    start = end

# چاپ لیست‌های حاصل
for i, lst in enumerate(lists, 1):
    print(f"لیست {i}:", lst)