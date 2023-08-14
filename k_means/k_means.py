import random

import numpy as np
from PIL import Image as image


# 进行聚类中心获取
def get_centroids(data, clusters, k):
    k_centroids = []
    for i in range(k):
        cluster_indices = np.nonzero(clusters[:, :, 0] == i)
        cluster_points = data[cluster_indices]
        centroids = np.mean(cluster_points, axis=0)
        k_centroids.append(centroids)
    return k_centroids


# 判断是否有同样的样本
def is_same(centroids, cmp):
    for centroid in centroids:
        if np.all(centroid == cmp):
            return True
    return False


# k_means++算法计算与中心最近距离
def nearest(point, centroids):
    min_dist = np.inf
    m = np.shape(centroids)[0]
    for i in range(m):
        dist = distance(point, centroids[i])
        if min_dist < dist:
            min_dist = dist
    return min_dist


# 用于k_means++算法获得初始中心
def rand_center_plus_plus(data, k: int = 2):
    centroids = []
    x = np.random.randint(0, np.shape(data)[0])
    y = np.random.randint(0, np.shape(data)[1])
    centroids.append([data[x][y]])
    dist = []
    for i in range(1, k):
        sum_all = 0
        for j in range(np.shape(data)[0]):
            for ids in range(np.shape(data)[1]):
                dist.append((nearest(data[j][ids], centroids), (j, ids)))
                sum_all += dist[-1]
        sum_all = random.random() * sum_all
        for di in dist:
            sum_all -= di[0]
            if sum_all > 0:
                continue
            centroids.append(di[1])
            break
    return centroids


# 进行中心随机生成
def rand_center(data, k: int = 2):
    centroids = []

    print(np.shape(data))
    for i in range(0, k):
        x = np.random.randint(0, np.shape(data)[0])
        y = np.random.randint(0, np.shape(data)[1])
        while is_same(centroids, data[x][y]):
            x = np.random.randint(0, np.shape(data)[0])
            y = np.random.randint(0, np.shape(data)[1])
        centroids.append(data[x][y])

    return centroids


# 进行欧式距离计算
def distance(vec_a, vec_b):
    vec_a = np.array(vec_a)
    vec_b = np.array(vec_b)
    return np.linalg.norm(vec_a - vec_b)


# 生成图片
def make_picture(data, clusters):
    pic_new = image.new("RGB", (np.shape(data)[0], np.shape(data)[1]))
    # 颜色表
    color_state = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [0, 255, 255], [255, 0, 255]]
    for i in range(clusters.shape[0]):
        for j in range(clusters.shape[1]):
            pic_new.putpixel((i, j), tuple(color_state[int(clusters[i, j, 0])]))
    pic_new.save("result.jpeg", "JPEG")


def run_kmeans(data, k):
    print("----- 随机初始化center --------")
    centroids = rand_center(data, k)

    print("进行计算")
    clusters = np.zeros((np.shape(data)[0], np.shape(data)[1], 2))
    changed = True
    op = 0
    while changed:
        print("第{}次计算".format(op))
        op += 1
        changed = False
        for i in range(np.shape(data)[0]):
            for j in range(np.shape(data)[1]):
                min_dist = np.inf
                cluster_id = -1
                for ids in range(k):
                    dist = distance(data[i][j], centroids[ids])
                    if dist < min_dist:
                        cluster_id = ids
                        min_dist = dist
                if clusters[i, j, 0] != cluster_id:
                    changed = True
                clusters[i, j, 0] = cluster_id
                clusters[i, j, 1] = min_dist
        centroids = get_centroids(data, clusters, k)
    make_picture(data, clusters)
    print("----- finished -----")
