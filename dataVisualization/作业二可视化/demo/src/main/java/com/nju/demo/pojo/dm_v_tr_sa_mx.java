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
@Table(name = "dm_v_tr_sa_mx")
public class dm_v_tr_sa_mx extends Data_mx {
    @Id
    private String uid;
    private String cardNo;
    private String custName;
    private String acctNo;
    private Integer detN;
    private String currType;
    private String tranTellerNo;
    private BigDecimal crAmt;
    private BigDecimal bal;
    private BigDecimal tranAmt;
    private String tranCardNo;
    private String tranType;
    private String tranLogNo;
    private BigDecimal drAmt;
    private String openOrg;
    private String dscrpCode;
    private String remark;
    private String tranTime;
    private String tranDate;
    private String sysDate;
    private String tranCode;
    private String remark_1;
    private String oppoCustName;
    private String agtCertType;
    private String agtCertNo;
    private String agtCustName;
    private String channelFlag;
    private String oppoAcctNo;
    private String oppoBankNo;
    private String srcDt;
    private String etlDt;
}
