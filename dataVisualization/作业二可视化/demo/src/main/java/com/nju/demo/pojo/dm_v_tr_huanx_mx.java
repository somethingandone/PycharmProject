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
@Table(name = "dm_v_tr_huanx_mx")
public class dm_v_tr_huanx_mx extends Data_mx {
    @Id
    private String uid;
    private String tranFlag;
    private String custName;
    private String acctNo;
    private String tranDate;
    private String tranTime;
    private BigDecimal tranAmt;
    private BigDecimal cacIntcPr;
    private String tranCode;
    private String drCrCode;
    private Integer payTerm;
    private String tranTellerNo;
    private String intcStrtDate;
    private String intcEndDate;
    private BigDecimal intr;
    private String tranLogNo;
    private String tranType;
    private String dscrpCode;
    private String etlDt;
}
