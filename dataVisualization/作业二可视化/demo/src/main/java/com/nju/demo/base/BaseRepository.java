package com.nju.demo.base;


import com.nju.demo.DTO.TotalDTO;
import com.nju.demo.DTO.UserAmtDTO;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.NoRepositoryBean;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.List;

@NoRepositoryBean
public interface BaseRepository<T, ID extends Serializable> extends JpaRepository<T, ID>, JpaSpecificationExecutor<T> {

    @Query(value = "select new com.nju.demo.DTO.UserAmtDTO(et.uid, pcbi.custName, et.etlDt , sum(et.tranAmt))" +
            "from #{#entityName} as et, PriCustBaseInfo pcbi " +
            "where et.uid = pcbi.uid and et.etlDt = ?1 " +
            "group by et.uid,pcbi.custName,et.etlDt " +
            "order by et.etlDt, sum(et.tranAmt) desc limit 5")
    List<UserAmtDTO> getTop5Users(String date);

    @Query(value = "select et.etl_dt, sum(et.tran_amt)" +
            "from #{#entityName} as et " +
            "where toYear(toDateTime(et.etl_dt)) = ?1 " +
            "and toMonth(toDateTime(et.etl_dt)) = ?2 " +
            "group by et.etl_dt " +
            "order by et.etl_dt ", nativeQuery = true
    )
    List<Object[]> getDayTotal(int year, int mon);

    @Query(value = "select x.y, x.m, x.amt " +
            "from (select" +
            " toYear(toDateTime(et.etl_dt)) as y" +
            " ,toMonth(toDateTime(et.etl_dt)) as m" +
            " ,sum(et.tran_amt) as amt" +
            "    from #{#entityName} as et" +
            "    group by y, m) as x " +
            "where x.y=?1 ", nativeQuery = true
    )
    List<Object[]> getMonthTotal(int year);

    @Query(value = "select new com.nju.demo.DTO.TotalDTO(et.etlDt, sum(et.tranAmt))" +
            "from #{#entityName} as et " +
            "where et.etlDt= ?1 " +
            "group by et.etlDt " +
            "order by et.etlDt "
    )
    TotalDTO getByDay(String date);

    @Query(value = "select sum(et.tranAmt)" +
            "from #{#entityName} as et"
    )
    BigDecimal getTotal();

}