package com.abhi;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import com.abhi.component.Laptop;

@Configuration
@ComponentScan(basePackages = "com.abhi")
public class SpringConfig {
	
	@Bean(name = "laptop")
	public Laptop getLaptop()
	{
		return new Laptop();
	}

}
