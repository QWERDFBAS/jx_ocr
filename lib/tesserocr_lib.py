# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/8 15:34'

import tesserocr


#api法调用tesserocr
#选择语言为中文简体
api = tesserocr.PyTessBaseAPI(lang='chi_sim')

api.SetImageFile('/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/Snip20180223_59.png')


print api.GetUTF8Text().strip()





# api.SetImageFile('/Users/MRJ/PycharmProjects/OCR v1.0/lib/smoothing2.jpg')
# print api.GetUTF8Text().strip()
#print tesserocr.image_to_text(image)  # print ocr text from image
# or
#调用file_to_text方法
#print tesserocr.file_to_text('t/Users/MRJ/PycharmProjects/OCR v1.0/lib/grayimg1.jpg',lang='chi_sim')