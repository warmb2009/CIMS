(function(){
    lastyear = document.querySelector('.no-hd .lastyear');
    thisyear = document.querySelector('.no-hd .thisyear');

    $.ajax({
        url: 'http://127.0.0.1:8000/api/meetings/count/years/',
        dataType: 'json',
        data: {},
        success: function (json) { // 获取当前数据
            data = json;
            lastyear.innerHTML = data.lastyear;
            thisyear.innerHTML = data.thisyear;
        }
    });

})();

//今年的柱状图
(function () {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/meetings/count/everymonth/thisyear/',
        dataType: 'json',
        data: {},
        success: function (json) { // 获取当前数据
            data = json;
            console.log(data)
            generateChart(data);
        }
    });

    function generateChart(data) {
        //基于准备好的DOM，初始化echarts实例
        var myChart = echarts.init(document.querySelector('.bar .chart'));

        //指定图表的配置项和数据
        //myChart.clear();

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
                    data: data.categories,
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
                    name: '会议数量',
                    type: 'bar',
                    barWidth: '35%',
                    //categories:data.categories,
                    data: data.data,
                    itemStyle: {
                        barBorderRadius: 5,
                    },
                    label: {
                        show: true, // 开启显示
                        //rotate: 70, // 旋转70度
                        position: 'top', // 在上方显示
                        distance: 20, // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。
                        verticalAlign: 'middle',
                        textStyle: { // 数值样式
                            color: 'white',
                            fontSize: 14
                        }
                    }
                }

            ]
        };

        //使用刚指定的配置项和数据显示图表
        myChart.setOption(option);
        window.addEventListener('resize', function () {
            myChart.resize();
        });

        myChart.on('click', function(params) {
            dt = new Date();
            var y = dt.getFullYear();

            date = new Date(y,params.dataIndex,1)
            document.getElementById('calendar').gotoDate(date);            
        });

        
    }
})();

//去年的柱状图
(function () {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/meetings/count/everymonth/lastyear/',
        dataType: 'json',
        data: {},
        success: function (json) { // 获取当前数据
            data = json;
            console.log(data)
            generateChart(data);
        }
    });

    function generateChart(data) {
        //基于准备好的DOM，初始化echarts实例
        var myChart = echarts.init(document.querySelector('.line .chart'));

        //指定图表的配置项和数据
        //myChart.clear();

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
                    data: data.categories,
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
                    name: '会议数量',
                    type: 'bar',
                    barWidth: '35%',
                    //categories:data.categories,
                    data: data.data,
                    itemStyle: {
                        barBorderRadius: 5,
                    },
                    label: {
                        show: true, // 开启显示
                        //rotate: 70, // 旋转70度
                        position: 'top', // 在上方显示
                        distance: 20, // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。
                        verticalAlign: 'middle',
                        textStyle: { // 数值样式
                            color: 'white',
                            fontSize: 14
                        }
                    }
                }
            ]
        };

        //使用刚指定的配置项和数据显示图表
        myChart.setOption(option);
        window.addEventListener('resize', function () {
            myChart.resize();
        });
        myChart.on('click', function(params) {
            //console.log(params); 
            dt = new Date();
            var y = dt.getFullYear();

            date = new Date(y-1,params.dataIndex,1)
            a = $('#calendar')//.gotoDate(date);
            console.log(a);
            a.gotoDate(date);
            //a.fullCalendar('gotoDate', date)
            //$('#calendar').fullCalendar('option', 'firstDay', 0);



        });
    }
})();