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
@Table(name = "dm_v_tr_sdrq_mx")
public class dm_v_tr_sdrq_mx extends Data_mx {
    @Id
    private String uid;
    private String hosehldNo;
    private String acctNo;
    private String custName;
    private String tranType;
    private String tranDate;
    @Column(name = "tran_amt_fen")
    private BigDecimal tranAmt;
    private String channelFlg;
    private String tranOrg;
    private String tranTellerNo;
    private String tranLogNo;
    private String batchNo;
    private String tranSts;
    private String returnMsg;
    private String etlDt;
}
