
import re
import os
import bibtexparser



# 读取bibtex文件，生成字典
bib_name = r'C:\Users\kenger\Documents\GitHub\GH_bot_kenger\wolfbolin\test.bib'

out_bib =  bibtexparser.bibdatabase.BibDatabase()

# 将BibTeX内容分割为各个条目
with open(bib_name, 'r', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# 打印所有解析的条目
for entry in bib_database.entries:
    print(entry)
    title = entry['title']
    entry['title'] = ""
    out_bib.entries.append(entry)

# 打开文件以写入BibTeX数据
with open('out.bib', 'w', encoding='utf-8') as bibtex_file:
    bibtexparser.dump(out_bib, bibtex_file)

