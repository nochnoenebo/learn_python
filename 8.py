formatter = "%s %s %s %s"

print (formatter % (1, 2, 3, 4))
print (formatter % (u"раз", u"два", u"три", u"четыре"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter)) # выводим formatter кот.= строке "%s %s %s %s"
print (formatter % (
    u"Спят в конюшне пони,",
    u"начал пес дремать,",
    u"только мальчик Джонни",
    u"не ложится спать!"
    ))