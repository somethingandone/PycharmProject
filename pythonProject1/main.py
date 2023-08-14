import csv
from math import *
import pandas as pd


def read_files():
    print("start reading ratings.csv")
    ratings = pd.read_csv("./ml-latest-small/ratings.csv")
    print("start reading movies.csv")
    movies = pd.read_csv("./ml-latest-small/movies.csv")
    data = pd.merge(movies, ratings, on='movieId')
    print("creating data.csv")
    data[['userId', 'rating', 'movieId', 'title']]. \
        sort_values('userId').to_csv('./ml-latest-small/data.csv', index=False)
    print("start reading data.csv")
    content = {}
    context = open("./ml-latest-small/data.csv", 'r', encoding='UTF-8')
    context.readline()
    for line in context.readlines():
        line = line.strip().split(',')
        if not line[0] in content.keys():
            content[line[0]] = {line[2]: line[1]}
        else:
            content[line[0]][line[2]] = line[1]
    print("finish reading data.csv")
    context.close()
    return content


def recommend(contents):
    print("start computing similarities...")
    recommendations = {}
    result = []
    for userid_first in contents.keys():
        for userid_second in contents.keys():
            if not userid_first == userid_second:
                distance = 0
                userid_first_rating = contents[userid_first]
                userid_second_rating = contents[userid_second]
                for key in userid_first_rating.keys():
                    if key in userid_second_rating.keys():
                        distance += pow(float(userid_first_rating[key])-float(userid_second_rating[key]), 2)
                same = 1 / (1 + sqrt(distance))
                result.append((userid_second, same))
        result.sort(key=lambda value: value[1])
        same_userid_content = contents[result[0][0]]
        recommendation = []
        for content in same_userid_content.keys():
            if content not in contents[userid_first].keys():
                recommendation.append((content, same_userid_content[content]))
        recommendation.sort(key=lambda value: value[1], reverse=True)
        recommendations[userid_first] = recommendation[0]
    print("finish computing same")
    return recommendations


def write_output(recommendations):
    print("start creating output.csv...")
    with open("./ml-latest-small/output.csv", "a", newline="") as f:
        writer = csv.writer(f, dialect="excel")
        writer.writerow(["----userId----", "----movieId----"])
        for item in recommendations.keys():
            writer.writerow([item, recommendations[item][0]])
    print("finish creating output.csv")
    return


if __name__ == '__main__':
    write_output(recommend(read_files()))
