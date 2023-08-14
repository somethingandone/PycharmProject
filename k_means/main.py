import numpy
from PIL import Image as image
from k_means import run_kmeans


def load_data(file):
    f = open(file, "rb")
    datas = []
    im = image.open(f)
    im = im.resize((512, 512))
    m, n = im.size
    print(m, n)
    for i in range(m):
        tmp_re = []
        for j in range(n):
            tmp = []
            x, y, z = im.getpixel((i, j))
            tmp.append(x)
            tmp.append(y)
            tmp.append(z)
            tmp_re.append(tmp)
        datas.append(tmp_re)
    f.close()
    return numpy.array(datas)


if __name__ == '__main__':
    k = 6
    file_path = "pic.png"
    print("----------load image-----------")
    data = load_data(file_path)
    print("---------- run k_means ------------")
    run_kmeans(data, k)
