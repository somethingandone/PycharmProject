package com.nju.demo.DTO;

import lombok.Data;

import java.math.BigDecimal;

@Data
public class TotalDTO {
    private String date;
    private BigDecimal total;

    public TotalDTO(String date, BigDecimal total) {
        this.date = date;
        this.total = total;
    }

    public TotalDTO(int year, short month, BigDecimal total) {
        this.date = year + "-" + month;
        this.total = total;
    }

    @Override
    public String toString() {
        return "TotalDTO{" +
                "date='" + date + '\'' +
                ", total=" + total +
                '}';
    }
}
