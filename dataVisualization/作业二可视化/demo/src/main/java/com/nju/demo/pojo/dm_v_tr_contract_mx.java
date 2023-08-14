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
@Table(name = "dm_v_tr_contract_mx")
public class dm_v_tr_contract_mx {
    @Id
    private String uid;
    private String contractNo;
    private String applyNo;
    private String artificialNo;
    private String occurDate;
    private String loanCustNo;
    private String custName;
    private String bussType;
    private String occurType;
    private String isCreditCyc;
    private String currType;
    @Column(name = "buss_amt")
    private BigDecimal tranAmt;
    private BigDecimal loanPert;
    private int termYear;
    private int termMth;
    private int termDay;
    private String baseRateType;
    private BigDecimal baseRate;
    private String floatType;
    private BigDecimal rateFloat;
    private BigDecimal rate;
    private int payTimes;
    private String payType;
    private String direction;
    private String loanUse;
    private String paySource;
    private String putoutDate;
    private String matuDate;
    private String vouchType;
    private String isOthVouch;
    private String applyType;
    private int extendTimes;
    private BigDecimal actuOutAmt;
    private BigDecimal bal;
    private BigDecimal normBal;
    private BigDecimal dlayBal;
    private BigDecimal dullBal;
    private BigDecimal owedIntIn;
    private BigDecimal owedIntOut;
    private BigDecimal finePrInt;
    private BigDecimal fineIntrInt;
    private int dlayDays;
    private String fiveClass;
    private String classDate;
    private String mgeOrg;
    private String mgrNo;
    private String operateOrg;
    private String operator;
    private String operateDate;
    private String regOrg;
    private String register;
    private String regDate;
    private String inteSettleType;
    private String isBad;
    private BigDecimal frzAmt;
    private String conCrlType;
    private String shiftType;
    private int dueIntrDays;
    private String resonType;
    private BigDecimal shiftBal;
    private String isVcVouch;
    private String loanUseAdd;
    private String finshType;
    private String finshDate;
    private String stsFlag;
    private String srcDt;
    private String etlDt;

}
