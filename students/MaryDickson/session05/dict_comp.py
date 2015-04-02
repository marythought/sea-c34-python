food_prefs = {"name": u"Mary",
              u"city": u"Seattle",
              u"cake": u"carrot",
              u"fruit": u"mango",
              u"salad": u"cucumber",
              u"pasta": u"angel hair"}

print (
    "{name} lives in {city} and she likes {cake} cake,"
    "{fruit} fruit, {salad} salad, and {pasta} pasta.".format(**food_prefs)
)

d = dict(zip((i for i in range(1, 17)),
             (i for i in range(1, 11) + ["A", "B", "C", "D",
                                         "E", "F"])))

print d

new_d = food_prefs.copy()
new_d_a = dict(zip((i for i in new_d.keys()),
                   (i.count("a") for i in new_d.values())))
print new_d_a

s2 = [i for i in range(0, 21) if i % 2 == 0]
s3 = [i for i in range(0, 21) if i % 3 == 0]
s4 = [i for i in range(0, 21) if i % 4 == 0]
print s2, s3, s4


def makeset(num):
    x = [i for i in range(0, 21) if i % num == 0]
    return x

print makeset(2)
print makeset(5)
