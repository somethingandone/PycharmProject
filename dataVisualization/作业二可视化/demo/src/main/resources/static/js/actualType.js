let type = cookieKeyGetValue('type');
let year;
let month;
let day
console.log(type);
document.getElementById('title').innerHTML = type;

// 折线图模块1
var myYearChart = echarts.init(document.querySelector(".line .chart"));
(function () {
    // 年份对应数据
    var yearData = [{
        year: "2021", // 年份
        data: []
    },
    {
        year: "2022", // 年份
        data: []
    }
    ];

    $.ajax({
        type: 'GET',
        url: 'http://localhost:8080/charts/year',
        data: {
            type: type,
            year: 2021
        },
        success: function (data) {
            console.log(data.amounts);
            yearData[0].data = data.amounts;
        }
    })

    $.ajax({
        type: 'GET',
        url: 'http://localhost:8080/charts/year',
        data: {
            type: type,
            year: 2022
        },
        success: function (data) {
            console.log(data.amounts);
            yearData[1].data = data.amounts;
        }
    })



    var option = {
        // 修改两条线的颜色
        color: ['#00f2f1', '#ed3f35'],
        tooltip: {
            trigger: 'axis'
        },
        // 图例组件
        legend: {
            // 当serise 有name值时， legend 不需要写data
            // 修改图例组件文字颜色
            textStyle: {
                color: '#4c9bfd'
            },
            right: '10%',
        },
        grid: {
            top: "20%",
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true,
            show: true, // 显示边框
            borderColor: '#012f4a' // 边框颜色
        },
        xAxis: {
            type: 'category',
            boundaryGap: false, // 去除轴间距
            data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
            // 去除刻度线
            axisTick: {
                show: false
            },
            axisLabel: {
                color: "#4c9bfb" // x轴文本颜色
            },
            axisLine: {
                show: false // 去除轴线
            }
        },
        yAxis: {
            type: 'value',
            // 去除刻度线
            axisTick: {
                show: false
            },
            axisLabel: {
                color: "#4c9bfb" // x轴文本颜色
            },
            axisLine: {
                show: false // 去除轴线
            },
            splitLine: {
                lineStyle: {
                    color: "#012f4a"
                }
            }
        },
        series: [{
            type: 'line',
            smooth: true, // 圆滑的线
            name: '交易金额',
            data: yearData[0].data
        }
        ]
    };

    console.log(option.series);
    myYearChart.setOption(option);

    // 4.让图表随屏幕自适应
    window.addEventListener('resize', function () {
        myYearChart.resize();
    })

    // 5.点击切换2020 和 2021 的数据
    $('.line h2 a').on('click', function () {
        // console.log($(this).index());
        // 点击a 之后 根据当前a的索引号 找到对应的 yearData 相关对象
        // console.log(yearData[$(this).index()]);
        var obj = yearData[$(this).index()];
        year = obj.year;
        option.series[0].data = obj.data;
        // 选中年份高亮
        $('.line h2 a').removeClass('a-active');
        $(this).addClass('a-active');

        // 需要重新渲染
        myYearChart.setOption(option);
    })
})();


// 折线图模块2
var myMonthChart = echarts.init(document.querySelector('.line2 .chart'));
(function () {

    var option = {
        tooltip: {
            trigger: 'axis',
        },
        legend: {
            top: "0%",
            textStyle: {
                color: "rgba(255,255,255,.5)",
                fontSize: "12"
            }
        },
        grid: {
            top: '30',
            left: '10',
            right: '30',
            bottom: '10',
            containLabel: true
        },
        xAxis: [{
            type: 'category',
            boundaryGap: false,
            // 文本颜色为rgba(255,255,255,.6)  文字大小为 12
            axisLabel: {
                textStyle: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: 12
                }
            },
            // x轴线的颜色为   rgba(255,255,255,.2)
            axisLine: {
                lineStyle: {
                    color: "rgba(255,255,255,.2)"
                }
            },
            data: []
        }],
        yAxis: [{
            type: 'value',
            axisTick: {
                // 不显示刻度线
                show: false
            },
            axisLine: {
                lineStyle: {
                    color: "rgba(255,255,255,.1)"
                }
            },
            axisLabel: {
                textStyle: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: 12
                }
            },
            // 修改分割线的颜色
            splitLine: {
                lineStyle: {
                    color: "rgba(255,255,255,.1)"
                }
            }
        }],
        series: [{
            name: '交易金额',
            type: 'line',
            smooth: true, // 圆滑的线
            // 单独修改当前线条的样式
            lineStyle: {
                color: "#0184d5",
                width: 2
            },
            // 填充区域渐变透明颜色
            areaStyle: {
                color: new echarts.graphic.LinearGradient(
                    0,
                    0,
                    0,
                    1,
                    [{
                        offset: 0,
                        color: "rgba(1, 132, 213, 0.4)" // 渐变色的起始颜色
                    },
                        {
                            offset: 0.8,
                            color: "rgba(1, 132, 213, 0.1)" // 渐变线的结束颜色
                        }
                    ],
                    false
                ),
                shadowColor: "rgba(0, 0, 0, 0.1)"
            },
            // 拐点设置为小圆点
            symbol: 'circle',
            // 设置拐点大小
            symbolSize: 5,
            // 开始不显示拐点， 鼠标经过显示
            showSymbol: false,
            // 设置拐点颜色以及边框
            itemStyle: {
                color: "#0184d5",
                borderColor: "rgba(221, 220, 107, .1)",
                borderWidth: 12
            },
            data: []
        }
        ]
    };

    // myChart.setOption(option);

    window.addEventListener('resize', function () {
        myMonthChart.resize();
    })

    myYearChart.on('click', function (params) {
        month = params.name;
        console.log(month);
        $.ajax({
            type: 'GET',
            url: 'http://localhost:8080/charts/month',
            data: {
                type: type,
                year: year,
                month: month
            },
            success: function (data) {
                option.xAxis[0].data = data.indexList;
                option.series[0].data = data.amounts;
                myMonthChart.setOption(option);
            }
        })
        console.log(option);
        // myMonthChart.setOption(option);
        document.getElementById('actual-month').innerHTML = year + '-' + month;
    })
})();

// 柱状图模块2
var myRankChart = echarts.init(document.querySelector(".bar2 .chart"));
(function () {

    // 声明颜色数组
    var myColor = ["#1089E7", "#F57474", "#56D0E3", "#F8B448", "#8B78F6"];
    // 2.指定配置项和数据
    var option = {
        grid: {
            top: "10%",
            left: '22%',
            bottom: '10%',
            // containLabel: true
        },
        xAxis: {
            // 不显示x轴相关信息
            show: false
        },
        yAxis: [{
            type: 'category',
            // y轴数据反转，与数组的顺序一致
            inverse: true,
            // 不显示y轴线和刻度
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            // 将刻度标签文字设置为白色
            axisLabel: {
                color: "#fff"
            },
            data: []
        }, {
            // y轴数据反转，与数组的顺序一致
            inverse: true,
            show: true,
            // 不显示y轴线和刻度
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            // 将刻度标签文字设置为白色
            axisLabel: {
                color: "#fff"
            },
            data: []
        }],
        series: [{
            // 第一组柱子（条状）
            name: '条',
            type: 'bar',
            // 柱子之间的距离
            barCategoryGap: 50,
            // 柱子的宽度
            barWidth: 10,
            // 层级 相当于z-index
            yAxisIndex: 0,
            // 柱子更改样式
            itemStyle: {
                barBorderRadius: 20,
                // 此时的color可以修改柱子的颜色
                color: function (params) {
                    // params 传进来的是柱子的对象
                    // dataIndex 是当前柱子的索引号
                    // console.log(params);
                    return myColor[params.dataIndex];
                }
            },
            data: [],
            // 显示柱子内的百分比文字
            label: {
                show: true,
                position: "inside",
                // {c} 会自动解析为数据（data内的数据）
                formatter: "{c}%"
            }
        },
            {
                // 第二组柱子（框状 border）
                name: '框',
                type: 'bar',
                // 柱子之间的距离
                barCategoryGap: 50,
                // 柱子的宽度
                barWidth: 14,
                // 层级 相当于z-index
                yAxisIndex: 1,
                // 柱子修改样式
                itemStyle: {
                    color: "none",
                    borderColor: "#00c1de",
                    borderWidth: 2,
                    barBorderRadius: 15,
                },
                data: [100, 100, 100, 100, 100]
            }
        ]
    };
    // 3.把配置项给实例对象
    // myRankChart.setOption(option);

    // 4.让图表随屏幕自适应
    window.addEventListener('resize', function () {
        myRankChart.resize();
    })

    myMonthChart.on('click', function (params) {
        day = params.name;
        let date = getDateStr(year, month, day);
        $.ajax({
            type: 'GET',
            url: 'http://localhost:8080/charts/rank',
            data: {
                type: type,
                date: date
            },
            success: function (data) {
                console.log('succeed');
                option.yAxis[0].data = data.names;
                option.yAxis[1].data = data.amounts;
                option.series[0].data = data.percents;
                myRankChart.setOption(option);
            },
            error: function () {
                console.log('failed');
            }

        })

        // myRankChart.setOption(option);
        document.getElementById('rank-date').innerHTML = date;
    })
})();

function getDateStr(year, month, day) {
    if (month < 10) {
        month = '0' + month;
    }
    if (day < 10) {
        day = '0' + day;
    }
    return year + '-' + month + '-' + day;
}

