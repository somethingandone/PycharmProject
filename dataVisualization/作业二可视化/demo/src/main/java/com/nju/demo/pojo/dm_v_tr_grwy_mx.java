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
@Table(name = "dm_v_tr_grwy_mx")
public class dm_v_tr_grwy_mx extends Data_mx {
    @Id
    private String uid;
    private String mchChannel;
    private String loginType;
    private String ebankCustNo;
    private String tranDate;
    private String tranTime;
    private String tranCode;
    private String tranSts;
    private String returnCode;
    private String returnMsg;
    private String sysType;
    private String payerAcctNo;
    private String payerAcctName;
    private String payeeAcctNo;
    private String payeeAcctName;
    private BigDecimal tranAmt;
    private String etlDt;

}
