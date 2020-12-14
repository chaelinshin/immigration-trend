// set the dimensions and margins of the graph
var margin = {left:80, right:20, top:50, bottom:100};
var height = 500 - margin.top - margin.bottom,
    width = 800 - margin.left - margin.right; 

// append the svg object to the body of the page
var svg = d3.select("#mychart")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");


// Initialize an Y axis
var y = d3.scaleLinear().range([height, 0]);
var yAxis = d3.axisLeft().scale(y);
svg.append("g")
  .attr("class","myYaxis")


function update(selectedVar) {

  // Parse the Data
  d3.csv("Data/cleaned/cleanUSRefugeeAndPopulation.csv", function(mydata) {

    var year = d3.timeParse("%Y");

    mydata.forEach(function(d) {
      d.Year = year(d.Year);
    }); 

    // Initialize  X Axis:
    var x = d3.scaleTime()
      .domain(d3.extent(mydata, function(d) { return d.Year; }))
      .range([0, width]); 
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    // create the Y axis
    y.domain([0, d3.max(mydata, function(d) { return d[selectedVar]  }) ]);
    svg.selectAll(".myYaxis")
      .transition()
      .duration(1000)
      .call(yAxis);

    var line = svg.selectAll(".lineTest")
      .data([mydata], function(d) { return d.Year; });

    // update line chart
    line
      .enter()
      .append("path")
      .attr("class","lineTest")
      .merge(line)
      .transition()
      .duration(1000)
      .attr("d", d3.line()
        .x(function(d) { return x(d.Year); })
        .y(function(d) { return y(d[selectedVar]); }))
        .attr("fill", "none")
        .attr("stroke", "#8938EE")
        .attr("stroke-width", 3.5)
  });

};


// Initialize plot
update('Number')