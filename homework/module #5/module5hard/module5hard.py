import time

class User:
    def __init__(self, nickname = None, password = None, age = None):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return(self.nickname)
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname and password == i.password:
                self.current_user = i

    def register(self, nickname, password, age):
        password = hash(password)
        for j in self.users:
            if nickname == j.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for n in args:
            if n not in self.videos:
                self.videos.append(n)

    def get_videos(self, word):
        l_list = []
        for k in self.videos:
            if word.lower() in k.title.lower():
                l_list.append(k.title)
        return l_list

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for m in self.videos:
            if m.title == title:
                if m.adult_mode and self.current_user.age < 18:
                    print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for s in range(1, m.duration + 1):
                        print(s, end=' ')
                        time.sleep(1)
                    print(f'Конец видео')
        if title not in self.videos:
            return



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



