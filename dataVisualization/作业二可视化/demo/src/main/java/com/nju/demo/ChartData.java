package com.nju.demo;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class ChartData {
    String type;
    int size = 0;
    List<Integer> indexList = new ArrayList<>();
    List<BigDecimal> amounts = new ArrayList<>();

    public ChartData() {
        type = "Invalid";
    }

    public ChartData(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public void setAmounts(List<BigDecimal> amounts) {
        this.amounts = amounts;
        this.size = amounts.size();
        for (int i = 0; i < size; i++) {
            indexList.add(i+1);
        }
    }

    public List<Integer> getIndexList() {
        return indexList;
    }

    public List<BigDecimal> getAmounts() {
        return amounts;
    }

    public int getSize() {
        return size;
    }
}
