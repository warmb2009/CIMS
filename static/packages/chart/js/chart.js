(function () {
    lastyear = document.querySelector('.no-hd .lastyear');
    thisyear = document.querySelector('.no-hd .thisyear');
    thismonth = document.querySelector('.no-hd .thismonth');
    $.ajax({
        url: '/api/meetings/count/years/',
        dataType: 'json',
        data: {},
        success: function (json) { // 获取当前数据
            
            data = json;
            lastyear.innerHTML = data.lastyear;
            thisyear.innerHTML = data.thisyear;
            thismonth.innerHTML = data.thismonth;
        }
    });
})();

//今年的柱状图
(function () {
    $.ajax({
        url: '/api/meetings/count/everymonth/thisyear/',
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
            //legend: {
            //data: ['部级会议', '省级会议', '市级会议']
            //},
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
                    name: '部级会议',
                    type: 'bar',
                    barWidth: '35%',
                    stack: '会议',
                    //categories:data.categories,
                    data: data.level1,
                    itemStyle: {
                        normal: {
                            color: 'rgba(0,123,255, 0.8)',
                        }
                    },
                    label: {
                        show: false, // 开启显示
                        //rotate: 70, // 旋转70度
                        position: 'inside', // 在上方显示
                        distance: 20, // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。
                        verticalAlign: 'middle',
                        textStyle: { // 数值样式
                            color: 'white',
                            fontSize: 14
                        }
                    }
                },
                {
                    name: '省级会议',
                    type: 'bar',
                    barWidth: '35%',
                    stack: '会议',
                    //categories:data.categories,
                    data: data.level2,
                    itemStyle: {
                        normal: {
                            //A12F2F
                            color: 'rgba(161,47,47, 0.8)',
                        }
                    },
                    label: {
                        show: false, // 开启显示
                        //rotate: 70, // 旋转70度
                        position: 'inside', // 在上方显示
                        distance: 1, // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。
                        verticalAlign: 'middle',
                        textStyle: { // 数值样式
                            color: 'white',
                            fontSize: 14
                        }
                    }
                },
                {
                    name: '市级会议',
                    type: 'bar',
                    barWidth: '35%',
                    stack: '会议',
                    //categories:data.categories,
                    data: data.level3,
                    itemStyle: {
                        normal: {
                            //407434
                            color: 'rgba(64,116,52, 0.8)',
                        }
                    },
                    label: {
                        show: false, // 开启显示
                        //rotate: 70, // 旋转70度
                        position: 'inside', // 在上方显示
                        distance: 1, // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。
                        verticalAlign: 'middle',
                        textStyle: { // 数值样式
                            color: 'white',
                            fontSize: 14
                        }
                    }
                },
                {
                    name: '会议汇总',
                    type: 'line',
                    barWidth: '35%',
                    //categories:data.categories,
                    data: data.data,
                    itemStyle: {
                        barBorderRadius: 5,
                        normal: { color: '#548dd5' }

                    },
                    label: {
                        show: true, // 开启显示
                        //rotate: 70, // 旋转70度
                        position: 'top', // 在上方显示
                        distance: 10, // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。
                        verticalAlign: 'middle',
                        textStyle: { // 数值样式
                            color: 'white',
                            fontSize: 14
                        }
                    }
                },
            ]
        };

        //使用刚指定的配置项和数据显示图表
        myChart.setOption(option);
        window.addEventListener('resize', function () {
            myChart.resize();
        });

        /*
        myChart.on('click', function (params) {
            dt = new Date();
            var y = dt.getFullYear();

            date = new Date(y - 1, params.dataIndex, 1)

            gotoDate(date);
        });
        */

        function gotoIndex(myIndex) {
            dt = new Date();
            var y = dt.getFullYear();
            date = new Date(y, myIndex, 1)
            gotoDate(date);
        }

        myChart.getZr().on('click', params => {
            let pointInPixel = [params.offsetX, params.offsetY]
            if (myChart.containPixel('grid', pointInPixel)) {
                let xIndex = myChart.convertFromPixel({ seriesIndex: 0 }, [params.offsetX, params.offsetY])[0]
                gotoIndex(xIndex);
            }
        })
    }
})();

//去年的柱状图
(function () {
    $.ajax({
        url: '/api/meetings/count/everymonth/lastyear/',
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
            //legend: {
            //    itemWidth: 23,
            //    itemHeight: 14,
            //    data: ['部级会议', '省级会议', '市级会议']
            //},
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
                    name: '部级会议',
                    type: 'bar',
                    barWidth: '40%',
                    stack: '会议',
                    //categories:data.categories,
                    data: data.level1,
                    itemStyle: {
                        normal: {
                            color: 'rgba(0,123,255, 0.8)',
                        }
                    },
                    //label: {
                    //    show: false, // 开启显示
                    //rotate: 70, // 旋转70度
                    //    position: 'inside', // 在上方显示
                    //distance: 20, // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。
                    //    verticalAlign: 'middle',
                    //    textStyle: { // 数值样式
                    //        color: 'white',
                    //        fontSize: 14
                    //    }
                    //}
                },
                {
                    name: '省级会议',
                    type: 'bar',
                    barWidth: '40%',
                    stack: '会议',

                    data: data.level2,
                    itemStyle: {
                        normal: {
                            //A12F2F
                            color: 'rgba(161,47,47, 0.8)',
                        }
                    },
                    //label: {
                    //    show: false, // 开启显示
                    //rotate: 70, // 旋转70度
                    //    position: 'inside', // 在上方显示
                    //distance: 1, // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。
                    //    verticalAlign: 'middle',
                    //    textStyle: { // 数值样式
                    //        color: 'white',
                    //        fontSize: 14
                    //    }
                    //}
                },
                {
                    name: '市级会议',
                    type: 'bar',
                    barWidth: '40%',
                    stack: '会议',

                    data: data.level3,
                    itemStyle: {
                        normal: {
                            //407434
                            color: 'rgba(64,116,52, 0.8)',
                        }
                    },
                    //label: {
                    //    show: false, // 开启显示
                    //rotate: 70, // 旋转70度
                    //    position: 'inside', // 在上方显示
                    //distance: 1, // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。
                    //    verticalAlign: 'middle',
                    //    textStyle: { // 数值样式
                    //        color: 'white',
                    //        fontSize: 14
                    //    }
                    //}
                },
                {
                    name: '会议汇总',
                    type: 'line',
                    barWidth: '40%',

                    data: data.data,
                    itemStyle: {
                        barBorderRadius: 5,
                        normal: { color: '#548dd5' }
                    },
                    label: {
                        show: true, // 开启显示
                        //rotate: 70, // 旋转70度
                        position: 'top', // 在上方显示
                        distance: 10, // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。
                        verticalAlign: 'middle',
                        textStyle: { // 数值样式
                            color: 'white',
                            fontSize: 14
                        }
                    }
                },
            ]
        };

        //使用刚指定的配置项和数据显示图表
        myChart.setOption(option);
        window.addEventListener('resize', function () {
            myChart.resize();
        });
        /*
        myChart.on('click', function (params) {
            //console.log(params); 
            dt = new Date();
            var y = dt.getFullYear();

            date = new Date(y - 1, params.dataIndex, 1)

            gotoDate(date);
        });
        */
        function gotoIndex(myIndex) {
            dt = new Date();
            var y = dt.getFullYear();
            date = new Date(y - 1, myIndex, 1)
            gotoDate(date);
        }

        myChart.getZr().on('click', params => {
            let pointInPixel = [params.offsetX, params.offsetY]
            if (myChart.containPixel('grid', pointInPixel)) {
                let xIndex = myChart.convertFromPixel({ seriesIndex: 0 }, [params.offsetX, params.offsetY])[0]
                gotoIndex(xIndex);
            }
        })
    }
})();


//今年各单位饼图
(function () {
    $.ajax({
        url: '/api/meetings/count/offices/thisyear/',
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
        var myChart = echarts.init(document.querySelector('.officepie .chart'));


        option = {
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b} : {c} ({d}%)'
            },

            series: [
                {
                    type: 'pie',
                    radius: '85%',
                    center: ['50%', '50%'],

                    selectedMode: 'single',
                    data: data,
                    emphasis: {
                        itemStyle: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
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
    }
})();


//去年各单位饼图
(function () {
    $.ajax({
        url: '/api/meetings/count/offices/lastyear/',
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
        var myChart = echarts.init(document.querySelector('.officepielast .chart'));


        option = {
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b} : {c} ({d}%)'
            },

            series: [
                {
                    type: 'pie',
                    radius: '85%',
                    center: ['50%', '50%'],
                    //roseType: 'radius',
                    selectedMode: 'single',
                    data: data,
                    emphasis: {
                        itemStyle: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    },
                    //label:{
                    //fontSize:10,
                    //},
                    //labelLine:{
                    //    length:2,
                    //    length2:4,
                    //},
                }
            ]

        };

        //使用刚指定的配置项和数据显示图表
        myChart.setOption(option);
        window.addEventListener('resize', function () {
            myChart.resize();
        });
    }
})();