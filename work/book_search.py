def book_search(keyword):
    results = list()
    with open('book_data.tsv', encoding='utf-8') as f:
        for line in f:
            cols = line.split('\t')
            if keyword in cols[0]:
                results.append(line)
    if len(results) > 0:
        response = ''.join(results)
    else:
        response = '"{}"の含まれる書籍が見つかりませんでした'.format(keyword)
    return response

if __name__ == '__main__':
    print(book_search('いちばんやさしい'))
    print(book_search('寿司'))
    