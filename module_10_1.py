import threading
import time
from time import sleep

def write_words(word_count, file_name):

    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file1 = file.write(f'Какое-то слово № {i+1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}.')

    return file1
time_start = time.time()
write_words(10, 'example1')
write_words(30, 'example2')
write_words(200, 'example3')
write_words(100, 'example4')
time_end = time.time()
print(f'Работа функций: {time_end - time_start}')

write_words1 = threading.Thread(target=write_words, args=(10, 'example5'))
write_words2 = threading.Thread(target=write_words, args=(30, 'example6'))
write_words3 = threading.Thread(target=write_words, args=(200, 'example7'))
write_words4 = threading.Thread(target=write_words, args=(100, 'example8'))
time_start = time.time()
write_words1.start()
write_words2.start()
write_words3.start()
write_words4.start()
write_words1.join()
write_words2.join()
write_words3.join()
write_words4.join()
time_end = time.time()
print(f'Работа потоков: {time_end - time_start}')
