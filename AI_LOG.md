# AI Usage Log

Replace this template with your own entries. Add one entry per significant use of an AI tool.

## 1. Setting up Environment

**What I asked:**
- it was my first time using YOLO --> used AI to set it up on VSCode and helping with erros that occured when trying to import some packages (my terminal and VSCode were using different envirnments so some packages weren't compatible)

**What I kept vs. rewrote, and why:**
- I used AI to understand the error and had to fix the problem on my own environment.

**What the AI got wrong that I had to catch:**
- Some stuff the AI recommended me to do didn't do as it intended since the environment I was using already existed as Anaconds. 

**How I verified it (for example, checked the metric by hand, ran it on data it hadn't seen):**
- I ran some of the commands it gave me, understood version differences, then fixed the problems.

## 2. YOLO Training

**What I asked:**
- I asked AI to explain the different parameters used to train a YOLO model so I can properly figure out which ones were most relevant to use during my training

**What I kept vs. rewrote, and why:**
- I used AI's help with syntax and also learned how to make the taining faster using my mac processing unit. However, I did change the numbers it gave me as the parameter options. I chose my own number of epochs, and batch size so I could make sure everything was working well

**What the AI got wrong that I had to catch:**
- There wasn't really anything specifically wrong,  I only adjusted its recommendations ot fit what I thought was a good idea (smaller initial test)

**How I verified it (for example, checked the metric by hand, ran it on data it hadn't seen):**
- I was able to train the model for 5 epochs, everything worked fine

## 3. Understanding Results

**What I asked:**
- I asked AI to explain the relevence of some metrics I wasn't familiar with (mAP@50 and mAP@50-95) and also asked AI to make some easy to follow visualizations of the metrics using comparisons to understand the results better (I included them in my methodology)

**What I kept vs. rewrote, and why:**
-  I used the explanations to improve my understanding so I knew where to go from there in trying to improve model efficiency. I also did keep the visualizations since it did a pretty good job in summarizing some results and made model comparisons easier

**What the AI got wrong that I had to catch:**
- There wasn't really much error involved since I gave it the exact metrics and values as well as gave ideas for some visualizations

**How I verified it (for example, checked the metric by hand, ran it on data it hadn't seen):**
- I made sure it got all the values and metrics correct when explaining and creating visuals

## 4. Input/Output Folder Advice

**What I asked:**
- I sent it my logic to ask for user input by them typing it after running the file, but AI recommended me to instead use argparse to more closely align with the project requirements. 

**What I kept vs. rewrote, and why:**
- I decided to listen to the advice because when reading about argparse on google, it seemed to be what the project was expecting when it asked to take the image and output folder as arguements

**What the AI got wrong that I had to catch:**
- I think the suggestion to use argparse was a good one though I'm still not completely sure how neccessary that implemented change was

**How I verified it (for example, checked the metric by hand, ran it on data it hadn't seen):**
- I just learned about the module from AI and went to Google to learn about how it works
