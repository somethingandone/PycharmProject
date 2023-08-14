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
@Table(name = "dm_v_tr_sbyb_mx")
public class dm_v_tr_sbyb_mx extends Data_mx {
    @Id
    private String uid;
    private String custName;
    private String tranDate;
    private String tranSts;
    private String tranOrg;
    private String tranTellerNo;
    @Column(name = "tran_amt_fen")
    private BigDecimal tranAmt;
    private String tranType;
    private String returnMsg;
    private String etlDt;
}
