def all_variants(text):                                     #оу ес, у меня получилось
    start_of_cut = 0
    end_of_cut = 1
    while True:
        yield text[start_of_cut:start_of_cut + end_of_cut]
        start_of_cut += 1
        if end_of_cut == len(text):
            break
        elif (start_of_cut + end_of_cut) > len(text):
            start_of_cut = 0
            end_of_cut += 1


a = all_variants("abcdefgh")
for i in a:
    print(i)
