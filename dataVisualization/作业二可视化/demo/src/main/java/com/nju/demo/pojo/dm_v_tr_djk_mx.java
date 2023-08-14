package com.nju.demo.pojo;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;
import lombok.experimental.Accessors;

import java.math.BigDecimal;

@Data
@Entity
@Accessors(chain = true)
@Table(name = "dm_v_tr_djk_mx")
public class dm_v_tr_djk_mx {
    @Id
    private String uid;
    private String cardNo;
    private String tranType;
    private String tranTypeDesc;
    private BigDecimal tranAmt;
    private String tranAmtSign;
    private String merType;
    private String merCode;
    private String revInd;
    private String tranDesc;
    private String tranDate;
    private String valDate;
    private String purDate;
    private String tranTime;
    private String acctNo;
    private String etlDt;
}
