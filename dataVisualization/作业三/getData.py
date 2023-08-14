from clickhouse_driver import Client
import pandas as pd
import csv
import re

client = Client(host='172.17.153.117',
                port='19000',
                user='yajialiu',
                password='123456',
                database='dm')


def read_sql(sql):
    data, columns = client.execute(sql, columnar=True, with_column_types=True)
    df = pd.DataFrame({re.sub(r'\W', '_', col[0]): d for d, col in zip(data, columns)})
    return df


if __name__ == '__main__':
    credit_sql = """
    select distinct credit.uid as uid, credit_level,
    djk.cred_limit, djk.over_draft, djk.dlay_amt, djk.five_class, djk.bankacct_bal,
    djkfq.rem_ppl, djkfq.rem_fee,
    contract.dlay_bal, contract.dull_bal, contract.owed_int_in, contract.owed_int_out, contract.fine_pr_int,contract.fine_intr_int, contract.dlay_days, contract.five_class, contract.class_date, contract.is_bad, contract.due_intr_days,
    duebill.dlay_amt,duebill.dull_amt, duebill.bad_debt_amt,duebill.owed_int_in, duebill.owed_int_out, duebill.fine_pr_int, duebill.fine_intr_int, duebill.dlay_days, duebill.due_intr_days, duebill.vouch_type,
    base.sex,base.birthday,base.marrige , base.education, base.reg_add, base.career, base.prof_titl, base.is_employee, base.is_shareholder, base.is_contact, base.is_black,
    liabacct.five_class, liabacct.overdue_class, liabacct.overdue_flag, liabacct.owed_int_flag, liabacct.defect_type, liabacct.owed_int_in, liabacct.owed_int_out, liabacct.delay_bal,
    liab.bad_bal, liab.due_intr, liab.delay_bal
    from pri_credit_info as credit
    left join dm_v_as_djk_info as djk on credit.uid = djk.uid
    left join dm_v_as_djkfq_info as djkfq on credit.uid = djkfq.uid
    left join dm_v_tr_contract_mx as contract on credit.uid = contract.uid
    left join dm_v_tr_duebill_mx as duebill on credit.uid = duebill.uid
    left join pri_cust_base_info as base on credit.uid = base.uid
    left join pri_cust_liab_acct_info as liabacct on credit.uid = liabacct.uid
    left join pri_cust_liab_info as liab on credit.uid = liab.uid
    """

    star_sql = """
    select distinct star.uid as uid, star_level,
    asset.all_bal, asset.avg_mth, asset.avg_qur, asset.avg_year, asset.sa_bal, asset.td_bal , asset.fin_bal, asset.sa_crd_bal, asset.td_crd_bal, asset.sa_td_bal, asset.ntc_bal, asset.td_3m_bal, asset.td_6m_bal, asset.td_1y_bal, asset.td_2y_bal, asset.td_3y_bal, asset.td_5y_bal, asset.oth_td_bal, asset.cd_bal,
    base.sex,base.birthday,base.marrige , base.education, base.reg_add, base.career, base.prof_titl, base.is_employee, base.is_shareholder, base.is_contact, base.is_black,
    acct.bal,acct.avg_mth, acct.avg_qur, acct.avg_year,acct.is_secu_card,
    acct.acct_sts,acct.frz_sts,acct.stp_sts
    from pri_star_info as star
    left join pri_cust_asset_info as asset on star.uid = asset.uid
    left join pri_cust_base_info as base on star.uid = base.uid
    left join pri_cust_asset_acct_info as acct on star.uid = acct.uid
    """

    credit_train = read_sql(credit_sql +
                            """
                            where credit.credit_level <> '-1'
                            order by credit.uid;
                            """)
    print('credit训练数据检索完成！')

    star_train = read_sql(star_sql +
                          """
                          where star.star_level <> '-1'
                          order by star.uid;
                          """)
    print('star训练数据检索完成！')

    credit_train.to_csv('.\\data\\credit\\' + 'credit_train.csv', index=False, encoding='utf_8_sig')
    star_train.to_csv('.\\data\\star\\' + 'star_train.csv', index=False, encoding='utf_8_sig')

    credit_test = read_sql(credit_sql +
                           """
                           where credit.credit_level = '-1'
                           order by credit.uid;
                           """)
    print('credit测试数据检索完成！')

    star_test = read_sql(star_sql +
                         """
                         where star.star_level = '-1'
                         order by star.uid;
                         """)
    print('star测试数据检索完成！')

    credit_test.to_csv('.\\data\\credit\\' + 'credit_test.csv', index=False, encoding='utf_8_sig')
    star_test.to_csv('.\\data\\star\\' + 'star_test.csv', index=False, encoding='utf_8_sig')
