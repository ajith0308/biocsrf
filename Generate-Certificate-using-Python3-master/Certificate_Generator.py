import pandas as pd
from PIL import Image, ImageDraw, ImageFont
data = pd.read_excel (r'C:\Users\ajith\Desktop\Main_Project_scf\Generate-Certificate-using-Python3-master\Book1.xlsx') 
x=data['Name'].tolist()
y=data['mark'].tolist()
z=data['csrf'].tolist()
xlocation =(500,430)
ylocation=(950,1210)
zlocation=(950,425)
text_color = (0, 120, 209)
text_colorc = (0, 0,0)
fontx= ImageFont.truetype("arial.ttf", 90)
fonty= ImageFont.truetype("arial.ttf", 60)
fontz= ImageFont.truetype("arial.ttf",40)
for i in range(0,len(x)):
    im = Image.open(r'C:/Users/ajith/Desktop/Main_Project_scf/certificate/xth.jpg')
    d = ImageDraw.Draw(im)
    a1=x[i]
    a2=str(y[i])
    a3="SN:"+str(z[i])
    d.text(xlocation, a1, fill = text_color, font = fontx)
    d.text(ylocation,a2, fill = text_color, font = fonty)
    d.text(zlocation,a3, fill = text_colorc, font = fontz)
    im.save("certificate_" +a3+ ".jpg")



