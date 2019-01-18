lunch = {
    '김밥카페': '02-1234-5678',
    '양자강': '02-2345-6789',
    '순남시래기': '02-9876-5432'
}

lunch2 = [
    {
        '상호명': '김밥카페',
        '전화번호': '02-1234-5678',
    },
    {
        '상호명': '양자강',
        '전화번호': '02-2345-6789',
    },
    {
        '상호명': '순남시래기',
        '전화번호': '02-9876-5432',
    }
]

# with open('lunch.csv', 'w') as f:
#     f.write('상호명,전화번호\n')
#     for name, phone in lunch.items():
#         f.write('{},{}\n'.format(name, phone))


import csv

# menu = ['김밥', '탕수육', '시래기']

# with open('lunch.csv', 'w') as f:
#     cw = csv.writer(f)
    
#     # cw.writerow(리스트)
#     cw.writerow(menu)
    
with open('lunch.csv', 'w') as f:
    # writer = csv.Dictwriter(f, 필드네임(튜플))
    field = ('상호명', '전화번호')
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
    for l in lunch2:
        writer.writerow(l)
    
# with open('lunch.csv', newline = '') as f:
#     cr = csv.reader(f)
#     for row in cr:
#         print(row)