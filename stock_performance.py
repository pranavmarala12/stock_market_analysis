import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker



df = pd.read_csv("stock_data.csv")


df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')


pivot_df = df.pivot(index='Date', columns='Ticker', values='Close')
pivot_df = pivot_df.sort_index()


normalized_df = pivot_df / pivot_df.iloc[0] * 100

# look for different style of chart within seaborn library
plt.style.use("seaborn-v0_8-darkgrid")
sns.set_context("talk", font_scale=1.1)
fig, ax = plt.subplots(figsize=(16, 8))


for ticker in normalized_df.columns:
    ax.plot(normalized_df.index, normalized_df[ticker], label=ticker, linewidth=2)

# format x and y axis labels
ax.set_title("Stock Performance (Normalized to 100)", fontsize=18, weight='bold', pad=20)
ax.set_xlabel("Date", fontsize=14)
ax.set_ylabel("Performance (Start = 100)", fontsize=14)
ax.legend(title="Company", bbox_to_anchor=(1.05, 1), loc='upper left')
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

ax.set_ylim(bottom=100)
ax.set_yscale('log')

fig.text(0.5, 0.01, "EACH LINE SHOWS STOCK GROWTH USING 100 AS THE BASELINE VALUE",
         ha='center', fontsize=12, style='italic')

plt.show()

