package com.nju.demo.service.impl;

import com.nju.demo.ChartData;
import com.nju.demo.DTO.TotalDTO;
import com.nju.demo.DTO.UserAmtDTO;
import com.nju.demo.RankData;
import com.nju.demo.base.BaseRepository;
import com.nju.demo.repository.*;
import com.nju.demo.service.ChartsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

@Service
public class ChartsServiceImpl implements ChartsService {

    private String typeInfo;
    private BaseRepository repo;

    private void reset(String type) {
        switch (type) {
            case "贷记卡":
                typeInfo = "贷记卡交易";
                repo = djkRepo;
                break;
            case "第三方":
                typeInfo = "第三方交易";
                repo = dsfRepo;
                break;
            case "ETC":
                typeInfo = "ETC交易";
                repo = etcRepo;
                break;
            case "个人网银":
                typeInfo = "个人网银交易";
                repo = grwyRepo;
                break;
            case "工资代发":
                typeInfo = "工资代发明细";
                repo = gzdfRepo;
                break;
            case "贷款还本":
                typeInfo = "贷款还本明细";
                repo = huanbRepo;
                break;
            case "贷款还息":
                typeInfo = "贷款还息明细";
                repo = huanxRepo;
                break;
            case "活期":
                typeInfo = "活期交易";
                repo = saRepo;
                break;
            case "社保医保":
                typeInfo = "社保医保交易";
                repo = sbybRepo;
                break;
            case "水电燃气":
                typeInfo = "水电燃气交易";
                repo = sdrqRepo;
                break;
            case "商户交易":
                typeInfo = "商户交易明细";
                repo = shopRepo;
                break;
            case "手机银行":
                typeInfo = "手机银行交易";
                repo = sjyhRepo;
                break;
            default:
                System.err.println("未能识别交易类型: " + type);
                break;
        }
    }

    @Override
    public BigDecimal getTotal(String type) {
        reset(type);
        return repo.getTotal();
    }

    @Override
    public RankData getTop5UsersAtDay(String type, String date) {
        reset(type);
        List<UserAmtDTO> userAmtDTOS =  repo.getTop5Users(date);
        return userAmtDTO2RankData(userAmtDTOS);
    }

    @Override
    public ChartData getYearChart(String type, int year) {
        reset(type);
        ChartData yearChart = new ChartData(typeInfo);

        List<TotalDTO> dtos = object2TotalDTO(repo.getMonthTotal(year));
        yearChart.setAmounts(totalDTO2ListBD(dtos, 12));
        return yearChart;
    }

    @Override
    public ChartData getMonthChart(String type, int year, int month) {
        reset(type);
        ChartData monthChart = new ChartData(typeInfo);

        List<TotalDTO> dtos = object2TotalDTO(repo.getDayTotal(year, month));
        monthChart.setAmounts(totalDTO2ListBD(dtos, getDaysOfMonth(year, month)));
        return monthChart;
    }

    private RankData userAmtDTO2RankData(List<UserAmtDTO> userAmtDTOS) {
        List<String> names = new ArrayList<>();
        List<BigDecimal> amounts = new ArrayList<>();

        for (UserAmtDTO dto : userAmtDTOS) {
            names.add(dto.getName());
            amounts.add(dto.getAmount());
        }

        RankData res = new RankData(typeInfo, names);
        res.setAmounts(amounts);
        return res;
    }

    private List<TotalDTO> object2TotalDTO(List<Object[]> rows) {
        List<TotalDTO> res = new ArrayList<>();
        for (Object[] row : rows) {
            TotalDTO dto;
            if (row.length == 3) {
                int year = (int) row[0];
                short month = (short) row[1];
                BigDecimal amount = (BigDecimal) row[2];

                dto = new TotalDTO(year, month, amount);
            } else {
                String date = (String) row[0];
                BigDecimal amount = (BigDecimal) row[1];

                dto = new TotalDTO(date, amount);
            }

            res.add(dto);
        }
        return res;
    }

    private List<BigDecimal> totalDTO2ListBD(List<TotalDTO> dtos, int size) {
        List<BigDecimal> amounts = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            amounts.add(BigDecimal.valueOf(0));
        }

        for (TotalDTO dto : dtos) {
            String[] date = dto.getDate().split("-");
            int index = Integer.parseInt(date[date.length-1]) - 1;
            amounts.set(index, dto.getTotal());
        }

        return amounts;
    }

    private int getDaysOfMonth(int year, int month) {
        int[] days = {31, 28, 31, 30,
                31, 30, 31, 31,
                30, 31, 30, 31};
        if (year % 4 == 0)
            days[2] = 29;
        return days[month-1];
    }

    @Autowired
    ContractRepo contractRepo;
    @Autowired
    DjkRepo djkRepo;
    @Autowired
    DsfRepo dsfRepo;
    @Autowired
    DuebillRepo duebillRepo;
    @Autowired
    EtcRepo etcRepo;
    @Autowired
    GrwyRepo grwyRepo;
    @Autowired
    GzdfRepo gzdfRepo;
    @Autowired
    HuanbRepo huanbRepo;
    @Autowired
    HuanxRepo huanxRepo;
    @Autowired
    SaRepo saRepo;
    @Autowired
    SbybRepo sbybRepo;
    @Autowired
    SdrqRepo sdrqRepo;
    @Autowired
    ShopRepo shopRepo;
    @Autowired
    SjyhRepo sjyhRepo;
}
