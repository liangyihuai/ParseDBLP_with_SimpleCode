import xml.etree.ElementTree as et
import os

file_in_path = "dataSetDBLP/dblp.xml"
file_out_clean = "dataSetDBLP/DBLP_clean.txt"
file_out_path = "dataSetDBLP/resultDBLP.txt"

# 1. remove all symbol &, then save the cleaned version to the hard disk
print("remove old file")
if os.path.isfile(file_out_clean):
    # os.remove(file_out_clean)
    raise Exception("file existed")

count = 0
f = open(file_out_clean, 'w+')
with open(file_in_path, mode='r', encoding='utf-8', errors='ignore') as file:
    for line in file:
        line = line.replace('&', '')
        f.write(line)
        count += 1
        if count % 10000 == 0:
            print(count)

# 2. read the cleaned version line by line and get value / content from each XML tag
print("remove old file")
if os.path.isfile(file_out_path):
    os.remove(file_out_path)
f = open(file_out_path, 'w+')
# get an iterable
context = et.iterparse(file_out_clean, events=("start", "end"))
# turn it into an iterator
context = iter(context)
# get the root element
ev, root = next(context)
contents = ""
count  = 0
stack = []
startTag = ""
# the event will be 'start' when meeting <...>, will be 'end' when meeting </...>, e.g.,
# <article>
#    <author> Jone </author>
# </article>
# The events will be 'start', 'start', 'end', 'end'
# So we use a stack to store the tag name. When the stack is empty, we get out of "article".
for event, elem in context:
    tag = elem.tag
    value = elem.text
    if value:
        value = value.encode('utf-8').strip()
    else:
        value = ''

    if event == 'start':
        stack.append(elem.tag)
        if value:
            contents += str(value, 'UTF-8').strip() + ", "
    elif event == 'end':
        if len(stack) != 0:
            stack.pop()
        if len(stack) == 0:
            if value:
                contents += str(value, 'UTF-8').strip() + ","
            f.write(contents)
            f.write('\n')
            contents = ''
            count += 1
            if count % 10000 == 0:
                print(count)
    root.clear()
f.close()