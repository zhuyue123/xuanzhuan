import os
from PIL import Image as img
imgTypes = ['.png','.jpg','.bmp']
#angle = 0
size = 128
for root, dirs, files in os.walk(".", topdown=True):
    for currentFile in files:
        imagefile=os.path.join(root,currentFile)
        if imagefile[imagefile.rindex('.'):].lower() in imgTypes:
            im = img.open(imagefile)
            im_resized = im.resize((size, size),img.BILINEAR)
            # NEAREST：最近滤波。从输入图像中选取最近的像素作为输出像素。它忽略了所有其他的像素。
            # BILINEAR：双线性滤波。在输入图像的2x2矩阵上进行线性插值。注意：PIL的当前版本，做下采样时该滤波器使用了固定输入模板。
            # BICUBIC：双立方滤波。在输入图像的4x4矩阵上进行立方插值。注意：PIL的当前版本，做下采样时该滤波器使用了固定输入模板。
            # ANTIALIAS：平滑滤波。这是PIL 1.1.3版本中新的滤波器。对所有可以影响输出像素的输入像素进行高质量的重采样滤波，
            # 以计算输出像素值。在当前的PIL版本中，这个滤波器只用于改变尺寸和缩略图方法。
            # #注意：在当前的PIL版本中，ANTIALIAS滤波器是下采样（例如，将一个大的图像转换为小图）时唯一正确的滤波器。
            # BILIEAR和BICUBIC滤波器使用固定的输入模板，用于固定比例的几何变换和上采样是最好的。
            #im_rotate = im_resized.rotate(angle)
            #out = im_resized.transpose(img.FLIP_LEFT_RIGHT)
            #out = im_resized.transpose(img.FLIP_TOP_BOTTOM)
            out = im_resized.transpose(img.ROTATE_90)
            #out = im_resized.transpose(img.ROTATE_180)
            #out = im_resized.transpose(img.ROTATE_270)
            outfile = os.path.join(root,'newdata',currentFile)
            out.save(outfile)




