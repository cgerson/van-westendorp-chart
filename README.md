# van-westendorp-chart

Summary
-----
Generate a Van Westendorp pricing chart with matplotlib. Plot Optimal Price Point (OPP) and/or Range of Acceptable Prices.

Resources
-----
* 5 Circles Research: http://www.5circles.com/van-westendorp-pricing-the-price-sensitivity-meter/
* driveresearch: https://www.driveresearch.com/single-post/2017/07/02/How-Does-the-van-Westendorp-Pricing-Model-Work
* Nufer Marketing Research: http://www.nufermr.com/the-price-is-right-using-the-van-westendorp-price-sensitivity-analysis-to-help-set-price/
* MedPanel: http://www.medpanel.com/van-westendorp-price-sensitivity-meter/

Usage
-----
``` python
import chart_vw

# instantiate object and process data -> remove outliers, remove illogical responses
obj = chart_vw.ChartObject(pricing_data_file_path = "../data/example_data.csv")

# plot Optimal Price Point (OPP) and save file to chart_path
obj.plot(intersection="opp", title = "Example", chart_path= "../charts/example_chart.png", 
         annotate=True, OPP_coords=(12,29))
```

Output
------
![Chart](https://github.com/cgerson/van-westendorp-chart/blob/master/charts/example_chart.png)


More details
------
See "example_plot" notebook for a full demo.