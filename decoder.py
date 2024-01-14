from pydub import AudioSegment

Hamm74 = [[0, 0, 0, 1, 1, 1, 1],
          [0, 1, 1, 0, 0, 1, 1],
          [1, 0, 1, 0, 1, 0, 1]]

# Загрузка аудиофайла
audio_file = AudioSegment.from_file('encoded.wav', format='wav')

# Открытие WAV-файла и чтение последних битов
with open('encoded.wav', 'rb') as wav_file:
    # Чтение заголовка WAV-файла
    header = wav_file.read(44)
    # Чтение данных WAV-файла
    data = wav_file.read()

    # Преобразование данных в список байт
    data_bytes = list(data)
    print(data_bytes[:20])
    # print(data_bytes)
    bit_data_bytes = []

    # Изменение последних битов в данных
    for i in range(len(data_bytes)):
        bit_data_bytes.append(data_bytes[i] & 0x01)
# print(data_bytes[:10])
# print(secret_message)
def sem_blok(mas):
    m_return = []
    for i in range(0, (len(mas)) // 7 * 7, 7):
        m_return.append(mas[i:i+7])
    if (len(mas)) % 7 != 0:
        m_return.append(mas[len(mas) - len(mas) % 7:(len(mas))])
    return m_return

def kod3(matrix):
    m_r1 = []
    for i in range(len(matrix)):
        m_r = []
        s = 0
        if len(matrix[i]) == 7:
            for n in range(len(Hamm74)):
                for m in range(len(Hamm74[n])):
                    s += Hamm74[n][m] * matrix[i][m]
                m_r.append(s % 2)
                s = 0
            for now1 in m_r:
                m_r1.append(now1)
    return m_r1

new_big_mas_sem = sem_blok(bit_data_bytes)
print(new_big_mas_sem[:20])
itog_mas = kod3(new_big_mas_sem)
print(itog_mas[:10])
# print(itog_mas[:10])
# Преобразование измененных данных обратно в байты
data = bytes(itog_mas)
for now in range(20):
    print(data[now])

with open('encoded.wav', 'wb') as encoded_file:
    encoded_file.write(header)
    encoded_file.write(data)
# print(2)
