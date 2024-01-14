from pydub import AudioSegment
import wave
import io
def sem_blok(mas):
    m_return = []
    for i in range(0, (len(mas)) // 7 * 7, 7):
        m_return.append(mas[i:i+7])
    if (len(mas)) % 7 != 0:
        m_return.append(mas[len(mas) - len(mas) % 7:(len(mas))])
    return m_return

def tree_blok(mas):
    m_return = []
    for i in range(0, (len(mas)) // 3 * 3, 3):
        m_return.append(mas[i:i+3])
    if (len(mas)) % 3 != 0:
        m_return.append(mas[len(mas) - len(mas) % 3:(len(mas))])
    return m_return

def prov_matrix(matrix):
    for i in range(len(matrix)):
        m_r = []
        s = 0
        if len(matrix[i]) == 7:
            for n in range(len(Hamm74)):
                for m in range(len(Hamm74[n])):
                    s += Hamm74[n][m] * matrix[i][m]
                m_r.append(s % 2)
                s = 0
            des = m_r[0] * 4 + m_r[1] * 2 + m_r[2]
            if des != 0:
                matrix[i][des - 1] = int(not matrix[i][des - 1])
            m_r = []

def mas_mas(mas7, mas3):
    for i in range(len(mas3)):
        if len(mas3[i]) == 3:
            des = (mas3[i][0] * 4) + (mas3[i][1] * 2) + mas3[i][2]
            if des != 0:
                mas7[i][des - 1] = int(not mas7[i][des - 1])
            des = 0

def obr_sem_blok(mas7):
    m_r = []
    for i in mas7:
        for j in i:
            m_r.append(j)
    return m_r


# Преобразование аудиофайла в WAV
audio_file = AudioSegment.from_file('lagrang.mp3', format='mp3')
audio_file.export('lagrang.wav', format='wav')

audio_file1 = AudioSegment.from_file('alla.mp3', format='mp3')
audio_file1.export('alla.wav', format='wav')


Hamm74 = [[0, 0, 0, 1, 1, 1, 1],
          [0, 1, 1, 0, 0, 1, 1],
          [1, 0, 1, 0, 1, 0, 1]]

# Открытие WAV-файла и чтение последних битов
with open('lagrang.wav', 'rb') as wav_file:
    # Чтение заголовка WAV-файла
    header = wav_file.read(44)
    # Чтение данных WAV-файла
    data = wav_file.read()

    # Преобразование данных в список байт
    data_bytes = list(data)

    # print(data_bytes)
    bit_data_bytes = []

    # Изменение последних битов в данных
    for i in range(len(data_bytes)):
        bit_data_bytes.append(data_bytes[i] & 0x01)

def two_in_ten(ten):
    mas_r = []
    cv = 128
    while cv != 0.5:
        if ten // cv == 1:
            mas_r.append(1)
            ten %= cv
        else:
            mas_r.append(0)
        cv /= 2
    return mas_r

# Открытие WAV-файла и чтение последних битов
with open('alla.wav', 'rb') as wav_file:
    # Чтение заголовка WAV-файла
    header1 = wav_file.read(44)
    # Чтение данных WAV-файла
    data1 = wav_file.read()

    # Преобразование данных в список байт
    data_bytes1 = list(data1)

    # print(data_bytes)
    bit_data_bytes_small = []

    # Изменение последних битов в данных
    for i in range(len(data_bytes1)):
        # print(data_bytes1[i])
        t = two_in_ten(data_bytes1[i])
        # print(t)
        for now in t:
            bit_data_bytes_small.append(now)

y_big = sem_blok(bit_data_bytes)
# print(y_big[:10])
z_small = tree_blok(bit_data_bytes_small)
# print(z_small[:20])
prov_matrix(y_big)
# print(y_big[:10])
mas_mas(y_big, z_small)
# print(y_big[:10])
mom = obr_sem_blok(y_big)
# print(mom[:20])
for i in range(len(data_bytes)):
    data_bytes[i] = (data_bytes[i] & 0xFE) | mom[i]
# print(data_bytes)
# Преобразование измененных данных обратно в байты
data = bytes(data_bytes)
# for now in range(20):
#     print(data[now])
# Создаем объект AudioSegment из байтов
# sound = AudioSegment.from_file(io.BytesIO(data))

with open('encoded.wav', 'wb') as encoded_file:
    encoded_file.write(header)
    encoded_file.write(data)
print(2)




# РАСКОДИРОваниЕ

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
# print(new_big_mas_sem[:20])
itog_mas = kod3(new_big_mas_sem)
# print(itog_mas[:10])
# print(itog_mas[:10])
# Преобразование измененных данных обратно в байты
data = bytes(itog_mas)
# for now in range(20):
#     print(data[now])

with open('decoded.wav', 'wb') as encoded_file:
    encoded_file.write(header1)
    encoded_file.write(data1)
# print(2)