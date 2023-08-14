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
@Table(name = "dm_v_tr_gzdf_mx")
public class dm_v_tr_gzdf_mx extends Data_mx {
    @Id
    private String uid;
    private String belongOrg;
    private String entAcct;
    private String entName;
    private String engCertNo;
    private String acctNo;
    private String custName;
    private String tranDate;
    private BigDecimal tranAmt;
    private String tranLogNo;
    private String isSecuCard;
    private String trnaChannel;
    private String batchNo;
    private String etlDt;

}
