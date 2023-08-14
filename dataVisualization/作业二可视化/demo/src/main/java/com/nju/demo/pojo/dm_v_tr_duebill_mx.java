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
@Table(name = "dm_v_tr_duebill_mx")
public class dm_v_tr_duebill_mx extends Data_mx {
    @Id
    private String uid;
    private String acctNo;
    private String receiptNo;
    private String contractNo;
    private String subjectNo;
    private String custNo;
    private String loanCustNo;
    private String custName;
    private String bussType;
    private String currType;
    @Column(name = "buss_amt")
    private BigDecimal tranAmt;
    private String putoutDate;
    private String matuDate;
    private String actuMatuDate;
    private BigDecimal bussRate;
    private BigDecimal actuBussRate;
    private String intrType;
    private String intrCyc;
    private Integer payTimes;
    private String payCyc;
    private Integer extendTimes;
    private BigDecimal bal;
    private BigDecimal normBal;
    private BigDecimal dlayAmt;
    private BigDecimal dullAmt;
    private BigDecimal badDebtAmt;
    private BigDecimal owedIntIn;
    private BigDecimal owedIntOut;
    private BigDecimal finePrInt;
    private BigDecimal fineIntrInt;
    private Integer dlayDays;
    private String payAcct;
    private String putoutAcct;
    private String payBackAcct;
    private Integer dueIntrDays;
    private String operateOrg;
    private String operator;
    private String regOrg;
    private String register;
    private String occurDate;
    private String loanUse;
    private String payType;
    private String payFreq;
    private String vouchType;
    private String mgrNo;
    private String mgeOrg;
    private String loanChannel;
    private String tenClass;
    private String srcDt;
    private String etlDt;
}
