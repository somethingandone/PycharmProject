package com.nju.demo.DTO;

import lombok.Data;

import java.math.BigDecimal;

@Data
public class UserAmtDTO {
    String uid;
    String name;
    String date;
    BigDecimal amount;

    public UserAmtDTO(String uid, String name, String date, BigDecimal amount) {
        this.uid = uid;
        this.name = name;
        this.date = date;
        this.amount = amount;
    }

    @Override
    public String toString() {
        return "UserAmtDTO{" +
                "uid='" + uid + '\'' +
                ", name='" + name + '\'' +
                ", date='" + date + '\'' +
                ", amount=" + amount +
                '}';
    }
}
