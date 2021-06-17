import chart_studio.plotly as py
import cufflinks as cf

cf.go_offline(connected=True)
import json
import pandas as pd

with open('D:/movie_review/new_data_review/the_outlaws/review_data.json', "r", encoding='utf-8') as f:
    review_data = json.load(f)
count = 1
sum = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
while (count <= 28531):
    rating = review_data[count - 1]["rating"].strip()
    rating = int(rating)
    print(rating)
    if rating == 1:
        a += 1
    elif rating == 2:
        b += 1
    elif rating == 3:
        c += 1
    elif rating == 4:
        d += 1
    elif rating == 5:
        e += 1
    elif rating == 6:
        f += 1
    elif rating == 7:
        g += 1
    elif rating == 8:
        h += 1
    elif rating == 9:
        i += 1
    elif rating == 10:
        j += 1

    count += 1
df = pd.DataFrame({"rating": [a, b, c, d, e, f, g, h, i, j]})
df.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
layout = {
    'title':
        {
            'text': '<b>Distribution of ratings by film</b>',
            'font': {
                'size': 17,
                'color': '#37474F'
            },
            'x': 0.5,
            'y': 0.88

        },
    'xaxis': {
        'showticklabels': True,
        'dtick': 1,
        'title': {
            'text': 'Rating',
            'font': {
                'size': 13,
                'color': '#37474F'
            }
        }
    },
    'yaxis': {
        'showticklabels': True,
        'title': {
            'text': 'Number',
            'font': {
                'size': 13,
                'color': '#37474F'
            }
        }

    }
}
df.iplot(kind='scatter', mode='lines+markers', layout=layout)