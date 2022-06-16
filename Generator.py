import os

from faker import Faker
import random
from PIL import Image, ImageFont, ImageDraw
import os


class Generator(object):
    def __init__(self):
        self.fake = Faker('zh_CN')
        self.head_path_male_list = []
        self.head_path_female_list = []
        self.__load_head_image_path()

    def __load_head_image_path(self):
        for file in os.listdir('./headimages/male'):
            self.head_path_male_list.append(os.path.join('./headimages/male', file))
        for file in os.listdir('./headimages/female'):
            self.head_path_female_list.append(os.path.join('./headimages/female', file))

    def get_random_name(self):
        return self.fake.name()

    def get_random_addr(self):
        return self.fake.address()

    def get_random_gender(self):
        return '男女'[random.randint(0, 1)]

    def get_random_idcard(self):
        return self.fake.ssn()

    def get_random_phone_number(self):
        return self.fake.phone_number()

    def get_random_date(self):
        return self.fake.date()

    def get_random_head(self, sex):
        if sex == '男':
            img = Image.open(self.head_path_male_list[random.randint(0, len(self.head_path_male_list) - 1)])
        else:
            img = Image.open(self.head_path_female_list[random.randint(0, len(self.head_path_female_list) - 1)])
        return img.resize((302, 405))


if __name__ == '__main__':
    g = Generator()
    print(g.get_random_date())
