# Digital-Sentiment-Analysis---NLP

Sentiment Analysis - Natural Language Processing

Software requirements Specifications

Technologies used:

1.	Python
a.	Transformers
b.	Pandas
c.	CSV
d.	AutoTokenizer
e.	AutoModelForSequenceClassification
f.	Scipy
2.	Hugging face twitter-roberta-base
3.	Excel


Project Background

With about 4 G&B B2C businesses (Appliances, Interio, Locks and Security solutions), we need sentiment analysis in the Qualitative feedback we have received under NPS scores.
We surveyed 1724 B2C consumers (who intent to purchase from the above 4 businesses from Godrej or our competitors in next 6 months or have purchased within last 12 months).
We covered NCCS A category Indians (Male and Female) across 10 cities, aged 18-50.
This is the first wave of Brand Health Track, and it will be carried out quarterly across four waves in a year.


Present Objective: 

Columns to be referred for the Godrej NPS verbatims: Cleaning, scrubbing, and analysing data present in columns namely:

•	Godrej Appliances: Column CI 
•	Godrej Locks: Column EL
•	Godrej Interio: Column HE
•	Godrej Security solutions: Column JF

Perception mapping/ Sentiment analysis of the verbatims (not looking at word cloud like the ppt attached) with focus areas (both positives/ strengths and negatives/ improvements) 

Cross business analysis if any (Halo effect and spill over from one brand experience to another) as well as Brand pull (Mother brand halo effect over other BUs)


Future Objective: 

Columns to be referred for the Godrej NPS verbatims: Cleaning, scrubbing, and analysing data present in columns namely:

GOOD TO HAVE would also be: Emerging patterns across demographics and eco-social structure as mentioned below.

Example: Godrej Interio has positive sentiments coming from Kolkata, Male, Age 45+, Occupation: Service class, Household income >20Lakhs INR.

Example: Poor service in appliances is attributed mainly to cities of Lucknow & Delhi!  

a.	City, Age, Gender, Education (Columns Z, AA, AB, AC)
b.	NCCS categorization (AD), Occupation (JY), Household income (JZ)
c.	Marital and Household members (KA to KD)

Procedure for performing Operations

1.	Fetching data – For this operation we operate column by column, so we start by copying a column worth data into a .csv file.
2.	To ready the dataset for Cleaning, we use clean.py (A python script) here we are removing all the null values and gibberish from the dataset.
3.	After the cleaning, we must ready the data for a Sentiment Analysis, for the same we have a 3 4-step procedure:
a.	Remove commas, numbers and special characters (,*#$%)
b.	Convert all Big-Case characters to Small-Case (Hello -> hello)
4.	Dropping any Stop words and Spamming (Also, because)After we have readied the data, we push it either to a new or an existing .csv file and run the “Sentiment.py” code which pushes the output to the next column in the same csv file.
5.	This process can then be repeated for all columns of data that requires a sentiment analysis till the goal output is achieved.

One customer should contain one tag only – either he/she is a promoter , or passive, or detractor.


Standing and Open Questions:

1.	Is there any logic to be instilled between the numeric rating of feedback and the sentiment analysis of the verbatim?

a.	Example: 
i.	Rating: 8
ii.	Verbatim: I am satisfied with the design and experience although I believe the product can be more cost-effective -> (Sentiment Analysis:  - Positive = 59%, Negative = 39%, Neutral: 2%)

Essentially is there anything we should be doing with these numbers (e.g., Sum, Average, Special Representation)
•	If score >=8 and positive >=50% , its in sync – label as Promoter
•	If score below 8, positive >=50%, its not in sync and the person is a promoter, label as “Revised promoter”.
•	If score <=8 , (neutral + negative) >=50%, its in sync, label as “Detractor”
•	If score >=8, (neutral + negative)>=50%, its not in sync and person is a passive or detractor. We need to pay heed, label as “Revised Detractor”

2.	What should we exactly be doing with the empty cells?
a.	Example: 
i.	Leave them as they are
ii.	Insert a special word there => (N.A, 0, Empty etc.)
iii.	Delete those Rows

Essentially is there anything specific we should be doing
A.	Run a check horizontally for same customer across 4 columns.If horizontal check throws no other verbatim across 4 columns, write N.A.
B.	If horizontal check throws 1 or 2 more, but we can look at the response and correlate, specially where COUNTA>=2.

3.	What does “Slicing and Dicing” data along with “Scrubbing the data” exactly mean, is there anything we should be doing other than removing the Null Values and Jargon?
Answered below.

4.	For the sentiment analysis, is there any specific intuition required?
Okay.
Intuition means the words we’ve used to analyse the data 

Good words: Nice, Positive, amazing
Neutral: Okay, Satisfactory, mid
Negative Words: Bad, Pathetic, Useless

Millions of English words like these have been used to come up with the dataset, is there any specific trackers you need us to put that will be classified as Positive, Negative or Neutral?



Output for BU1:
1.	Total NPS taker (Count of Verbatims) – 4 BUs and one combined for mother brand
2.	%age of absolute promoters (also passives and detractors)
Need to discuss algorithm. 

Positive	Neutral	Negative	Algorithm
>=70%	30%	Promoter
40%	>=60%	Detractor
Any other ratio is Passive.

3.	Top promoters, top passives, top detractors – BU by BU.

4.	Focus areas to be attained – how can we get that? Bucketing of the repeat verbatims. (eg: Absolute no of promoters in service and detractors in service) 

a. There may be cross BU mention (Appliance, Locks, Security, Interio)
b. Keywords for bucketing (Manual or via Tools):

# Product (keywords for sub buckets: design, modern, stylish, attractive, features, quality, durable, long lasting, material, innovation)
# Price (keywords: costly, high price, market pricing)
# Range (wide options)
# Availability (limited, online, offline, stores)
# Servicing / Customer service
# Reviews / Bad remarks and reviews.
# Brand / Brand image (Trust, Legacy, Heritage, Reliable)
# Experience (reviews, ratings, friends, family)




Future:
5.	Trend analysis for future waves (year 1 , wave 1,2,3,4 then year 2, wave 1,2,3,4, and so on)
6.	Analysis across +ve , Neutral, -ve BU by BU
7.	Analysis across +ve, Neutral , -ve with filters on City, Gender, Age, Education, Occupation, Income, Marital, Household members.






