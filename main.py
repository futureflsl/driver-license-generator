from PIL import Image, ImageFont, ImageDraw
import random
from Generator import *
import copy


class DriverLicenseGenerator(object):
    def __init__(self):
        self.zheng_img = Image.open('./moudle/zheng.png')
        self.fu_img = Image.open('./moudle/fu.png')
        self.gen = Generator()
        self.font1 = ImageFont.truetype('./font/驾行中文字体.ttf', 45)
        self.font2 = ImageFont.truetype('./font/方正宋三简体.ttf', 30)
        self.font3 = ImageFont.truetype('./font/行驶2015.ttf', 30)

    def get_image_zheng(self, id, name, sex, nation, addr, birth, first_get_license_date, start_time, stop_time,
                        head_img):
        whole_img = copy.deepcopy(self.zheng_img)
        drawer = ImageDraw.Draw(whole_img)
        drawer.text((491, 180), id, fill=(0, 0, 0), font=self.font3)
        drawer.text((182, 245), name, fill=(0, 0, 0), font=self.font1)
        drawer.text((668, 250), sex, fill=(0, 0, 0), font=self.font1)
        drawer.text((930, 254), nation, fill=(0, 0, 0), font=self.font1)
        drawer.text((197, 328), addr, fill=(0, 0, 0), font=self.font1)
        drawer.text((518, 495), birth, fill=(0, 0, 0), font=self.font3)
        drawer.text((582, 575), first_get_license_date, fill=(0, 0, 0), font=self.font3)
        drawer.text((285, 750), start_time, fill=(0, 0, 0), font=self.font3)
        drawer.text((622, 746), stop_time, fill=(0, 0, 0), font=self.font3)
        whole_img.paste(head_img, (901, 394))
        drawer.text((911, 798), id, fill=(0, 0, 0), font=self.font2)
        drawer.text((85, 494), '江苏省南京', fill=(255, 0, 0), font=self.font1,stroke_width=1)
        whole_img.show()

    def generate_one_zheng(self):
        id = self.gen.get_random_idcard()
        name = self.gen.get_random_name()
        sex = self.gen.get_random_gender()
        nation = '中国/CHN'
        addr = self.gen.get_random_addr()
        birth = self.gen.get_random_date()
        first_get_license_date = self.gen.get_random_date()
        start_time = self.gen.get_random_date()
        stop_time = self.gen.get_random_date()
        head_img = self.gen.get_random_head(sex)
        self.get_image_zheng(id, name, sex, nation, addr, birth, first_get_license_date, start_time, stop_time,
                             head_img)


if __name__ == '__main__':
    dlg = DriverLicenseGenerator()
    dlg.generate_one_zheng()
