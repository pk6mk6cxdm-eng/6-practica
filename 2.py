class UserProfile:
    def __init__(self, username, phone, photo):
        self.username = username
        self.phone = phone
        self.photo = photo

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 3:
            raise ValueError("Пайдаланушы аты кемінде 3 таңбадан тұруы керек!")
        self.__username = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if not value.isdigit():
            raise ValueError("Телефон тек сандардан тұруы керек!")
        if len(value) < 10:
            raise ValueError("Телефон нөмірі кемінде 10 цифр болуы керек!")
        self.__phone = value

    @property
    def photo(self):
        return self.__photo

    @photo.setter
    def photo(self, value):
        if not value.endswith((".jpg", ".png")):
            raise ValueError("Сурет форматы .jpg немесе .png болуы керек!")
        self.__photo = value

    def show_info(self):
        print("\nПрофиль ақпараты:")
        print("Аты:", self.username)
        print("Телефон:", self.phone)
        print("Сурет:", self.photo)

class ProfileManager:
    def __init__(self):
        self.profiles = {}

    def create_profile(self, username, phone, photo):
        if username in self.profiles:
            print(f"{username} атты профиль бар.")
            return self.profiles[username]
        profile = UserProfile(username, phone, photo)
        self.profiles[username] = profile
        print(f"{username} атты профиль құрылды.")
        return profile

    def get_profile(self, username):
        return self.profiles.get(username)

    def delete_profile(self, username):
        if username in self.profiles:
            del self.profiles[username]
            print(f"{username} атты профиль өшірілді.")

manager = ProfileManager()

while True:
    username = input("\nПайдаланушы аты (stop - шығу): ")
    if username.lower() == "stop":
        break

    profile = manager.get_profile(username)
    if not profile:
        phone = input("Телефон нөмірі: ")
        photo = input("Сурет файлы (.jpg/.png): ")
        try:
            profile = manager.create_profile(username, phone, photo)
        except ValueError as e:
            print("Қате:", e)
            continue

    while True:
        profile.show_info()
        print("\n1 - Атын өзгерту")
        print("2 - Телефон өзгерту")
        print("3 - Сурет өзгерту")
        print("4 - Шығу")
        choice = input("Таңдау: ")

        if choice == "4":
            break

        try:
            if choice == "1":
                new_name = input("Жаңа ат: ")
                profile.username = new_name
            elif choice == "2":
                new_phone = input("Жаңа телефон: ")
                profile.phone = new_phone
            elif choice == "3":
                new_photo = input("Жаңа сурет: ")
                profile.photo = new_photo
            else:
                print("Белгісіз таңдау!")
        except ValueError as e:
            print("Қате:", e)