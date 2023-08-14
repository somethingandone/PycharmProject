package com.nju.demo.repository;

import com.nju.demo.base.BaseRepository;
import com.nju.demo.pojo.dm_v_tr_contract_mx;

import java.util.List;

public interface ContractRepo extends BaseRepository<dm_v_tr_contract_mx, String> {

    List<dm_v_tr_contract_mx> findAllByEtlDt(String date);

}
