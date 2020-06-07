import cv2 as cv
import numpy as np
#import xlsxwriter
from openpyxl import Workbook

def counting():
    workbook = Workbook('avgDEV.xlsx')
    worksheet = workbook.create_sheet('asdafsd')
    worksheet.append(['asd', 'fasdf', 'gsdfg'])

    #for i in range(1, 5)
    img_name = 'edgeImage.jpg'
    img = cv.imread(img_name)
    boundaries = [
        ([0, 0, 0], [255, 255, 255])
        ]

    for(lower, upper) in boundaries:

        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
        mask = cv.inRange(img, lower, upper)
        output = cv.bitwise_and(img, img, mask = mask)

    tot_pixel = output.size
    red_pixel = np.count_nonzero(output)
    percentage = round(red_pixel * 100 / tot_pixel, 2)

    #workbook = xlsxwriter.Workbook('avgDEV.xlsx')
    #worksheet = workbook.add_worksheet()

    print("Color pixels: " + str(red_pixel))
    print("Total pixels: " + str(tot_pixel))
    print("Percentage of color pixels: " + str(percentage) + "%")

    #worksheet.append([red_pixel, tot_pixel, percentage])
    #workbook.save('avgDEV.xlsx')
    #workbook.close()
    #worksheet.write('A1', str(red_pixel))
    #worksheet.write('B1', str(tot_pixel))
    #worksheet.write('C1', str(percentage))
    #workbook.close()
