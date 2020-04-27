"use strict";lastyear=document.querySelector(".no-hd .lastyear"),thisyear=document.querySelector(".no-hd .thisyear"),thismonth=document.querySelector(".no-hd .thismonth"),$.ajax({url:"/api/meetings/count/years/",dataType:"json",data:{},success:function(e){data=e,lastyear.innerHTML=data.lastyear,thisyear.innerHTML=data.thisyear,thismonth.innerHTML=data.thismonth}}),$.ajax({url:"/api/meetings/count/everymonth/thisyear/",dataType:"json",data:{},success:function(e){data=e,console.log(data),function(e){var a=echarts.init(document.querySelector(".bar .chart")),t={color:["#2f89cf"],tooltip:{trigger:"axis",axisPointer:{type:"shadow"}},grid:{top:"10%",left:"10px",right:"0%",bottom:"4%",containLabel:!0},xAxis:[{type:"category",data:e.categories,axisTick:{alignWithLabel:!0},axisLabel:{color:"rgba(255,255,255,.6)",fontSize:"12px"},axisLine:{show:!1}}],yAxis:[{type:"value",axisLabel:{color:"rgba(255,255,255,.6)",fontSize:"12px"},axisLine:{lineStyle:{color:"rgba(255,255,255,.1)",width:2}},splitLine:{lineStyle:{color:"rgba(255,255,255,.1)"}}}],series:[{name:"部级会议",type:"bar",barWidth:"35%",stack:"会议",data:e.level1,itemStyle:{normal:{color:"rgba(0,123,255, 0.8)"}},label:{show:!1,position:"inside",distance:20,verticalAlign:"middle",textStyle:{color:"white",fontSize:14}}},{name:"省级会议",type:"bar",barWidth:"35%",stack:"会议",data:e.level2,itemStyle:{normal:{color:"rgba(161,47,47, 0.8)"}},label:{show:!1,position:"inside",distance:1,verticalAlign:"middle",textStyle:{color:"white",fontSize:14}}},{name:"市级会议",type:"bar",barWidth:"35%",stack:"会议",data:e.level3,itemStyle:{normal:{color:"rgba(64,116,52, 0.8)"}},label:{show:!1,position:"inside",distance:1,verticalAlign:"middle",textStyle:{color:"white",fontSize:14}}},{name:"会议汇总",type:"line",barWidth:"35%",data:e.data,itemStyle:{barBorderRadius:5,normal:{color:"#548dd5"}},label:{show:!0,position:"top",distance:10,verticalAlign:"middle",textStyle:{color:"white",fontSize:14}}}]};a.setOption(t),window.addEventListener("resize",function(){a.resize()}),a.getZr().on("click",function(e){var t=[e.offsetX,e.offsetY];a.containPixel("grid",t)&&function(e){dt=new Date;var t=dt.getFullYear();date=new Date(t,e,1),gotoDate(date)}(a.convertFromPixel({seriesIndex:0},[e.offsetX,e.offsetY])[0])})}(data)}}),$.ajax({url:"/api/meetings/count/everymonth/lastyear/",dataType:"json",data:{},success:function(e){data=e,console.log(data),function(e){var a=echarts.init(document.querySelector(".line .chart")),t={color:["#2f89cf"],tooltip:{trigger:"axis",axisPointer:{type:"shadow"}},grid:{top:"10%",left:"10px",right:"0%",bottom:"4%",containLabel:!0},xAxis:[{type:"category",data:e.categories,axisTick:{alignWithLabel:!0},axisLabel:{color:"rgba(255,255,255,.6)",fontSize:"12px"},axisLine:{show:!1}}],yAxis:[{type:"value",axisLabel:{color:"rgba(255,255,255,.6)",fontSize:"12px"},axisLine:{lineStyle:{color:"rgba(255,255,255,.1)",width:2}},splitLine:{lineStyle:{color:"rgba(255,255,255,.1)"}}}],series:[{name:"部级会议",type:"bar",barWidth:"40%",stack:"会议",data:e.level1,itemStyle:{normal:{color:"rgba(0,123,255, 0.8)"}}},{name:"省级会议",type:"bar",barWidth:"40%",stack:"会议",data:e.level2,itemStyle:{normal:{color:"rgba(161,47,47, 0.8)"}}},{name:"市级会议",type:"bar",barWidth:"40%",stack:"会议",data:e.level3,itemStyle:{normal:{color:"rgba(64,116,52, 0.8)"}}},{name:"会议汇总",type:"line",barWidth:"40%",data:e.data,itemStyle:{barBorderRadius:5,normal:{color:"#548dd5"}},label:{show:!0,position:"top",distance:10,verticalAlign:"middle",textStyle:{color:"white",fontSize:14}}}]};a.setOption(t),window.addEventListener("resize",function(){a.resize()}),a.getZr().on("click",function(e){var t=[e.offsetX,e.offsetY];a.containPixel("grid",t)&&function(e){dt=new Date;var t=dt.getFullYear();date=new Date(t-1,e,1),gotoDate(date)}(a.convertFromPixel({seriesIndex:0},[e.offsetX,e.offsetY])[0])})}(data)}}),$.ajax({url:"/api/meetings/count/offices/thisyear/",dataType:"json",data:{},success:function(e){data=e,console.log(data),function(e){var t=echarts.init(document.querySelector(".officepie .chart"));option={tooltip:{trigger:"item",formatter:"{a} <br/>{b} : {c} ({d}%)"},series:[{type:"pie",radius:"85%",center:["50%","50%"],selectedMode:"single",data:e,emphasis:{itemStyle:{shadowBlur:10,shadowOffsetX:0,shadowColor:"rgba(0, 0, 0, 0.5)"}}}]},t.setOption(option),window.addEventListener("resize",function(){t.resize()})}(data)}}),$.ajax({url:"/api/meetings/count/offices/lastyear/",dataType:"json",data:{},success:function(e){data=e,console.log(data),function(e){var t=echarts.init(document.querySelector(".officepielast .chart"));option={tooltip:{trigger:"item",formatter:"{a} <br/>{b} : {c} ({d}%)"},series:[{type:"pie",radius:"85%",center:["50%","50%"],selectedMode:"single",data:e,emphasis:{itemStyle:{shadowBlur:10,shadowOffsetX:0,shadowColor:"rgba(0, 0, 0, 0.5)"}}}]},t.setOption(option),window.addEventListener("resize",function(){t.resize()})}(data)}});