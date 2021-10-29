# 1408. 24

h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))

sec1 = h1 * 3600 + m1 * 60 + s1
sec2 = h2 * 3600 + m2 * 60 + s2

sec = sec2 - sec1
if sec < 0:
    sec += 24 * 3600

hour = sec // 3600
sec -= hour * 3600
min = sec // 60
sec -= min * 60
print(f"{hour:02d}:{min:02d}:{sec:02d}")
