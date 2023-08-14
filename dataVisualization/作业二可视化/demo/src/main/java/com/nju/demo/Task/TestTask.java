package com.nju.demo.Task;

import com.nju.demo.SseSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Date;

public class TestTask implements Runnable {

    private static final Logger logger = LoggerFactory.getLogger(TestTask.class);
    private final String clientId;

    public TestTask(String clientId) {
        this.clientId = clientId;
    }

    @Override
    public void run() {
        logger.info("MSG: SseTask | ID: {} | Date: {}", clientId, new Date());
        SseSession.send(clientId, "123");
    }
}
