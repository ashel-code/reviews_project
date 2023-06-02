import pickle

class Record():
    def __init__(self, 
                 text, 
                 vector,
                 is_fake):
        self.x = vector
        self.y = is_fake
        self.text = text


class StoredData():
    def __init__(self, data):
        dataset = [[data[0][0], pickle.loads(bytes.fromhex(data[0][1])), data[0][2]]]
        for i in range(1, len(data)):  
            print(i)
            dataset.append([data[i][0], pickle.loads(bytes.fromhex(data[i][1])), data[i][2]])

        fake = []
        not_fake = []

        for i in range(len(dataset)):
            if dataset[i][2] == 1:
                fake.append(dataset[i])
            else:
                not_fake.append(dataset[i])
        
        max_abs_value = 0
        for i in range(len(fake)):
            tmp = max(abs(min(fake[i][1])), max(fake[i][1]))
            if tmp > max_abs_value:
                max_abs_value = tmp

        for i in range(len(not_fake)):
            tmp = max(abs(min(not_fake[i][1])), max(not_fake[i][1]))
            if tmp > max_abs_value:
                max_abs_value = tmp

        fake_len_all = len(fake)
        fake_len_train = round(len(fake) * 0.8)
        fake_len_test = fake_len_all - fake_len_train

        not_fake_len_data = round(len(fake) * 1.5)
        not_fake_len_all = len(not_fake)
        not_fake_len_train = round(not_fake_len_data * 0.8)
        not_fake_len_test = not_fake_len_data - not_fake_len_train
        


        data_all = []
        data_train = []
        data_test = []
                    
        for i in range(fake_len_all):
            res_vector = ((fake[i][1] / max_abs_value) + 1) / 2

            if i < fake_len_train:
                data_train.append(Record(fake[i][0], res_vector, fake[i][2]))
            elif i < fake_len_train + fake_len_test:
                data_test.append(Record(fake[i][0], res_vector, fake[i][2]))

            data_all.append(Record(fake[i][0], res_vector, fake[i][2]))

        for i in range(not_fake_len_all):
            res_vector = ((not_fake[i][1] / max_abs_value) + 1) / 2

            if i < not_fake_len_train:
                data_train.append(Record(not_fake[i][0], res_vector, not_fake[i][2]))
            elif i < not_fake_len_train + not_fake_len_test:
                data_test.append(Record(not_fake[i][0], res_vector, not_fake[i][2]))

            data_all.append(Record(not_fake[i][0], res_vector, not_fake[i][2]))
