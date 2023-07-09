import pandas as pd
import numpy as np
import  cv2

df=pd.read_csv('dataset_label_97c.txt')
dm=df.as_matrix()
annotation=''
for d in dm:
    print(d)
    image=cv2.imread(d[0])
    filename=d[0][d[0].find('/')+1:]
    num_plate=image[d[2]:d[4],d[1]:d[3]]
    cv2.imshow('numplate',num_plate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    label=input()
    annotation=annotation+'train-ocr/'+filename+','+label+'\n'
    cv2.imwrite('train-ocr/'+filename,num_plate)

with open('number_label.txt','w') as f:
    f.write(annotation)
f.close()