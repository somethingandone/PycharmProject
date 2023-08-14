package com.nju.demo.web;

import com.nju.demo.service.SseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

import java.io.IOException;

@Controller
@RequestMapping("/visualization")
@CrossOrigin
public class SseController {
    @Autowired
    private SseService sseService;

    @GetMapping
    public String visualization() {return "visualization";}

    /**
     * 创建SSE长链接
     *
     * @param clientId   客户端唯一ID(如果为空，则由后端生成并返回给前端)
     * @return org.springframework.web.servlet.mvc.method.annotation.SseEmitter
     **/
    @GetMapping("/createConnection")
    public SseEmitter createSseConnect(@RequestParam(name = "clientId", required = false) String clientId) throws IOException {
        clientId = "1";
        return sseService.createConnection(clientId);
    }

    /**
     * 关闭SSE连接
     *
     * @param clientId 客户端ID
     **/
    @GetMapping("/closeConnection")
    public String closeSseConnect(String clientId) {
        sseService.closeConnection(clientId);
        return "visualization";
    }
}
