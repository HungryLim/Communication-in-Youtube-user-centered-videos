# Politicians in Youtube: How do they use their Youtube Channel? 

How do politicians use their Youtube channel? I argue that politicians use their Youtube channel to communicate with their core supporters who closely follow legislative speech and behaviors. Compared to other media outlet often used by politicians such as Twitter or Facebook, Youtube videos in politicians' channels are more focsued on their floor speech or policy-focused messages.

# Motivation
* Youtube is one of the major information sources
* Little known about how legislators show themselves in their Youtube Channel
* Video has many features including text, image and audio


# Literature
* Scholars have studied political advertising in Youtube, but they have not focused how legislators use their Youtube channels overall. 
* Systematic analysis of large scale Youtube data is not done.
    * Klotz 2010; Lev-On 2012; Borah, Porismita, Erika Fowler, and Ridout 2018

# Goals: data
* Short term goal
Find descriptive statistics: channel data and video data
  * video.id, post.time, title, duration, view.count, like.count, dislike.count, comment, transcript etc
* Long term goal
download video, download transcript for analysis

# Research questions
* Short term goals
  * Which politicians use Youtube for what purposes?
  * Are politicians' Youtube contents different from their other media outlets such as Twitter and Facebook?

* Long term goal
  * How do politicians use emotions to affect audience? 
  * How do politicians use images?
  * What is politicians' campaign strategy?
  
  
# Data collecting process
Video and transcript
	\begin{itemize}
	    \item Using all legislators' available Youtube channel id, I scrapped the videos urls.
	    \item Download data to local drive and convert them
	    \item Move the data to Box cloud drive
	    \item Using Cluster to finish the looping
	\end{itemize}
Descriptive data of videos
\begin{itemize}
    \item Youtube API
    \item Other Python packages 
\end{itemize}
		    
