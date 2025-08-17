# Financial Market and Employment Data Analysis  
*Exploring Correlations with Web Scraping and Python*  

---

## Overview  
This project investigates the relationship between **financial market performance** and **U.S. employment trends** over the past decade (**2010–2024**).  

Using **web scraping** and publicly available datasets, I collected and cleaned historical data from multiple sources — including equity markets, commodities, and macroeconomic indicators — and compared them to employment statistics.  

The goal was to determine whether changes in employment levels align with trends in the **S&P 500, Dow Jones, NASDAQ, Gold, Oil, and Bitcoin**. While the overall correlation was modest, interesting patterns emerged during major economic disruptions such as the **COVID-19 pandemic**.  

Even though the data did not fully support the strong relationship I anticipated, the project provided valuable practice in **data acquisition, cleaning, and visualization** using Python, HTML, and web scraping techniques.  

---

## Key Findings  
- Only a **slight correlation** was observed between employment and market returns over the 10+ year period.  
- The correlation appeared **stronger during the COVID-19 years (2020–2021)**, when both employment and markets were highly volatile.  
- Long-term market trends often moved **independently of employment fluctuations**, suggesting more complex underlying drivers.  

---

## Tools & Skills  
- **Languages**: Python, HTML  
- **Libraries**: `yfinance`, `pandas`, `datetime`  
- **Techniques**: Web scraping, data cleaning, time-series analysis, feature engineering, visualization  
- **Data Sources**:  
  - [Yahoo Finance](https://finance.yahoo.com/) → historical market prices  
  - [FRED (Federal Reserve Economic Data)](https://fred.stlouisfed.org/) → M2 money supply, macro indicators  
  - [Bureau of Labor Statistics (BLS)](https://www.bls.gov/) → employment data  

---

## Project Workflow  

1. **Data Collection**  
   - Scraped and downloaded 10+ years of historical market data (equities, commodities, cryptocurrency).  
   - Retrieved macroeconomic indicators (employment statistics, M2 money supply) from FRED and BLS.  

2. **Data Cleaning**  
   - Removed unnecessary fields and rows.  
   - Forward-filled missing values for non-trading days to maintain consistency.  

3. **Feature Engineering**  
   - Calculated **annual returns** from December 31 closing prices.  
   - Built **monthly snapshots** to align with employment statistics for comparison.  

4. **Analysis & Visualization**  
   - Compared financial returns against employment trends.  
   - Identified time periods (e.g., COVID years) where correlations were more noticeable.  

5. **Output**  
   - Exported cleaned datasets and calculated metrics to CSV for further analysis and dashboarding.  

---

## Reflection  
Although the project did not uncover the strong correlation I originally expected, it was a **successful exploration in combining financial and economic datasets**. It strengthened my skills in **data wrangling, financial analysis, and storytelling with data**, while also highlighting the complexity of macroeconomic relationships.  

---

## 🚀 Future Improvements  
- Expand analysis to include **interest rates and inflation** as additional macroeconomic factors.  
- Incorporate **machine learning models** to better quantify predictive relationships.  
- Build an **interactive dashboard** for real-time visualization (Tableau).  

---
