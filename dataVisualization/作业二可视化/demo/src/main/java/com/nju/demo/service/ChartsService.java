package com.nju.demo.service;

import com.nju.demo.ChartData;
import com.nju.demo.RankData;

import java.math.BigDecimal;

public interface ChartsService {

    BigDecimal getTotal(String type);

    RankData getTop5UsersAtDay(String type, String date);

    ChartData getYearChart(String type, int year);

    ChartData getMonthChart(String type, int year, int month);


}
