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
@Table(name = "dm_v_tr_dsf_mx")
public class dm_v_tr_dsf_mx extends Data_mx {
    @Id
    private String uid;
    private String tranDate;
    private String tranLogNo;
    private String tranCode;
    private String channelFlg;
    private String tranOrg;
    private String tranTellerNo;
    private String dcFlag;
    private BigDecimal tranAmt;
    private String sendBank;
    private String payerOpenBank;
    private String payerAcctNo;
    private String payerName;
    private String payeeOpenBank;
    private String payeeAcctNo;
    private String payeeName;
    private String tranSts;
    private String busiType;
    private String busiSubType;
    private String etlDt;
}
