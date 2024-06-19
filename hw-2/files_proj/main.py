#для добавления новых типов файлов придется добавить небольшое количество кода если в базовом классе описать
# основные методы взаимодействия с файлом.
# При наследовании класса для работы с новым типом файла придется дописать только методы уникальные для этого типа файла,
# например написать код для конвертации
#
class BaseFile:
    def __init__(self, name, size, date, owner):
        self.name = name
        self.size = size
        self.date = date
        self.owner = owner

    def convert(self): pass  # базовый метод конвертации

    def get_feature(self): pass  # базовый метод извлечения фичи

    def create_file(self): pass  # метод создания файла

    def delete_file(self): pass  #метод удаления файла

    def save(self): pass  # метод для сохранения файла


class AudioFile(BaseFile):
    #  переопределение метода init для того чтобы добавить уникальные метаданные для этого типа файлов(например битрейт)
    def __init__(self, name, size, date, owner, bitrate):
        super().__init__(name, size, date, owner)
        self.bitrate = bitrate

    def convert(self): pass  # переопределенный метод конвертации

    def get_feature(self): pass  # переопределенный метод извлечения фичи


class VideoFile(BaseFile):
    def convert(self): pass  # переопределенный метод конвертации

    def get_feature(self): pass  # переопределенный метод извлечения фичи


class PhotoFile(BaseFile):
    def convert(self): pass  # переопределенный метод конвертации

    def get_feature(self): pass  # переопределенный метод извлечения фичи


class RemoteAudioFile(AudioFile):
    def connect(self, address): pass  # метод для подключения к удаленному хранилищу

    def download(self): pass  # метод для копирования файла в локальное хранилище

    def convert(self): pass  # переопределенный метод конвертации

    def get_feature(self): pass  # переопределенный метод извлечения фичи



file_1 = AudioFile('testFile', 1234, '19.06.2024', 'Andrew')

print (file_1.name)
