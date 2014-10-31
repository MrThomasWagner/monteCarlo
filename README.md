monteCarlo
==========

Quick example for Monte Carlo approxiamations. If you have iPython Notebooks set up I've included the .pynb file.  Otherwise you can use the .py


Have used this to approxiamate future required database capacities.  

For example, say you are tracking clicks on a site to generate a heatmap (what parts of my site are users actually USING).  You store all the clicks from the last 2 weeks in a database which are used to generate the heatmap.  A single entry contains the coordinates of the click, on which page, on which site.  If you are actively tracking clicks for 2000 sites and want to add the feature to another 1000 sites, what is a fair estimation of the newly required database capacity?

At first it seems the linear approach might work, simply expect 50% more usage.  But, not all sites are as popular as others and some sites store 20K clicks for the last two weeks and others store only 1K (there is a lot of deviation, so using the linear approach will get a decent approxiamation, but doesn't tell us anything on what a reseasonable upper bound may be for the new required database capacity). 

The Monte-Carlo method gives a good estimation on what the best, worst, and average cases might be, and can be used to create bell curves to visualize them all at once.

The basic method is - Given a list of click-counts for the existing sites already using the heatmaps, randomnly select X click-counts from the given list, where X is the total number of new sites.  So, for our example, randomnly select and sum 3000 numbers which are chosen from the raw data given by the existing 2000 sites.  Repeat this process many times, and graph each randomnly generated sum to give a distribution graph of expected outcomes.

Once you plot the histogram, you can see the benefit and get a great upper bound on your new needed database capacity!