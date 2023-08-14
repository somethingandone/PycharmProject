package com.nju.demo;

import com.nju.demo.DTO.TotalDTO;
import com.nju.demo.DTO.UserAmtDTO;
import com.nju.demo.base.BaseRepository;
import com.nju.demo.pojo.dm_v_tr_djk_mx;
import com.nju.demo.repository.ContractRepo;
import com.nju.demo.repository.DjkRepo;
import com.nju.demo.repository.EtcRepo;
import com.nju.demo.service.ChartsService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Arrays;
import java.util.List;

@SpringBootTest
class DemoApplicationTests {

	@Autowired
	DjkRepo djkRepo;
	@Autowired
	ContractRepo contractRepo;
	@Autowired
	EtcRepo etcRepo;
	@Autowired
	ChartsService chartsService;

	@Test
	void connectionTest() {
		List<dm_v_tr_djk_mx> djkMxes = djkRepo.findAll();
		for (dm_v_tr_djk_mx djkMx : djkMxes) {
			System.out.println(djkMx.getUid());
		}
	}

	@Test
	void topUserTest() {
		List<UserAmtDTO> userAmtDTOS = etcRepo.getTop5Users("2021-01-01");
		for (UserAmtDTO userAmtDTO : userAmtDTOS) {
			System.out.println(userAmtDTO.toString());
		}
	}

//	@Test
//	void DayTotal() {
//		List<TotalDTO> map = etcRepo.getDayTotal();
//		for (TotalDTO entry : map) {
//			System.out.println(entry.toString());
//		}
//	}

	@Test
	void totalByDay(){
		BaseRepository repo = djkRepo;
		TotalDTO dto = repo.getByDay("2021-03-08");
		System.out.println(dto.toString());
	}

	@Test
	void getYearChartTest() {
		ChartData data = chartsService.getYearChart("sbyb",2021);
		System.out.println(data.getSize());
		System.out.println(Arrays.toString(data.getAmounts().toArray()));
	}

	@Test
	void getMonthChartTest() {
		ChartData data = chartsService.getMonthChart("djk", 2021, 1);
		System.out.println(data.getSize());
		System.out.println(Arrays.toString(data.amounts.toArray()));
	}

	@Test
	void topUsersTest() {
		RankData rankData = chartsService.getTop5UsersAtDay("贷记卡", "2021-01-01");
		System.out.println(Arrays.toString(rankData.names.toArray()));
	}

}
