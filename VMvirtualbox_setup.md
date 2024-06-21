# SET UP Virtual Machines
you can set up multiple windows machines using vm virtual box, here is a general tutorial.
here are some additional references you might find helpful:
[youtube tutorial](https://www.youtube.com/watch?v=nvdnQX9UkMY)
this is on ubuntu,we should install windows.

## 1.Download oracal VM VitualBox

```bash
https://www.virtualbox.org/
```

## 2.Download Windows operating system
install the "Create Windows 10 installation media" to get the iso file
```bash
https://www.microsoft.com/en-us/software-download/windows10
```

## 3.Create new(n) instances of computer in VM Virtual box

click on new(N) and the directory of your previously downloaded iso file in the correct place,
and proceed.
allocate memory based on your needs. IN EXPERIENCE, WINDOWS take 20GB and ANACONDA and other packages needs 5GB, you need around 50GB to ensure smooth operation.


## 4.Open the instance

if there is any issue with that have to do with produce key, click on storage and remove the two undefined disk.
Then re-open the instance.
Finish setting of the windows computer.

## 5. Download ANACONDA or MINICONDA

base on the storage you allocate, download anaconda or miniconda(this will require less storage).
```bash
https://www.anaconda.com/download/success
https://docs.anaconda.com/free/miniconda/
```

## 6. Create and setup environment using environment.yml

open powershell prompt of conda and type
```bash
conda env create -f environment.yml
```

## 7. Download Visual studio code or other IDEs in assisting you
```bash
https://code.visualstudio.com/download
```
## 8. download the files inside VM requirement in github and start running the code!

one thing worth noting is that you should adjust the size and left up right bottom accordingly
when you open up your virtual machine, you can click view, and resize the screen to 100% so that the adjusted coordinates works. 
To be specific, they are 
Youtube: left up(409,174), right bottom(702,635)
Tiktok: initial click(413,550), left up(120,156), right bottom(489,710)
Ins: left up(346,127), right bottom(682,608)
in the pl_classes under the each class variables.


# Log into Accounts

For the platforms Instagram, Youtube, and Tiktok, log in to a brand new account which requires
setting of email, password, code justification(from your email), and birthday. For birthday, I used 2000/1/1 for all of them.

Emails should be aol for instagram and tiktok, and gmail for youtube. Other emails might be prone to security checks and blocks.
You should ensure that the browser which contains your login information is the browser you opened and operated last for the code to open the url in the corresponding accounts.


# Plain strategy

For plain strategy to work, you will have 50 videos played for each platform and each media.
So you will need 9 accounts created for thoes plain strategies.

## Import moldules
In main, import the corresponding modules

```bash
from exp_classes import Simple_Bot, Spatial_Bot, Plain_bot
from pl_classes import TikTok, Youtube, Snap, Instagram
from md_classes import Llava, Gemini, GPT4, GPT4o
```

## Conduct experiments
and then conduct experiments for each trial

```bash
Plain_bot.run_experiment(Youtube(), GPT4o(), 50, 30)
```

here is a detailed explaination of what each parameters meant:
```bash
run_experiment(platform = Youtube(), model = GPT4o(), n = number of trials, time = stay duration when decided to stay)
```

you will get a folder cotaining the 50 pictures in the same directory, and a csv file that records the data

# Simple Strategy

For simple strategy, we introduce the 50 personas that need to be tested on every platform and every model.
for each persona, a total of 9 accounts need to be created and for each of the account, 150 experiments are conducted where the first 100 is on training, and the later 50 is for evaluation.

In main, import the corresponding modules

```bash
from exp_classes import Simple_Bot, Spatial_Bot, Plain_bot
from pl_classes import TikTok, Youtube, Snap, Instagram
from md_classes import Llava, Gemini, GPT4, GPT4o
```
specify persona
```bash
Persona = "i graduated with a statistics degree. i'm a blackjack dealer. i know how to count cards in blackjack. i have 3 kids."
```
run for 150 trials.
```bash
Simple_Bot.run_experiment(Persona, TikTok(), GPT4o(), 100, 30)
Simple_Bot.run_experiment(Persona, TikTok(), GPT4o(), 50, 0)
```


you will get a folder containing 100 pictures for the training phase and another folder containing 50 pictures for evaluation phase. In addition a csv files that contains the 150 rows of data is created.

Note that the "Answer" collume which contains the "yes or no" of the decition might be not the same fromat and not always lowercased.

# Spacial Strategy

The structure of spacial strategy is to first ask the VLM to understand the persona through the question of 
```bash
f"I am scrolling on TikTok, Based on your personality. Can you come up with six general visual content you given your personality might enjoy? Rank it in order. Answer short word separated in commas. Your response should only be the answer."
```
and then check if the video is belonging to any of the 7 categories.
```bash
 f"I am scrolling on TikTok. Based on this screenshot, given 7 catergories: {cate1}, {cate2}, {cate3}, {cate4}, {cate5}, {core},  other.  Help me decide which category it belongs to or related to. Please answer in a single word."
```

For spacial strategy, we introduce the 50 personas and for each persona, 9 accounts are created for testing on three plateforms and three models(can be accomplished through three gmails). Here we donot have duration time specified in main.

150 experiments are conducted where the first 100 is training and the 50 is for eval.

In main, import the corresponding modules, and specify the persona.

```bash
Persona = "i graduated with a statistics degree. i'm a blackjack dealer. i know how to count cards in blackjack. i have 3 kids."
```
And this is the command to run a whole experiment
```bash
Spatial_Bot.run_experiment(Persona, TikTok(),GPT4o(), 100, 50)
```
To explain the code, the parameters are
```bash
run_experiment(interest= persona, platform = Tiktok(), model = GPT4o(), training_number = number of training trails, evaluating_number= number of eval trails)
```

You will get two csvs one containing the training information one with the evaluation. The evaluation does not have the stay duration collumn but have an additional "Type" collume that specify if the interest is core/ general/ other for analysis.




# New Spacial Strategy(prone to change)

```bash
New_spacial_bot.run_experiment(Persona, TikTok(),GPT4o(), 100, 50)
New_spacial_bot.run_experiment(Persona, TikTok(),GPT4o(), 50,0)
```




