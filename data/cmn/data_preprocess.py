import random

if __name__ == '__main__':
    en_sent_all = []
    ch_sent_all = []
    with open('./cmn.txt', 'r', encoding='utf-8') as f:
        datas = f.readlines()
        random.shuffle(datas)
        for row_data in datas:
            print(row_data)
            res = row_data.split('\t')
            print(res)
            en_sent = res[0]
            ch_sent = res[1]
            print(en_sent)
            print(ch_sent)
            en_sent_all.append(en_sent)
            ch_sent_all.append(ch_sent)
            print('****')

    with open('./cmn_ch_train.txt', 'w', encoding='utf-8') as w1:
        for row_sentence in ch_sent_all[:26155]:
            w1.write(row_sentence+'\n')

    with open('./cmn_en_train.txt', 'w', encoding='utf-8') as w2:
        for row_sentence in en_sent_all[:26155]:
            w2.write(row_sentence+'\n')

    with open('./cmn_ch_valid.txt', 'w', encoding='utf-8') as w1:
        for row_sentence in ch_sent_all[26155:]:
            w1.write(row_sentence+'\n')

    with open('./cmn_en_valid.txt', 'w', encoding='utf-8') as w2:
        for row_sentence in en_sent_all[26155:]:
            w2.write(row_sentence+'\n')
