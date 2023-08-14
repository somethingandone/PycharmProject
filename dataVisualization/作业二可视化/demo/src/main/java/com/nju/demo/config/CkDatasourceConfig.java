package com.nju.demo.config;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;

@Configuration
public class CkDatasourceConfig {
    @Bean(name = "ckDataSource")
    @Qualifier("ckDataSource")
    @ConfigurationProperties(prefix = "spring.datasource")
    public DataSource ckDataSource() {
        return DataSourceBuilder.create().build();
    }
}
