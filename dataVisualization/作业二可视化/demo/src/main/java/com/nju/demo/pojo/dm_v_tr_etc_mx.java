package com.nju.demo.pojo;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;
import lombok.experimental.Accessors;

import java.math.BigDecimal;

@Data
@Entity
@Accessors(chain = true)
@Table(name = "dm_v_tr_etc_mx")
public class dm_v_tr_etc_mx extends Data_mx {
    @Id
    private String uid;
    private String etcAcct;
    private String cardNo;
    private String carNo;
    private String custName;
    private String tranDate;
    private String tranTime;
    private BigDecimal tranAmtFen;
    @Column(name = "real_amt")
    private BigDecimal tranAmt;
    private BigDecimal concesAmt;
    private String tranPlace;
    private String mobPhone;
    private String etlDt;
}
