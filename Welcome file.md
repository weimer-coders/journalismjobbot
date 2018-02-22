---


---

<h1 id="journalism-job-bot">Journalism Job Bot</h1>
<p>This is a Twitter bot designed to help journalists find job opportunities on Twitter through certain hashtags and strings. As graduating seniors, the job hunt has been on our minds a lot so we wanted to help people find opportunities that they can apply for. We started with #journojob and #journalismjob hashtags but we wanted to make it more challenging than just a retweet bot.</p>
<p>We started out with the tutorials. One of our challenges were limiting geography, because we got a lot of tweets from Europe and Asia. We tried to limit it with a line of code. We originally ran it with a 5 second sleep function but we were overwhelmed with the amount of tweets so we decided to switch to once an hour. This became too much for our followers, and we started to lose followers. After conducting a Twitter poll we decided to tweet once every few hours. We deployed the bot using Heroku.</p>
<p>We experimented with hashtags to see which ones had the best results. For example, #writingjobs had a lot of blogging and fiction writing jobs, and #mediajob had a lot of conspiracy theories.</p>
<h1 id="bot-tutorials">Bot Tutorials</h1>
<p>We began by using tutorials by using the following tutorials:</p>
<ul>
<li><a href="https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app">How To Create a Twitter App</a>
<ul>
<li>this shows how to get the credentials for your Twitter Bot</li>
</ul>
</li>
<li><a href="https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library">How To Create a Twitterbot with Python 3 and the Tweepy Library</a>
<ul>
<li>this shows how to retweet from a hashtag</li>
</ul>
</li>
</ul>
<h1 id="heroku">Heroku</h1>
<p>Using Heroku was tricky because most tutorials use a <a href="http://credentials.py">credentials.py</a> document. We struggled to figure out how to connect Heroku to Github and how to use the scheduler. Here are some resources that helped us:</p>
<ul>
<li><a href="https://www.youtube.com/watch?v=DwWPunpypNA">15.8: Heroku Deployment - Twitter Bot Tutorial</a></li>
<li><a href="https://devcenter.heroku.com/articles/scheduler">Heroku Scheduler</a></li>
</ul>

