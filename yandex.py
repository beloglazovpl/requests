class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = 'AQAAAAAFE9JKAADLW7TXSY42c0hxkWbi60UwKsE'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)