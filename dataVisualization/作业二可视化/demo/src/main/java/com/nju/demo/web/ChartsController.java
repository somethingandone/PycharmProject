package com.nju.demo.web;

import com.nju.demo.ChartData;
import com.nju.demo.RankData;
import com.nju.demo.service.ChartsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/charts")
public class ChartsController {

//    ChartData yearChart = new ChartData();
//    ChartData monthChart = new ChartData();
//    List<UserAmtDTO> topUsers = new ArrayList<>();

    @Autowired
    ChartsService chartsService;
    @GetMapping()
    public String charts() {return "chartsTest";}

//    @ModelAttribute(name = "yearChart")
//    public ChartData getYearChart() {return yearChart;}
//
//    @ModelAttribute(name = "monthChart")
//    public ChartData getMonthChart() {return monthChart;}
//
//    @ModelAttribute(name = "topUsers")
//    public List<UserAmtDTO> getTopUsers() {return topUsers;}

    @GetMapping("all")
    public List<BigDecimal> getAll() {
        List<BigDecimal> allData = new ArrayList<>();
        allData.add(chartsService.getTotal("贷记卡"));
        allData.add(chartsService.getTotal("第三方"));
        allData.add(chartsService.getTotal("ETC"));
//        allData.add(chartsService.getTotal("个人网银"));
        allData.add(chartsService.getTotal("工资代发"));
        allData.add(chartsService.getTotal("贷款还本"));
        allData.add(chartsService.getTotal("贷款还息"));
//        allData.add(chartsService.getTotal("活期"));
        allData.add(chartsService.getTotal("社保医保"));
//        allData.add(chartsService.getTotal("水电燃气"));
        allData.add(chartsService.getTotal("商户交易"));
        allData.add(chartsService.getTotal("手机银行"));
        return allData;
    }

    @GetMapping("year")
    public ChartData updateYearChart(@RequestParam String type, @RequestParam int year) {
        return chartsService.getYearChart(type, year);
    }

    @GetMapping("month")
    public ChartData updateMonthChart(@RequestParam String type, @RequestParam int year, @RequestParam int month) {
        return chartsService.getMonthChart(type, year, month);
    }

    @GetMapping("rank")
    public RankData sendRank(@RequestParam String type, @RequestParam String date) {
        return chartsService.getTop5UsersAtDay(type, date);
    }
}
