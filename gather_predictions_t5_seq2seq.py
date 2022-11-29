import os
import shutil

from data import DATA_DIR


def main():
    os.mkdir(f'{DATA_DIR}/predictions')
    for label_desc_type in ['original', 'simplified']:
        for dataset in ['uklex-l1', 'eurlex-l1', 'mimic-l1', 'bioasq-l1', 'uklex-l2', 'eurlex-l2', 'mimic-l2', 'bioasq-l2']:
            if not os.path.exists(f'{DATA_DIR}/predictions/{dataset}'):
                os.mkdir(f'{DATA_DIR}/predictions/{dataset}')
            BASE_DIR = f'{DATA_DIR}/logs/adafactor/{dataset}/t5-base-seq2seq-{label_desc_type}/fp32'
            if not os.path.exists(BASE_DIR) and label_desc_type == 'simplified':
                BASE_DIR = f'{DATA_DIR}/logs/adafactor/{dataset}/t5-base-seq2seq/fp32'
                if not os.path.exists(BASE_DIR):
                    print(path + ' NOPE')
                    continue
            elif not os.path.exists(BASE_DIR):
                print(path + ' NOPE')
                continue
            OUTPUT_DIR = f'{DATA_DIR}/predictions/{dataset}/seq2seq-{label_desc_type}'
            os.mkdir(OUTPUT_DIR)
            for seed in [21, 32, 42, 84]:
                seed = f'seed_{seed}'
                path = os.path.join(BASE_DIR, seed, 'test_predictions.pkl')
                if not os.path.exists(path):
                    print(path + ' NOPE')
                    continue
                os.mkdir(OUTPUT_DIR + f'/{seed}')
                shutil.copy(path, OUTPUT_DIR + f'/{seed}/' + 'test_predictions.pkl')
                shutil.copy(path.replace('test_predictions.pkl', 'test_labels.pkl'),
                            OUTPUT_DIR + f'/{seed}/' + 'test_labels.pkl')
                print(path + ' EXISTS')


if __name__ == '__main__':
    main()