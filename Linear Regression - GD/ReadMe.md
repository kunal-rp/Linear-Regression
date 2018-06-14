To Run:

1)Need numpy, matplotlib, and pandas library installed
2)'python main.py' in terminal

Synapses: 

Imagine you are given a scatter plot graph, and you had to find the line that hits all of the points:

![alt text](https://saylordotorg.github.io/text_elementary-algebra/section_06/d59dd27a659d6b4c3a430f37479b34e7.jpg)

For this graph, we can visually see that a simple line can go through all points of the graph.

![alt text](https://saylordotorg.github.io/text_elementary-algebra/section_06/5d10b670d78abac93a4572dc0c2afb0f.jpg)

If we really wanted to, we could represent the line in the y = mx + b formula, the formula being y = -3x +5. Obviously, there is also a mathematic way to dertive the slope, the y-intercept, ect. but I'm assuming you already know all that basic stuff :)

Now how about for THIS graph:

![alt text](https://www.mathsisfun.com/data/images/scatter-ice-cream1.svg)

Now, a linear line cannot pass through all of the points. So what can we do?

Again, visually, we can't get a perfect line, but we can maybe draw the BEST FIT LINE :

![alt text](https://www.mathsisfun.com/data/images/interpolate.svg)

This process, the idea of finding the best fit linear line of a scatter plot, is the idea behind linear regression, one of the basic models for Machine Learning!

For this particular example, the graph shows that relationship between the temperature and the sales of something. With the best fit line, we can now reasonably predict what the sales is going to be given a certain temperature.

So it is easy to do this visually; to find the best fit line, just draw a straight line that is the closest to as many of the points as possible. However, how can we do this with MATH???

My code demonstrates linear regression with gradient descent. Feel Free to run it!!!!
