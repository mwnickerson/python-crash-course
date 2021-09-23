# active discussions
# bar chart showing the most active discussions on Hacker News

import requests
from plotly.graph_objs import Bar
from plotly import offline
from operator import itemgetter

# make an api call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status Code: {r.status_code}")

# process info about the submissions
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # api call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\t status: {r.status_code}")
    response_dict = r.json()
    # build dictionary for each article
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        # this is a paid article with comments disabled
        continue
    else:
        submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts,
                          key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# create the lists for plotting
titles, num_comments, discn_links = [], [], []
for sd in submission_dicts:
    title = sd['title']
    hn_link = sd['hn_link']
    discn_link = f"<a href='{hn_link}'>{title[:15]}...</a>"

    titles.append(title)
    num_comments.append(sd['comments'])
    discn_links.append('discn_link')

# make the bar chart
data = [{
    'type': 'bar',
    'x': titles,
    'y': num_comments,
    'hovertext': discn_links,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most Active Articles on Hacker News',
    'titlefont': {'size': 24},
    'xaxis': {
        'title': 'Article',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': 'Number of Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
}

fig = {'data': data, 'layout':my_layout}
offline.plot(fig, filename='active_discussions.html')









