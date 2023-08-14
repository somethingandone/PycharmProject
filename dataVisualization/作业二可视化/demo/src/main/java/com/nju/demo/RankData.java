package com.nju.demo;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.List;

public class RankData {

    String type;
    List<String> names = new ArrayList<>();

    List<BigDecimal> amounts = new ArrayList<>();

    List<BigDecimal> percents = new ArrayList<>();

    public RankData(String type, List<String> names) {
        this.type = type;
        this.names = names;
    }

    public void setAmounts(List<BigDecimal> amounts) {
        this.amounts = amounts;
        BigDecimal max = amounts.get(0);

        for (BigDecimal amount : amounts) {
            BigDecimal res = amount.divide(max, 4, RoundingMode.HALF_UP);
            percents.add(res.multiply(new BigDecimal(100)));
        }
    }

    public String getType() {
        return type;
    }

    public List<String> getNames() {
        return names;
    }

    public List<BigDecimal> getAmounts() {
        return amounts;
    }

    public List<BigDecimal> getPercents() {
        return percents;
    }
}
