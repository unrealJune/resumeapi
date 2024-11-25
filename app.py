# June Philip
# API to send resume info via RESTful API, allowing for live updates to resume

from flask import Flask, request, jsonify
import os
import json
import urllib.request
from helpers import Job, Bullet

testJobs = [Job(0,'Software Engineer', 'Google', 'Mountain View, CA', '2019-2020', [Bullet('Worked on the search team', [Bullet('Implemented new search algorithm', [])])]), Job(1,'Software Engineer', 'Facebook', 'Menlo Park, CA', '2017-2019', [Bullet('Worked on the ads team', [Bullet('Optimized ad serving algorithm', [])])])]
#get env variable for source URL
source_url = os.getenv('SOURCE_URL')

#load data
jobs = None
try:
    with urllib.request.urlopen(source_url) as url:
        data = json.loads(url.read().decode())
        jobs = []
        for job in data['jobs']:
            bullets = []
            for bullet in job['bullets']:
                subbullets = []
                for subbullet in bullet['subbullets']:
                    subbullets.append(Bullet(subbullet['text'], []))
                bullets.append(Bullet(bullet['text'], subbullets))
            jobs.append(Job(job['id'], job['title'], job['company'], job['location'], job['timerange'], bullets))
except:
    print('Error getting data from source')
    

app = Flask(__name__)

#route to get data
@app.route('/jobs', methods=['GET'])
def jobs():
    if jobs:
       return { 'jobs': [job.serialize() for job in jobs] }
    else:
        return 'Error getting data', 500
    
#get specific job by id
@app.route('/job/<id>', methods=['GET'])
def job(id):
    if jobs:
        for job in jobs:
            if str(job.id) == id:
                return job.serialize()
        return 'Job not found', 404
    else:
        return 'Error getting data', 500
