(function () {
    var myChart = echarts.init(document.querySelector('.bar .chart'));

    var option = {
        color: ['#2f89cf'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        grid: {
            top: '10%',
            left: '10px',
            right: '0%',
            bottom: '4%',
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                axisTick: {
                    alignWithLabel: true
                },
                axisLabel: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: "12px"

                },
                axisLine: {
                    show: false
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                axisLabel: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: "12px"
                },
                axisLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                        width: 2
                    }
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)"
                    }

                }
            }


        ],
        series: [
            {
                name: '直接访问',
                type: 'bar',
                barWidth: '35%',
                data: [10, 52, 200, 334, 390, 330, 220],
                itemStyle: {
                    barBorderRadius: 5,
                }
            }
        ]
    };


    myChart.setOption(option);
    window.addEventListener('resize', function(){
        myChart.resize();
    });

})();

