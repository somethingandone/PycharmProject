package com.nju.demo.pojo.info;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;
import lombok.experimental.Accessors;

@Data
@Entity
@Accessors(chain = true)
@Table(name = "pri_cust_base_info")
public class PriCustBaseInfo {
    @Id
    private String uid;
    private String certType;
    private String custNo;
    private String custName;
    private String engName;
    private String sex;
    private String birthday;
    private String cerExpdDate;
    private String marrige;
    private String education;
    private String homePhone;
    private String mobPhone;
    private String othPhone;
    private String homeAdd;
    private String regAdd;
    private String workUnit;
    private String workUnitChar;
    private String position;
    private String career;
    private String profTitl;
    private String industry;
    private String degree;
    private String country;
    private String nationality;
    private String politicalSts;
    private String nativePlace;
    private String province;
    private String city;
    private String conty;
    private String town;
    private String village;
    private String villageGroup;
    private String community;
    private String isEmployee;
    private String isShareholder;
    private String isBlack;
    private String isContact;
    private String isNine;
    private String healthSts;
    private String badHabit;
    private String mgrName;
    private String mgrNo;
    private String mgeOrgName;
    private String mgeOrg;
    private String createDate;
    private String openOrg;
    private String openTellerNo;
    private String updateDate;
    private String updateOrg;
    private String updateTellerNo;
    private String etlDt;
    private String isMgrDep;
}