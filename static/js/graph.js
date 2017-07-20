function getData(screen_name) {
    // var url = "http://localhost:7000/tweets/data?screen_name=" + screen_name;
    var url = "https://mytweetdash.herokuapp.com/tweets/data?screen_name=" + screen_name;
    queue().defer(d3.json, url).await(makeGraphs);
}

// Define days of the week for access in several charts
week_day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

// Average tweets per day
// Average tweets per day of the week 
// 10 most common words 
// Most liked tweets 
// Most retweeted tweets 
// Most liked/retweeted vs common words (crossfilter?) 
// Retweets / favorites by day of week / time of week 
// Most interactions vs time of the day
// Catch 404 for handles that don't exist
// Make accounts (Django?) to handle user sets (name db as user name in Django?)
// Top users (and display their followers)
// Compare 2 accounts side-by-side (draw tables twice using different datasets)
// Color selector with colorwheel that changes the colors of originals/retweets and redraws the charts


function timeOfDay(time) {
    var period = time.getHours();
    if (period >= 22)
        return "Late night";
    else if (period <= 5)
        return "Late night";
    else if (period > 16)
        return "Evening";
    else if (period > 11)
        return "Afternoon";
    else if (period > 6)
        return "Morning";
}

function makeGraphs(error, tweetsJson) {

    // Format all tweet's date using D3 date formats    
    // Raw time format in harvested Tweets: Thu Jun 06 10:51:22 +0000 2017
    // Time format accesors in D3.js:        %a  %b  %d %H:%M:%S %Z    %Y

    var all_tweets = tweetsJson;
    var dateFormat = d3.time.format("%a %b %d %H:%M:%S %Z %Y");
     
    all_tweets.forEach(function (d) {
        d["created_hour"] = dateFormat.parse(d["created_at"]);
        d["created_hour"].setSeconds(0);
        d["created_hour"].setMinutes(0);
        
        d["created_at"] = dateFormat.parse(d["created_at"]);
        return d;
    });


    // Create a variable accesor that allows the plot chart to determine 
    // whether a tweet is a RT or original and color them accordingly
    var tweetColors = d3.scale.ordinal()
            .domain(["ORIGINAL", "RT"])
            .range(["purple", "yellow"]);


    // Create a Crossfilter instance. This will aid in filtering your charts.
    // When you click on a particular chart element, all other charts accomodate 
    // their displayed data to filter on your selection
    var ndx = crossfilter(all_tweets);


    // Counts and groups all tweets in the database
    var all = ndx.groupAll();

    var profileimage = document.createElement('img');
    profileimage.src = all_tweets[0].user_profile_image_url.replace('_normal', '_400x400');
    document.getElementById('profile-image').appendChild(profileimage);
    profileimage.classList.add("img-circle");
    profileimage.classList.add("profile-img");


    // Define Dimensions

    // Dimension by date
    var dateDim = ndx.dimension(function (d) {
        return d["created_hour"];
    });

    // Dimension by favorites count
    var faveDim = ndx.dimension(function (d) {
        return d["favorite_count"];
    });

    // Dimension by retweet count
    var retweetDim = ndx.dimension(function (d) {
        return d["retweet_count"];
    });

    // Dimension by day of the week
    var dayDim = ndx.dimension(function (d) {
        return d["created_hour"].getDay();
    });

    // Dimension by time period
    var periodDim = ndx.dimension(function (d) {
        return timeOfDay(d["created_hour"]);
    });

    // Dimension by hashtags
    var hasHashtagDim = ndx.dimension(function (d) {
        return d["has_hashtags"];
    });

    // Dimension by retweets.
    var isRetweetDim = ndx.dimension(function (d) {
        return d["is_retweet"];
    });



    // Create an empty dictionary that we will use to store all tweets with the tweet date object as the key
    // and the exact second the tweet was created at as the value, this gives the plot dimension 2 coordinates
    // that it uses to plot the chart with
    var tweetsDict = {};

    // Dimension by date and hour, for the scatter plot
    var tweetsByDateAndHourDim = ndx.dimension(function (d, i) {
        tweetsDict[d["created_at"]] = d;
        return [d["created_at"], d["created_at"].getHours() + (d['created_at'].getMinutes()/100) + (d['created_at'].getSeconds()/1000)];
    })

    


    // Calculate groups

    // Groups all tweets by date
    var numTweetsByDate = dateDim.group();

    // Group all tweets by day of the week
    var numTweetsByDay = dayDim.group();

    // Groups all tweets that have a hashtag together. The data value is a boolean, the key is has_hashtag
    var numHasHashtag = hasHashtagDim.group();

    // Groups all tweets by tweet/retweet. The data value is a boolean, the key is is_retweet
    var numAllRetweets = isRetweetDim.group();

    // Groups only tweets that are retweets together. The data value is a boolean, the key is is_retweet
    var numIsRetweet = dateDim.group().reduceSum(function (d) {
        if (d.is_retweet === true ) {
            return 1;
        } else {
            return 0;
        }
    });

    // Groups only tweets that are not retweets together. The data value is a boolean, the key is is_retweet
    var numIsOriginal = dateDim.group().reduceSum(function (d) {
        if (d.is_retweet === false ) {
            return 1;
        } else {
            return 0;
        }
    });

    // Groups all tweets by period of day (morning, afternoon, evening, late night)
    var numTweetsByPeriod = periodDim.group();

    // Groups all tweets by average of tweets per day
    // var numTweetsPerDay = dayDim.group().reduce(
    //         function (p, v) {
    //             ++p.count;
    //             p.total += v.spend;
    //             p.average = p.total / p.count;
    //             return p;
    //         },
    //         function (p, v) {
    //             --p.count;
    //             if(p.count == 0) {
    //                 p.total = 0;
    //                 p.average = 0;
    //             } else {
    //                 p.total -= v.spend;
    //                 p.average = p.total / p.count;
    //             };
    //             return p;
    //         },
    //         function () {
    //             return {count: 0, total: 0, average: 0};
    //         }
    //     );

    // Groups all tweets by date, including minutes and seconds
    var tweetsByDateAndHourGroup = tweetsByDateAndHourDim.group();


 
    // Define values (to be used in charts)
    var minDate = dateDim.bottom(1)[0]["created_hour"];
    var maxDate = dateDim.top(1)[0]["created_hour"];
    var topfavorites = faveDim.top(10)[0]["favorite_count"];
    var topretweets = retweetDim.top(10)[0]["retweet_count"];



    // Declare charts with apropriate #IDs that go to the HTML section
    var timeChart = dc.lineChart("#time-chart");
    var hasHashtagChart = dc.pieChart("#hashtag-pie-chart");
    var uniqueTweetsPie = dc.pieChart("#unique-tweets-pie");
    var uniqueTweetsChart = dc.compositeChart("#unique-tweets-chart");
    var dayOfWeekPie = dc.pieChart("#tweets-by-day-of-week");
    var periodOfDayPie = dc.pieChart("#tweets-by-period-of-day");
    var scatterTweets = dc.scatterPlot("#scatter-Tweets-by-period-of-day");
    var totalTweetsDisplay = dc.numberDisplay("#total-tweets");

    
    // Experimenting with making the charts responsive programatically
    // instead of trying to create multiple media queries and transforms on CSS
    function parentWidth(elem) {
        return elem.parentElement.clientWidth;
    }    

    chart_height_element = document.getElementById('time-chart');
    positionInfo = chart_height_element.getBoundingClientRect();
    chart_height = positionInfo.height;
    // chart_width = parentWidth(document.getElementById('time-chart'));
    chart_width = positionInfo.width;

    pie_height_element = document.getElementById('hashtag-pie-chart');
    pie_position_info = pie_height_element.getBoundingClientRect();
    pie_height = pie_position_info.height;
    pie_width = pie_position_info.width;

    // Define chart properties

    timeChart
        .width(chart_width)
        .height(chart_height)
        .x(d3.time.scale().domain([minDate, maxDate]))
        .interpolate('linear')
        .renderArea(true)
        .round(d3.time.month.round)
        .brushOn(false)
        .elasticY(true)
        .renderDataPoints(true)
        .renderHorizontalGridLines(true)
        .mouseZoomable(true)
        .clipPadding(10)
        .yAxisLabel("Daily Tweets")
        .transitionDuration(500)
        .xAxisLabel("Date")
        .dimension(dateDim)
        .group(numTweetsByDate);

    hasHashtagChart
        .width(pie_width)
        .height(pie_height)
        .radius(90)
        .innerRadius(20)
        .transitionDuration(500)
        .dimension(hasHashtagDim)
        .group(numHasHashtag)
        .label(function (d) {
            if (d.key == true) {
                return 'Hashtags';
            } else {
                return 'No Hashtags'}
        })
        .title(function (d) {
            if (d.key == true) {
                return 'Hashtags: ' + d.value;
            } else {
                return 'No Hashtags: ' + d.value;}
        });

    uniqueTweetsPie
        .width(pie_width)
        .height(window.clientHeight/2)
        .radius(window.innerRadius/2)
        .innerRadius(20)
        .transitionDuration(500)
        .dimension(isRetweetDim)
        .group(numAllRetweets)
        .label(function (d) {
            if (d.key == true) {
                return 'Retweets';
            } else {
                return 'Original';}
        })
        .title(function (d) {
            if (d.key == true) {
                return 'Retweets: ' + d.value;
            } else {
                return 'Original: ' + d.value;}
        });

    dayOfWeekPie
        .width(pie_width)
        .height(window.clientHeight)
        .radius(window.innerRadius)
        .innerRadius(20)
        .transitionDuration(500)
        .dimension(dayDim)
        .group(numTweetsByDay)
        // The following titles and labels call a list called weed_day with the d.key object as the index value
        // which returns Mon-Sun depending on the value of d.key
        .label(function (d) {
            return week_day[d.key];
        })
        .title(function (d) {
            return week_day[d.key] + ": " + d.value;
        });

    periodOfDayPie
        .width(pie_width)
        .height(window.clientHeight)
        .radius(window.innerRadius)
        .innerRadius(20)
        .transitionDuration(500)
        .dimension(periodDim)
        .group(numTweetsByPeriod);

    uniqueTweetsChart
        .width(window.innerWidth/1.80)
        .height(window.innerHeight/2)
        .x(d3.time.scale().domain([minDate, maxDate]))
        .mouseZoomable(true)
        .yAxisLabel("Daily Tweets")
        .xAxisLabel("Date")
        .elasticY(true)
        .legend(dc.legend().x(80).y(20).itemHeight(13).gap(5))
        .renderHorizontalGridLines(true)
        .compose([
            dc.lineChart(uniqueTweetsChart)
                .dimension(dateDim)
                .colors('yellow')
                .renderDataPoints(true)
                .group(numIsRetweet, 'Retweets'),
            dc.lineChart(uniqueTweetsChart)
                .dimension(dateDim)
                .colors('purple')
                .renderDataPoints(true)
                .group(numIsOriginal, 'Originals')
        ])
        .brushOn(false);

    scatterTweets
        .width(window.innerWidth/1.8)
        .height(window.innerHeight/2)
        .x(d3.time.scale().domain([minDate, maxDate]))
        .brushOn(false)
        .mouseZoomable(true)
        .title(function (d) {
            var tweet = tweetsDict[d.key[0]];
            return d.key[0] + ": " + "\n" + tweet['text'];
        })
        .clipPadding(20)
        .symbolSize(7)
        .yAxisLabel("", 10)
        .colorAccessor(function (d) {
            var tweet = tweetsDict[d.key[0]];
            if(tweet.is_retweet)
                return "RT";
            else
                return "ORIGINAL";
        })
        .colors(tweetColors)
        .elasticY(true)
        .dimension(tweetsByDateAndHourDim)
        .group(tweetsByDateAndHourGroup);


        // This D3 function styles the Y axis label on the scatter plot to make it clear it is plotting
        // the Y axis on a 12H format
        scatterTweets.yAxis().tickFormat(function (d) {
            if (d <= 11)  {
                return d + " AM"
            } else {
                return d + " PM"
            }
        });

    totalTweetsDisplay
        .formatNumber(d3.format("d"))
        .valueAccessor(function (d) {
            return d;
        })
        .group(all);

    dc.renderAll();

    var resizeTimer;

    $(window).on('resize', function(e) {

    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {

        timeChart
            .width(window.innerWidth/1.8)
            .height(window.innerHeight/2);
        // hasHashtagChart
        //     .height(window.innerHeight/12)
        //     .width(pie_width)
        //     .redraw();
        // uniqueTweetsPie
        //     .height(window.innerHeight/12)
        //     .width(pie_width)
        //     .redraw();
        scatterTweets
            .width(window.innerWidth/1.8)
            .height(window.innerHeight/2);
        uniqueTweetsChart
            .width(window.innerWidth/1.8)
            .height(window.innerHeight/2);

        window.location.reload();
                
    }, 250);

    });

    // window.onresize = function() {
    //     timeChart
    //         .width(window.innerWidth/1.8)
    //         .height(window.innerHeight/2);
    //     // hasHashtagChart
    //     //     .height(window.innerHeight/12)
    //     //     .width(pie_width)
    //     //     .redraw();
    //     // uniqueTweetsPie
    //     //     .height(window.innerHeight/12)
    //     //     .width(pie_width)
    //     //     .redraw();
    //     scatterTweets
    //         .width(window.innerWidth/1.8)
    //         .height(window.innerHeight/2);
    //     uniqueTweetsChart
    //         .width(window.innerWidth/1.8)
    //         .height(window.innerHeight/2);

    //     dc.redrawAll();
    //     dc.renderAll();

    //     // console.log(svg_width);
    // };

}