package com.nju.demo.service;

import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

import java.io.IOException;

/**
 * SSE 相关业务接口
 *
 * @author zuster
 * @date 2021/1/5
 */
public interface SseService {
    /**
     * 新建连接
     *
     * @param clientId 客户端ID
     * @return
     */
    SseEmitter createConnection(String clientId) throws IOException;

    /**
     * 发送数据
     *
     * @param clientId 客户端ID
     * @return
     */
    String send(String clientId, Object content);

    /**
     * 关闭连接
     *
     * @param clientId 客户端ID
     * @return
     */
    String closeConnection(String clientId);
}
