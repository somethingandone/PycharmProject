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
@Table(name = "dm_v_tr_shop_mx")
public class dm_v_tr_shop_mx extends Data_mx {
    @Id
    private String uid;
    private String tranChannel;
    private String orderCode;
    private String shopCode;
    private String shopName;
    private String hlwTranType;
    private String tranDate;
    private String tranTime;
    private BigDecimal tranAmt;
    private String currentStatus;
    private BigDecimal scoreNum;
    private String payChannel;
    private String legalName;
    private String etlDt;

}
