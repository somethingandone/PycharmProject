package com.nju.demo.DTO;

import lombok.Data;

import java.math.BigDecimal;

@Data
public class YearChartDTO {
    int year;
    int month;
    BigDecimal amount;

    public YearChartDTO(int year, int month, BigDecimal amount) {
        this.year = year;
        this.month = month;
        this.amount = amount;
    }
}
