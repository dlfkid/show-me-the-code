# coding=utf-8
# !/usr /bin/env python
# -*- coding: utf-8 -*-


# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont

origin_avatar = "avatar.jpg"
saved_avatar = "modified_Avatar.jpg"
sample_font = "Arial.ttf"
color = (255, 0, 0)


def draw_text_in_avatar(text, filled_color, font):
	try:
		image = Image.open(origin_avatar)
		x, y = image.size
		print("图片的Size为: ", image.format, image.size, image.mode)
		image.show()

		draw = ImageDraw.Draw(image)
		text_font = ImageFont.truetype(font, 35)
		draw.text((x - 20, 7), text, filled_color, text_font)

		image.save(saved_avatar)
		image.show()
	except Exception:
		print("Unable to load image")
	else:
		pass
	finally:
		pass


if __name__ == "__main__":
	number = str(4)
	draw_text_in_avatar(number, color, sample_font)