# van-westendorp-chart

Summary
-----
Generate a Van Westendorp pricing chart with matplotlib. Plot Optimal Price Point (OPP) or Range of Acceptable Prices (RAI).

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