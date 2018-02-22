---
<h1 id="journalism-job-bot">Journalism Job Bot</h1>

<p>As journalism seniors who will soon be graduating from the University of Florida, the job hunt has been on our minds frequently. We set out to create a Twitter bot that retweets tweets with popular hashtags in order to help journalists like us find job opportunities.</p>

<p> We used Python and Tweepy to make the bot and deployed the final product using Heroku. The following tutorials were helpful in creating a retweet bot.</p>

<h2 id="bot-tutorials">Bot Tutorials:</h2>
<p>We began by using tutorials by using the following tutorials:</p>
<ul>
<li><a href="https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app">How To Create a Twitter App</a>
<ul>
<li>Before creating a Twitter bot, you must first create a Twitter app. This tutorial sets the foundation and explains how credentials work.</li>
</ul>
</li>
<li><a href="https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library">How To Create a Twitterbot with Python 3 and the Tweepy Library</a>
<ul>
<li>This shows how to use the Tweepy library and accomplish tasks such as retweeting from a hashtag.</li>
</ul>
</li>
</ul>

<h2 id="heroku">Heroku links:</h2>
<ul>
<li><a href="https://www.youtube.com/watch?v=DwWPunpypNA">15.8: Heroku Deployment - Twitter Bot Tutorial</a></li>
  <ul>
<li>This helped us get started with Heroku.</li>
</ul>
<li><a href="https://devcenter.heroku.com/articles/scheduler">Heroku Scheduler</a></li>
  <ul>
<li>This helped us set up Heroku Scheduler so that the app could run on a regular basis.</li>
</ul>
</ul>

<h2> Problem solving and limitations </h2>

<p>We experimented with different hashtags to see which ones had the best results, checking in on the bot every few hours to make sure that the tweets we were sharing were relevant. While hashtags like #journalismjobs, #journojobs and #pubjobs yielded relevant results, others were not as pertinent for our followers. For example, #writingjobs had a lot of blogging and fiction writing jobs, and #mediajob (singular, not plural) was included in several tweets with conspiracy theories about the Parkland shooting. Sometimes the right hashtags also picked up blog posts about jobs, or threads where people shared tips or concerns about the journalism job hunt. </p>

<p> Next, we had to decide how often we wanted to tweet new job postings to our followers. Setting up a sleep function allowed us to space out the tweets. We initially programmed the bot to tweet every hour, but we soon realized that we were losing followers. After conducting a Twitter poll we decided to tweet once every six hours. </p>
  
 <p> Though were were able to solve most of our problems through trial and error, there were still several limitations from the Twitter API that we had were not able to overcome. One issue we ran into was geographic location. After seeing tweets pop up about jobs from Europe and Asia, we tried to limit the tweets we gathered to only those from the United States. Even though we added a line of code to constrict the location of the tweets, a person in America could tweet about a foreign journalism job and that would still come up in our feed. </p>

<h2>Questions? Comments?</h2>
<p> We had a blast making this Twitter bot, and we hope it helps you find your next journalism job! Please reach out with feedback:</p>

<ul>
  <li>Gabrielle Calise</li>
    <ul> 
      <li><a href="https://github.com/gabriellecalise">Github</a></li>
      <li><a href="https://twitter.com/gabriellecalise">Twitter</a></li>
    </ul>
  <li>Nicole Dan</li>
    <ul> 
      <li><a href="https://github.com/nicoledan">Github</a></li>
      <li><a href="https://twitter.com/NicoleKDan">Twitter</a></li>
    </ul>
 </ul>

