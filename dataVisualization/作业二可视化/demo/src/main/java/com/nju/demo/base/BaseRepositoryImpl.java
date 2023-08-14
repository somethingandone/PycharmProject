//package com.nju.demo.base;
//
//
//import com.nju.demo.DTO.TotalDTO;
//import com.nju.demo.DTO.UserAmtDTO;
//import jakarta.persistence.Query;
//import org.springframework.data.jpa.repository.support.JpaEntityInformation;
//import org.springframework.data.jpa.repository.support.SimpleJpaRepository;
//import jakarta.persistence.EntityManager;
//
//import java.io.Serializable;
//import java.math.BigDecimal;
//import java.util.ArrayList;
//import java.util.List;
//import java.util.Objects;
//
//public class BaseRepositoryImpl <T, ID extends Serializable> extends SimpleJpaRepository<T, ID> implements BaseRepository<T, ID> {
//
//    private static final int BATCH_SIZE = 500;
//    private EntityManager entityManager;
//
//    public BaseRepositoryImpl(JpaEntityInformation<T, ?> entityInformation, EntityManager entityManager) {
//        super(entityInformation, entityManager);
//        this.entityManager = entityManager;
//    }
//
//    public BaseRepositoryImpl(Class<T> domainClass, EntityManager entityManager) {
//        super(domainClass, entityManager);
//        this.entityManager = entityManager;
//    }
//
////    @Override
////    @Transactional(rollbackFor = Throwable.class)
////    public <S extends T> Iterable<S> batchInsert(Iterable<S> var1) {
////        Iterator<S> iterator = var1.iterator();
////        int index = 0;
////        while (iterator.hasNext()){
////            entityManager.persist(iterator.next());
////            index++;
////            if (index % BATCH_SIZE == 0){
////                entityManager.flush();
////                entityManager.clear();
////            }
////        }
////        if (index % BATCH_SIZE != 0){
////            entityManager.flush();
////            entityManager.clear();
////        }
////        return var1;
////    }
////
////    @Override
////    @Transactional(rollbackFor = Throwable.class)
////    public <S extends T> Iterable<S> batchUpdate(Iterable<S> var1) {
////        Iterator<S> iterator = var1.iterator();
////        int index = 0;
////        while (iterator.hasNext()){
////            entityManager.merge(iterator.next());
////            index++;
////            if (index % BATCH_SIZE == 0){
////                entityManager.flush();
////                entityManager.clear();
////            }
////        }
////        if (index % BATCH_SIZE != 0){
////            entityManager.flush();
////            entityManager.clear();
////        }
////        return var1;
////    }
////
////    @Override
////    public int delById(String tableName, Long id) {
////        Query nativeQuery = entityManager.createNativeQuery("alter table " + tableName + " delete where id=?");
////        nativeQuery.setParameter(1, id);
////        int count = nativeQuery.executeUpdate();
////        return count;
////    }
//
//    @Override
//    public List<UserAmtDTO> getTop20Users() {
//        return null;
//    }
//
//    @Override
//    public List<TotalDTO> getDayTotal(int year, int mon) {
//        return null;
//    }
//
//    @Override
//    public List<TotalDTO> getMonthTotal(int year) {
//        Query query = entityManager.createNativeQuery("select x.y as year, x.m as month ,x.amt as amount " +
//                "from (select" +
//                " toYear(toDateTime(et.etl_dt)) as y" +
//                " ,toMonth(toDateTime(et.etl_dt)) as m" +
//                " ,sum(et.tran_amt) as amt" +
//                "    from #{#entityName} as et" +
//                "    group by y, m) as x " +
//                "where x.y=?1 ");
//        List<Object[]> rows = query.getResultList();
//
//        List<TotalDTO> res = new ArrayList<>();
//        for (Object[] row : rows) {
//            TotalDTO dto = new TotalDTO((int) row[0], (int) row[1], (BigDecimal) row[2]);
//            res.add(dto);
//        }
//        return res;
//    }
//
//    @Override
//    public TotalDTO getByDay(String date) {
//        return null;
//    }
//
//    @Override
//    public BigDecimal getTotal() {
//        return null;
//    }
//}