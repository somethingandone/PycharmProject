package com.nju.demo.service.impl;

import com.nju.demo.Task.TestTask;
import com.nju.demo.exception.SseException;
import com.nju.demo.service.SseService;
import com.nju.demo.SseSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

import java.io.IOException;
import java.util.Date;
import java.util.concurrent.*;

@Service
public class SseServiceImpl implements SseService {
    private static final Logger logger = LoggerFactory.getLogger(SseServiceImpl.class);
    private static ScheduledExecutorService executors = Executors.newScheduledThreadPool(2);

    @Override
    public SseEmitter createConnection(String clientId) throws IOException {
        // 默认30秒超时,设置为0L则永不超时
        SseEmitter emitter = new SseEmitter(0L);

        logger.info("MSG: SseConnect | EmitterHash: {} | ID: {} | Date: {}", emitter.hashCode(), clientId, new Date());
        SseSession.add(clientId, emitter);
//        final ScheduledFuture<?> future = executors.schedule(new FlinkConsumer(clientId), 0, TimeUnit.SECONDS);
        final ScheduledFuture<?> future = executors.scheduleAtFixedRate(new TestTask(clientId), 0, 5, TimeUnit.SECONDS);

        emitter.onCompletion(() -> {
            logger.info("MSG: SseConnectCompletion | EmitterHash: {} |ID: {} | Date: {}", emitter.hashCode(), clientId, new Date());
            SseSession.onCompletion(clientId, future);
        });
        emitter.onTimeout(() -> {
            logger.error("MSG: SseConnectTimeout | EmitterHash: {} |ID: {} | Date: {}", emitter.hashCode(), clientId, new Date());
            SseSession.onError(clientId, new SseException("TimeOut(clientId: " + clientId + ")"));
        });
        emitter.onError(t -> {
            logger.error("MSG: SseConnectError | EmitterHash: {} |ID: {} | Date: {}", emitter.hashCode(), clientId, new Date());
            SseSession.onError(clientId, new SseException("Error(clientId: " + clientId + ")"));
        });
        return emitter;
    }

    @Override
    public String send(String clientId, Object content) {
        if (SseSession.send(clientId, content)) {
            return "Succeed!";
        }
        return "error";
    }

    @Override
    public String closeConnection(String clientId) {
        logger.info("MSG: SseConnectClose | ID: {} | Date: {}", clientId, new Date());
        if (SseSession.del(clientId)) return "Succeed!";
        return "Error!";
    }
}
