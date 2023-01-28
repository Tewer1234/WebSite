$.ajaxSetup({
    headers: { 'X-CSRFToken': csrf_token },
    type: 'POST',
});

$(document).ready(function(){
    $.ajax({
        url: '/web_tool/readCSV/', 
        success: function(response){ 
            da = JSON.parse(response.message);
            window.alert("Success");
            console.log(da);
            var size = [], type = [], dd=[];
            for (var i=0;i<Object.keys(da).length;i++){
                // console.log(da[i]["Length"]);
                size.push(da[i]["End"] - da[i]["Start"]+1);
                type.push(da[i]["Type"]);
            }

            // for (var i=0;i<size.length;i++){

            // }
            console.log(size);
            for (var i=0;i<size.length;i++){
                dd.push({"Type":type[i],"Length":size[i]});
            }
            console.log(dd);

            const stack = d3.stack().keys(["Type"]);

            const stackSeries = stack(dd);
            console.log(stackSeries);


            // const colorScale = d3.scaleOrdinal()
            //     .domain(["five_prime_UTR","exon","intron","three_prime_UTR"])
            //     .range(["orange","yellow","gray","gray"]);
            
            //     for (var i=0;i<Object.keys(stackSeries).length;i++){
            //         console.log(stackSeries[i][0].data.Type);
            //         console.log(stackSeries[i][1].data.Start);
            //         console.log(stackSeries[i][2].data.End);
            //     }
            // // // var xScale = d3.scaleBand().range([0, width]).padding(0.5),
            // // //     yScale = d3.scaleLinear().range([height, 0]);
            
            // const g = d3.select('svg')
            //     .attr('width', 3000)
            //     .selectAll('g')
            //     .data(stackSeries)
            //     .enter()
            //     .append('g')
            //     .attr('fill', d => colorScale(d.key));
            // console.log(g);
            // 繪製長條圖
            // g.selectAll('rect')
            // .data(d=>d)
            // .join('rect')
            // .attr('width', function (d){
            //     var width = d;
            //     return d;
            //  });
             // 長度為終點值減掉起始值
            // .attr('x', d => d.data.Start) // x 座標設定為起始值
            // .attr('y', (d, i) => i *30) 
        },error: function(){
            window.alert("Wrong");
        }
    });
});
