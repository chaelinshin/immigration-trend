// set the dimensions and margins of the graph
var margin = {left:80, right:20, top:50, bottom:100};
var height = 500 - margin.top - margin.bottom,
    width = 800 - margin.left - margin.right; 

// append the svg object to the body of the page
var svg = d3.select("#chart-area")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

//labels
var xLabel = svg.append("text")
    .attr("y", height+70)
    .attr("x", width/2)
    .attr('font-size', '20px')
    .attr('text-anchor', 'middle')
    .text("G20 Countries"); 

var yLabel = svg.append("text")
    .attr("transform", 'rotate(-90)' )
    .attr("y", -60)
    .attr('x', -200)
    .attr('font-size', '20px')
    .attr("text-anchor", 'middle')
    .text("Number of Refugees"); 

// Initialize the X axis
var x = d3.scaleBand()
  .range([ 0, width ])
  .padding(0.2);
var xAxis = svg.append("g")
  .attr("transform", "translate(0," + height + ")")



// Initialize the Y axis
var y = d3.scaleLinear()
  .range([ height, 0]);
var yAxis = svg.append("g")
  .attr("class", "myYaxis")

//global variable
var newyear;

// A function that create / update the plot for a given variable:
function update(selectedVar) {

    d3.csv("Data/cleaned/cleanRefugeeByAsylum.csv", function(mydata) {

        mydata.forEach(function(d) {
            d['2009'] = +d['2009']
            d['2010'] = +d['2010']
            d['2011'] = +d['2011']
            d['2012'] = +d['2012']
            d['2013'] = +d['2013']
            d['2014'] = +d['2014']
            d['2015'] = +d['2015']
            d['2016'] = +d['2016']
            d['2017'] = +d['2017']
            d['2018'] = +d['2018']
            d['2019'] = +d['2019']
        });

        newyear = d3.select('#year-select').property('value')
            
        //tooltip
        var tip = d3.tip()
          .attr('class', 'd3-tip')
          .offset([-10,0])
          .html(function(d) {
              var text = "<strong>Country:</strong> <span style='color: #EA396C;'>" + d.Country + "</span><br>";
              text += "<strong>Year:</strong> <span style='color: #EA396C;'>" + newyear + "</span><br>";
              text += "<strong>Value:</strong> <span style='color: #EA396C;'>" + d3.format(",.0f")(d[newyear]) + "</span><br>";

              return text; 
          });

        svg.call(tip); 

        //X Axis
        x.domain(mydata.map(function(d) { return d.Country; }))
        xAxis.transition().duration(700).call(d3.axisBottom(x))
            .selectAll('text')
                .style('text-anchor', 'end')
                .attr('transform', 'rotate(-30)');

        //Y Axis
        y.domain([0, d3.max(mydata, function(d) { return +d[selectedVar] }) ]);
        yAxis.transition().duration(700).call(d3.axisLeft(y));

        // variable bar: map data to existing bars
        var bar = svg.selectAll("rect")
          .data(mydata)
      
        // update bars
        bar
            .enter()
            .append("rect")
                .on('mouseover', tip.show)
                .on('mouseout', tip.hide)
            .merge(bar)
            .transition()
            .duration(700)
                .attr("x", function(d) { return x(d.Country); })
                .attr("y", function(d) { return y(d[selectedVar]); })
                .attr("width", x.bandwidth())
                .attr("height", function(d) { return height - y(d[selectedVar]); })
                .attr("fill", "#62C8F9")
                
      }); //d3 csv

  };// update function

//Initialize Plot
update('2009');

$('#year-select')
  .on('change', function() {
    update(newyear)
  });

