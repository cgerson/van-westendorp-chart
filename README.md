# van-westendorp-chart

Summary
-----
Generate a Van Westendorp pricing chart with matplotlib. Plot Optimal Price Point (OPP) or Range of Acceptable Prices (RAI).

Usage
-----
``` python
    import chart_vw

    # instantiate and clean
    obj = chart_vw.ChartObject(pricing_data_file_path = "example_data.csv")
    
    # plot
    obj.plot(intersection="opp", title = "OPP Chart", chart_path = "example_chart.png"))
```

See "example_plot" notebook for a full demo.