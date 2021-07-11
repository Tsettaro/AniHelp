import pandas as pd
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# a = "750 руб."
# print(a[:-5])
df = pd.DataFrame(columns=['name', 'price', 'shop', 'category'])
_df = pd.DataFrame([['namae[i]', 'price[i]', 'Discomir', 'Manga']], columns=['name', 'price', 'shop', 'category'])
df = df.append(_df, ignore_index=True)
print(df)
# import itertools
# s = "ABC"
# com_set = itertools.combinations(s, 2)
# for i in com_set:
#     print(i[1])
