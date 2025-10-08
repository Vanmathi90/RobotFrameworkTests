import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from lxml import etree
import sys

build_id = sys.argv[0]
print(f"Build ID: build_id")
tree = etree.parse('reports/build_id/output.xml')
tag_stats = tree.xpath('//statistics/tag/stat')
headers = ['Requirement','Total', 'Pass', 'Fail', 'NoRun']
table_data = []
tag_labels, tag_pass_count, tag_fail_count, tag_skip_count = [], [], [], []
for each_tag in tag_stats:
    total = int(each_tag.get('pass')) + int(each_tag.get('fail')) + int(each_tag.get('skip'))
    table_data.append([each_tag.text, total, each_tag.get('pass'), each_tag.get('fail'), each_tag.get('skip')])
    tag_labels.append(each_tag.text)
    tag_pass_count.append(int(each_tag.get('pass')))
    tag_fail_count.append(int(each_tag.get('fail')))
    tag_skip_count.append(int(each_tag.get('skip')))
tags_count = len(tag_stats)
col_count = 3
row_count = (tags_count // 3) + 1
ind = np.arange(len(tag_labels))
print(f'col_count :{col_count}')
print(f'row_count :{row_count}')
print(f'Tag Labels:{tag_labels}')
print(f'Tag Pass:{tag_pass_count}')
print(f'Tag Fail:{tag_fail_count}')
print(f'Tag No Run:{tag_skip_count}')
print(f'Table data:{table_data}')
matplotlib.use('Agg')

plt.bar(tag_labels, tag_pass_count, label='Pass', color='#9BE198')
plt.bar(tag_labels, tag_fail_count, bottom=tag_pass_count, label='Fail', color='#FF9999')
plt.bar(tag_labels, tag_skip_count, bottom=np.array(tag_pass_count) + np.array(tag_fail_count), label='NoRun', color='#D3D3D3')
plt.title('Robot Test Run Results')
plt.xticks(ind, tag_labels, rotation=30, ha='right')
plt.xlabel('Requirements')
plt.ylabel('Count')
plt.savefig('reports/build_id/report.png')
plt.close()

plt.figure(figsize=(4,2))
plt.axis('off')
table = plt.table(cellText=table_data, colLabels=headers, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(list(range(len(headers))))
plt.savefig('reports/build_id/table.png', dpi=100, bbox_inches='tight', pad_inches=0)
