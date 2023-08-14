package com.nju.demo.repository;

import com.nju.demo.base.BaseRepository;
import com.nju.demo.pojo.dm_v_tr_sdrq_mx;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface SdrqRepo extends BaseRepository<dm_v_tr_sdrq_mx, String> {
    @Override
    @Query(value = "select et.etl_dt, sum(et.tran_amt_fen)" +
            "from #{#entityName} as et " +
            "where toYear(toDateTime(et.etl_dt)) = ?1 " +
            "and toMonth(toDateTime(et.etl_dt)) = ?2 " +
            "group by et.etl_dt " +
            "order by et.etl_dt ", nativeQuery = true
    )
    List<Object[]> getDayTotal(int year, int mon);

    @Override
    @Query(value = "select x.y, x.m, x.amt " +
            "from (select" +
            " toYear(toDateTime(et.etl_dt)) as y" +
            " ,toMonth(toDateTime(et.etl_dt)) as m" +
            " ,sum(et.tran_amt_fen) as amt" +
            "    from #{#entityName} as et" +
            "    group by y, m) as x " +
            "where x.y=?1 ", nativeQuery = true
    )
    List<Object[]> getMonthTotal(int year);
}
