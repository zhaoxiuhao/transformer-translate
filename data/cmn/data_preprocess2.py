import random
import pandas as pd
if __name__ == '__main__':
    sent_all = []
    with open('./cmn.txt', 'r', encoding='utf-8') as f:

        datas = f.readlines()
        random.shuffle(datas)
        for row_data in datas:
            ch_en_sentence = []
            print(row_data)
            res = row_data.split('\t')
            print(res)
            en_sent = res[0]
            ch_sent = res[1]
            print(en_sent)
            print(ch_sent)
            ch_en_sentence.append(ch_sent)
            ch_en_sentence.append(en_sent)
            sent_all.append(ch_en_sentence)
            print('****')

    print(len(sent_all))
    print(sent_all[0])

    name = ['src', 'trg']
    news_train_data = pd.DataFrame(columns=name, data=sent_all[:26155])
    news_train_data.to_csv('./cmn_train.csv', encoding='utf-8', index=False)
    news_dev_data = pd.DataFrame(columns=name, data=sent_all[26155:])
    news_dev_data.to_csv('./cmn_dev.csv', encoding='utf-8', index=False)
