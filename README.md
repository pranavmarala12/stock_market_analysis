# stock_market_analysis

For this project, I found a dataset (stock_data.csv) on Kaggle that contained data metrics I was looking for: ticker, open price, and more importantly 10 years of stock market data. My goal for this project was to take a large handful of companies in the S&P 500 and compare aggregate growth for the last 10 years. For this project, I knew I was going to use matplotlib, pandas, and seaborn libraries. This project in partcular uses more seaborn features that allowed me to create a more dynamic customized graph.

After importing a few libraries, I then called in my dataset and got to work. Becauase I was dealing with a siginficant amount of data that was depending on a timeframe, I aligned all of the dates in the dataset into a Month/Day/Year format. After this was formatted, I wanted to make sure this my graph did not look like previous bar charts that I had output during previous programming projects. I searched the web for different graph formats that I could use to effectively show my data. I set the style to "seaborn-v0_8-darkgrid". 

After formatting the x and y axis' and labeling the chart, I ran into a problem. One company in the dataset (NVDA) actually performed so well, that it made the rest of the companies in the dataset look like they had barely any growth over the 10 year window. Obviously this was not the case in reality so I had to play around with the Y axis. After some research, I learned that I had two realistic options to fix the scale of the y axis. Using 100 as the starting value - so that I could solely focus on postive growth and not take negative hiccups into consideration - I was able to set a true baseline instead of 0. 

First, I used ax.set_yscale('linear') - this created the output that allowed NVDA to show the skewed data growth that showed poor performance by the other companies. This can be seen in the "data with linear.png" file.  

I pivoted and used ax.set_yscale('log') - this fixed the chart being totally skewed by NVDA. This allowed the scaling of the Y axis to use a logarithmic scale (10^2, 10^3, etc) and subsequently fixed the skew. This can seen in the "data with log.png" file. 

While every coding project requires some problem solving skills, this project was a prime opportunity for me to think outside the box and leverage outside resources to not just customize the appearance of my graph, but significantly change the way my data was displayed. As a finance major during undergraduate study this was a super rewarding project to work on. 

