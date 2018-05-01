# van-westendorp-chart

Summary
-----
Generate a Van Westendorp pricing chart with matplotlib. Plot Optimal Price Point (OPP) or Range of Acceptable Prices (RAI).

Resources
-----
* 5 Circles Research: http://www.5circles.com/van-westendorp-pricing-the-price-sensitivity-meter/
* driveresearch: https://www.driveresearch.com/single-post/2017/07/02/How-Does-the-van-Westendorp-Pricing-Model-Work

Usage
-----
``` python
import chart_vw

# instantiate and clean
obj = chart_vw.ChartObject(pricing_data_file_path = "../data/example_data.csv")

# plot
obj.plot(intersection="opp", title = "OPP Chart", chart_path = "../charts/example_chart.png"))
```

Output
------
![Chart](https://github.com/cgerson/van-westendorp-chart/blob/master/charts/pricing_chart.png)


More details
------
See "example_plot" notebook for a full demo.